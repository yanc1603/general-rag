#!/bin/bash

# Stop on error
set -e

echo "Installing system dependencies..."
# ffmpeg is for audio support; libimage-exiftool-perl is for metadata
sudo apt update
sudo apt install -y python3 python3-pip python3-venv ffmpeg libimage-exiftool-perl

echo "creating Python virtual environment..."
python3 -m venv .venv

echo "Installing MarkItDown..."
source .venv/bin/activate
pip install --upgrade pip
pip install "markitdown[all]"

echo "Creating input folder..."
mkdir -p raw_files

echo ""
echo "Setup Complete!"
echo "Put your documents in the 'raw_files' folder."
echo "Then run 'bash run.sh' to convert them."