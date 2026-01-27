# General RAG - File to Markdown Converter

[![Python](https://img.shields.io/badge/Python-v3.8+-3776AB.svg?style=plastic&logo=python)](https://www.python.org/)

---
## Abstract

This project is an automated pipeline designed to convert various raw file formats (PDF, Word, Excel, Images, Audio, etc.) into clean Markdown format using Microsoft's MarkItDown. 

**Main Goal:** To generate two critical assets for your AI agents:
1. **RAG Knowledge Base (Markdown)**: A clean, structured markdown file for Retrieval-Augmented Generation.
2. **Fuzzy Search Dataset (JSON)**: A structured JSON file for high-precision fuzzy search queries.

---
## Features

- **Dual Output Generation**: Facilitates creation of both RAG Markdown and Fuzzy Search JSON.
- **Batch Processing**: Automatically detects and processes all files in the input directory.
- **Multi-Format Support**: Handles PDFs, Office documents, images (with EXIF/OCR), and audio files.
- **Automated Setup**: Includes self-contained scripts for environment and dependency management.

---
## Table of Contents

- [Requirements](#requirements)
    - [Software](#software)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Workflow: RAG & JSON Generation](#workflow-rag--json-generation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

---
## Requirements

### Software
- **Operating System**: Linux (Scripts utilize `apt` for system dependencies).
- **Python**: Version 3.8 or higher.
- **System Tools**: `ffmpeg`, `libimage-exiftool-perl` (Installed automatically via setup script).

---

## Quick Start

### Step 1. First-Time Setup
Run the setup script to install system dependencies and create the Python virtual environment.
```bash
bash setup.sh
```

### Step 2. Curate Your Content (CRITICAL)
Before adding files, you **must** review your documents:
- **Remove figurative expressions** (metaphors, idioms) that confuse AI models.
- **Delete inaccurate or ambiguous info** that could lead to hallucinations.
- Ensure the text is factual, clear, and direct.
- **Avoid content repetition** and mantain a clear and concise structure.

### Step 3. Add Your Files
Place your **curated** documents into the `raw_files` directory.
*(Note: This folder is created automatically during setup)*

### Step 4. Run the Converter
Execute the runner script to convert documents to markdown.
```bash
bash run.sh
```

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/yanc1603/general-rag.git
cd general-rag
```

**2. Run Automated Setup**
The `setup.sh` script handles all dependency installation:
- Updates `apt` repositories.
- Installs `ffmpeg` and `exiftool`.
- Creates a Python `.venv`.
- Installs `markitdown` and other Python libraries.

```bash
bash setup.sh
```

---

## Configuration

The project uses a simple folder-based configuration defined in `main.py`:

- **Input**: `raw_files/` - Place extraction targets here.
- **Output**: `markdown_outputs/` - Converted files appear here.

---

## Project Structure

```bash
├── documents/          # Reference RAG structures and JSON examples
│   ├── examples_FS/    # Fuzzy Search JSON templates
│   └── examples_RAG/   # Markdown structure templates
├── markdown_outputs/   # (Generated) Converted Markdown files
├── raw_files/          # (Input) Place raw documents here
├── main.py             # Core conversion logic
├── run.sh              # Execution wrapper script
├── setup.sh            # Environment setup script
└── README.md           # Project documentation
```

---

## Workflow: RAG & JSON Generation

This workflow produces both the **RAG Markdown** and the **Fuzzy Search JSON**.

### Step 1: Pre-Processing & Curation
**Goal:** Prepare clean input data.
- Open your source documents (PDF, Docx, etc.).
- **Sanitize the text**: Remove marketing fluff, metaphors, and ambiguous language.
- **Fact-check**: Remove outdated or incorrect information.
- Save the gathered files to `raw_files/`.

### Step 2: Automated Conversion
**Goal:** Convert curated files to Markdown.
Run `bash run.sh`. The script will output raw markdown files to `markdown_outputs/`.

### Step 3: Post-Processing Verification
**Goal:** Create the final `general_rag.md`.
- Review the generated Markdown in `markdown_outputs/`.
- Fix any formatting errors introduced during conversion.
- Consolidate relevant sections into a single, clean `general_rag.md` file.

### Step 4: AI Processing (Gemini 3 Pro)
**Goal:** Generate `fuzzy_search.json` from `general_rag.md`.
Use **Gemini 3 Pro** with the following prompt:

**Prompt Template:**
```text
Create a JSON file using the exact schema/structure of the uploaded general_fs.json file, but populate it exclusively with the information from my attached curated markdown file (general_rag.md).

Critical Instructions:
1. Granularity: Does not combine large sections. Break info into specific Q&A pairs.
2. Data Isolation: Do not include text from the example JSON. Use it only for structure.
3. Triggers: Create varied and natural user queries for each answer.
```

**Reference Files:**
- JSON Structure: [general_fs.json](documents/examples_FS/general_fs.json)
- RAG Example: [octopy_RAG.md](documents/examples_RAG/octopy_RAG/octopy_RAG.md)
- Output Example: [octopy_fs.json](documents/examples_FS/octopy_fs.json)

---

## Troubleshooting

**Problem:** `ffmpeg` or `exiftool` not found.
**Solution:** Ensure you ran `bash setup.sh` with sudo privileges, or install them manually via `sudo apt install ffmpeg libimage-exiftool-perl`.

---

## Credits

- **MarkItDown**: Microsoft's tool for file conversion.