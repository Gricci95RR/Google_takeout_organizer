import os
import shutil
from pathlib import Path

# --- START CONFIGURATION ---

# 1. Add the full paths to your extracted Google Takeout "Google Photos" folders here.
SOURCE_DIRECTORIES = [
    r"/path/to/takeout-20260627T164913Z-3-001/Takeout/Google Photos",
    r"/path/to/takeout-20260627T164913Z-3-002/Takeout/Google Photos",
]

# 2. Add the single directory where you want all your organized albums to end up.
DESTINATION_DIRECTORY = r"/path/to/Output/Directory"

# 3. Set to True to copy Google Takeout JSON files, False to skip them.
COPY_JSON_FILES = False

# --- END CONFIGURATION ---

def merge_directories():
    dest_path = Path(DESTINATION_DIRECTORY)

    # Create the main destination folder if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)

    # Open the list of source directories one by one
    for src in SOURCE_DIRECTORIES:
        src_path = Path(src)

        if not src_path.exists() or not src_path.is_dir():
            print(f"⚠️ Skipping invalid source directory: {src_path}")
            continue

        print(f"🔍 Scanning source directory: {src_path}")

        # List all directories (albums/years) available inside the source
        for album_dir in src_path.iterdir():
            if album_dir.is_dir():
                album_name = album_dir.name

                # Create a matching directory in the destination folder
                target_album_dir = dest_path / album_name
                target_album_dir.mkdir(parents=True, exist_ok=True)

                # Copy files from the source album to the target album
                for file_path in album_dir.iterdir():
                    if file_path.is_file():

                        # Skip JSON files if disabled
                        if not COPY_JSON_FILES and file_path.suffix.lower() == ".json":
                            print(f"  Skipped JSON: {file_path.name}")
                            continue

                        target_file_path = target_album_dir / file_path.name

                        # Only copy if the file doesn't already exist
                        if not target_file_path.exists():
                            shutil.copy2(file_path, target_file_path)
                            print(f"  Copied: {file_path.name} -> {album_name}/")
                        else:
                            print(f"  Skipped (Already exists): {file_path.name}")

if __name__ == "__main__":
    print("🚀 Starting the merging process...")
    merge_directories()
    print("✅ All done! Your photos have been consolidated.")