const { createApp } = Vue;

createApp({
    data() {
        return {
            selectedFile: null,
            uploading: false,
            processing: false,
            isDragging: false,
            results: null,
            sessionId: null,
            activeTab: 'polished',
            error: null
        };
    },
    methods: {
        triggerFileInput() {
            this.$refs.fileInput.click();
        },
        handleFileSelect(event) {
            const file = event.target.files[0];
            if (file) this.validateAndSetFile(file);
        },
        handleDrop(event) {
            this.isDragging = false;
            const file = event.dataTransfer.files[0];
            if (file) this.validateAndSetFile(file);
        },
        validateAndSetFile(file) {
            this.error = null;
            const allowed = ['.md', '.docx', '.txt'];
            const ext = '.' + file.name.split('.').pop().toLowerCase();
            if (!allowed.includes(ext)) {
                this.error = `Unsupported format. Allowed: ${allowed.join(', ')}`;
                return;
            }
            if (file.size > 10 * 1024 * 1024) {
                this.error = 'File too large. Max 10MB';
                return;
            }
            this.selectedFile = file;
        },
        async uploadFile() {
            if (!this.selectedFile) return;
            this.uploading = true;
            this.processing = true;
            this.error = null;
            
            const formData = new FormData();
            formData.append('file', this.selectedFile);
            
            try {
                const response = await axios.post('/api/upload', formData, {
                    headers: {'Content-Type': 'multipart/form-data'}
                });
                this.results = response.data;
                this.sessionId = response.data.session_id;
                this.activeTab = 'polished';
            } catch (err) {
                this.error = err.response?.data?.detail || 'Failed to process file';
                this.processing = false;
            } finally {
                this.uploading = false;
            }
        },
        async downloadResults() {
            if (!this.sessionId) return;
            try {
                const response = await axios.get(`/api/download/${this.sessionId}`, {
                    responseType: 'blob'
                });
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', `results_${this.sessionId}.zip`);
                document.body.appendChild(link);
                link.click();
                link.remove();
                window.URL.revokeObjectURL(url);
            } catch (err) {
                this.error = 'Failed to download results';
            }
        },
        reset() {
            this.selectedFile = null;
            this.results = null;
            this.sessionId = null;
            this.processing = false;
            this.uploading = false;
            this.error = null;
            this.activeTab = 'polished';
            this.$refs.fileInput.value = '';
        },
        formatFileSize(bytes) {
            if (bytes < 1024) return bytes + ' B';
            if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
            return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
        },
        renderMarkdown(content) {
            if (!content) return '';
            let html = marked.parse(content);
            html = html.replace(/\bGreen\b/g, '<span class="traffic-light green">Green</span>');
            html = html.replace(/\bYellow\b/g, '<span class="traffic-light yellow">Yellow</span>');
            html = html.replace(/\bRed\b/g, '<span class="traffic-light red">Red</span>');
            return html;
        }
    }
}).mount('#app');
