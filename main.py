import os
from markitdown import MarkItDown


# --- CONFIGURATION ---
INPUT_FOLDER = 'raw_files'          # Place your source files here
OUTPUT_FOLDER = 'markdown_outputs'  # Results will appear here
# ---------------------


def process_files():
    # Initialize MarkItDown
    md = MarkItDown()

    # Ensure directories exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Created output directory: {OUTPUT_FOLDER}")

    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
        print(f"Created input directory: '{INPUT_FOLDER}'. Please put your files in here.")
        return

    # List files
    files = [f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]
    
    if not files:
        print(f"No files found in '{INPUT_FOLDER}'.")
        return

    print(f"Found {len(files)} files. Starting conversion...\n")

    for filename in files:
        file_path = os.path.join(INPUT_FOLDER, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}.md")

        print(f"Processing: {filename}...")
        
        try:
            # 4. Convert
            result = md.convert(file_path)
            
            # 5. Save
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result.text_content)
            
            print(f"  [OK] Saved to {output_path}")

        except Exception as e:
            print(f"  [ERROR] Failed: {e}")

    print("\nProcessing complete.")

if __name__ == "__main__":
    process_files()