# Automated File to Markdown Converter

This tool automatically detects and converts files (PDF, Word, Excel, Images, etc.) from a folder into Markdown format using Microsoft's MarkItDown.

## Quick Start

### 1. First-Time Setup
Run the setup script to install system dependencies (ffmpeg, exiftool) and create the Python virtual environment.

```
bash setup.sh
```

### 2. Add Your Files

Put all the documents you want to convert into the raw_files folder that was just created.

### 3. Run the Converter

Run the processor script. It will convert everything in raw_files and save the results to markdown_outputs.

```
bash run.sh
```