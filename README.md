# Google Takeout Organizer

A lightweight, zero-dependency Python utility designed to merge multiple split Google Takeout "Google Photos" archives into a single, organized directory.

 

## 📌 Table of Contents

1. [🚀 Getting Started](https://www.google.com/search?q=%23-getting-started)
* [Prerequisites](https://www.google.com/search?q=%231-prerequisites)
* [Downloading the Repository](https://www.google.com/search?q=%232-downloading-the-repository)


2. [⚙️ Configuration & Parameter Setup](https://www.google.com/search?q=%23%EF%B8%8F-configuration--parameter-setup)
3. [💻 How to Run the Script](https://www.google.com/search?q=%23-how-to-run-the-script)
4. [📦 Appendix: Preparing Your Google Takeout Data](https://www.google.com/search?q=%23-appendix-preparing-your-google-takeout-data)

 

## 🚀 Getting Started

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

 

## ⚙️ Configuration & Parameter Setup

Before running the script, you need to tell it where your files are located. Open the script (`google_takeout_organizer.py`) in any text editor or IDE and locate the `  START CONFIGURATION  ` block.

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

 

## 💻 How to run the script

Once your configuration is saved, open your terminal/command prompt, navigate to the script's directory, and execute it.

* **On Windows:**

```cmd
python main.py

```

* **On macOS / Linux:**

```bash
python3 main.py

```

 

## 📦 Appendix: Preparing Your Google Takeout Data

Because large photo libraries are often split into multiple `.zip` archives by Google, follow these steps exactly to export your data correctly before running the script:

1. **Go to Google Takeout:** Open your browser and navigate to [takeout.google.com](https://takeout.google.com).
2. **Select Only Google Photos:**
* Click **Deselect all** at the top of the list to uncheck other Google services.
* Scroll down to find **Google Photos** and check the box next to it.
* *(Optional)* Click **All photo albums included** to filter out specific years or albums you don't want to download.


3. **Configure Export Settings:** Scroll to the bottom of the page and click **Next step**.
4. **Choose Destination & Frequency:** Set your destination (usually *Transfer to email/Download link*) and frequency (*Export once*).
5. **Set File Type & Size (Crucial):**
* Leave File type as **.zip**.
* Change the **File size** dropdown to **50 GB**. *Choosing a larger size like 50 GB prevents Google from splitting your library into dozens of small zip files.*


6. **Create Export:** Click **Create export**. Google will compile your photos and email you when the download links are ready.
7. **Download & Extract:** * Download all the provided ZIP files to your computer.
* **Unzip/Extract all files** completely using your system's built-in extractor, or tools like 7-Zip (Windows) / Unarchive (Mac).
* *Note down the paths of the extracted folders containing `/Takeout/Google Photos`—you will need them for the script configuration!*
