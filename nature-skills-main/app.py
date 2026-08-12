#!/usr/bin/env python3
"""
Nature Paper Checker - Web Interface
====================================
FastAPI web frontend for nature_checker CLI tool.

Usage: python app.py
Visit: http://127.0.0.1:5000
"""

import io
import shutil
import zipfile
from datetime import datetime
from pathlib import Path

import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

from nature_checker.pipeline import run_pipeline

app = FastAPI(title="Nature Paper Checker", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True)

STATIC_DIR = Path("static")
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    index = STATIC_DIR / "index.html"
    return FileResponse(index) if index.exists() else {"message": "API", "docs": "/docs"}


@app.post("/api/upload")
async def upload_paper(file: UploadFile = File(...)):
    allowed = {".md", ".docx", ".txt"}
    ext = Path(file.filename).suffix.lower()
    if ext not in allowed:
        raise HTTPException(400, f"Unsupported format. Allowed: {', '.join(allowed)}")

    content = await file.read()
    if len(content) > 10 * 1024 * 1024:
        raise HTTPException(400, "File too large. Max 10MB")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    session_dir = TEMP_DIR / timestamp
    session_dir.mkdir(parents=True, exist_ok=True)

    try:
        input_path = session_dir / file.filename
        input_path.write_bytes(content)

        output_base = session_dir / "result"
        result = run_pipeline(input_path=input_path, output_path=output_base)

        written = result["written"]
        polished = Path(written["polished"]).read_text(encoding="utf-8")
        revision = Path(written["revision"]).read_text(encoding="utf-8")
        compliance = Path(written["compliance"]).read_text(encoding="utf-8")

        report = result["report"]
        stats = {
            "total_issues": report.stats.get("total_issues", len(report.issues)),
            "mean_words_per_sentence": report.stats.get("overall_avg_words", "n/a"),
            "sentences_over_30": report.stats.get("over_30_count", 0),
            "max_sentence_length": report.stats.get("max_words", 0),
        }

        return {
            "success": True,
            "session_id": timestamp,
            "filename": file.filename,
            "stats": stats,
            "results": {
                "polished": polished,
                "revision_notes": revision,
                "compliance_report": compliance,
            },
        }

    except Exception as e:
        if session_dir.exists():
            shutil.rmtree(session_dir, ignore_errors=True)
        raise HTTPException(500, f"Processing failed: {str(e)}")


@app.get("/api/download/{session_id}")
async def download_results(session_id: str):
    session_dir = TEMP_DIR / session_id
    if not session_dir.exists():
        raise HTTPException(404, "Session not found")

    try:
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in session_dir.glob("result*.md"):
                zf.write(f, f.name)
        buf.seek(0)
        return StreamingResponse(
            buf,
            media_type="application/zip",
            headers={"Content-Disposition": f"attachment; filename=results_{session_id}.zip"},
        )
    except Exception as e:
        raise HTTPException(500, f"Download failed: {str(e)}")


@app.delete("/api/cleanup")
async def cleanup_old_files(max_age_hours: int = 24):
    try:
        import time
        current = time.time()
        deleted = 0
        for d in TEMP_DIR.iterdir():
            if d.is_dir() and (current - d.stat().st_mtime) / 3600 > max_age_hours:
                shutil.rmtree(d, ignore_errors=True)
                deleted += 1
        return {"success": True, "deleted_sessions": deleted}
    except Exception as e:
        raise HTTPException(500, f"Cleanup failed: {str(e)}")


@app.get("/api/health")
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    print("=" * 60)
    print("Nature Paper Checker - Web Interface")
    print("=" * 60)
    print("\n📝 Visit: http://127.0.0.1:5000")
    print("📚 Docs: http://127.0.0.1:5000/docs\n")
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
