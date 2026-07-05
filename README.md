# Google Takeout Organizer

A lightweight, zero-dependency Python utility designed to merge multiple split Google Takeout "Google Photos" archives into a single, organized directory.

---

## Getting Started

### 1. Prerequisites

You only need **Python 3.6 or higher** installed on your system.

* **Check Python installation:** Open your terminal or command prompt and run:
```bash
python --version

```
*(Note: On some macOS/Linux systems, you may need to use `python3 --version`)*

### 2. Downloading the Repository

You can get the code onto your local machine using either of the following methods:

#### Option A: Using Git (Recommended)

Clone the repository using your terminal:

```bash
git clone https://github.com/YOUR_USERNAME/Google_takeout_organizer.git
cd Google_takeout_organizer

```

#### Option B: Manual Download

1. Click the **Code** button at the top right of this GitHub page.
2. Select **Download ZIP**.
3. Extract the ZIP file anywhere on your computer and open that folder.

---

## ⚙️ Configuration & Parameter Setup

Before running the script, you need to tell it where your files are located. Open the script (`google_takeout_organizer.py`) in any text editor or IDE and locate the `--- START CONFIGURATION ---` block.

Modify the following three variables:

```python
# 1. Add the full paths to your extracted Google Takeout "Google Photos" folders here.
SOURCE_DIRECTORIES = [
    r"/path/to/takeout-20260627T164913Z-3-001/Takeout/Google Photos",
    r"/path/to/takeout-20260627T164913Z-3-002/Takeout/Google Photos",
]

# 2. Add the single directory where you want all your organized albums to end up.
DESTINATION_DIRECTORY = r"/path/to/Output/Directory"

# 3. Set to True to copy Google Takeout JSON files, False to skip them.
COPY_JSON_FILES = False

```

---

## How to Use

Once your configuration is saved, open your terminal/command prompt, navigate to the script's directory, and execute it.

* **On Windows:**
```cmd
python main.py

```


* **On macOS / Linux:**
```bash
python3 main.py

```

1. The script will safely scan each source directory.
2. It will recreate your album structures inside your destination directory.
3. If a file already exists in the destination folder, **it will skip it** to save time and prevent duplicates.
4. You will see a live console log of files being copied, skipped, or omitted.
