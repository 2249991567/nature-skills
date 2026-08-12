"""Nature-polishing paper checker and polisher.

Rules are sourced exclusively from nature-polishing/ (SKILL.md + references/).
"""

__version__ = "1.0.0"

from .pipeline import run_pipeline, polish_text

__all__ = ["run_pipeline", "polish_text", "__version__"]
