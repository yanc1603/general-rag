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

## Prompt to generate Fuzzy Search JSON with AI

Ensure that you add the specific files for each case.

```
Create a JSON file using the exact schema/structure of the uploaded general_fs.json file, but populate it exclusively with the information from general_RAG.md.

Critical Instructions:

    Granularity: Do not combine large sections of text into a single answer. Break the information down into specific, granular Q&A pairs. For example, instead of one general entry for a product/topic, create separate entries for its 'Definition', 'Features', 'Benefits', and 'Use Cases'.

    Data Isolation: Do not include any data or text from the example JSON file. Use it only for the code structure.

    Triggers: Create varied and natural user queries (triggers) relevant to each specific answer.
```

The example for structure of the FS JSON is in [general_fs.json](/documents/examples_FS/general_fs.json)


An expected output can be seen, when using the following [octopy_RAG.md](/documents/examples_RAG/octopy_RAG/octopy_RAG.md), in [octopy_fs.json](/documents/examples_FS/octopy_fs.json) 