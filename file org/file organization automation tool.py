import os
import shutil
import time

# Path to your Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Define the target directory on your Desktop
desktop_folder = r"C:\Users\Nani3\OneDrive\Desktop"

# Define the folder paths for each file type
folders = {
    "pdf": os.path.join(desktop_folder, "PDFs"),
    "mp4": os.path.join(desktop_folder, "MP4s"),
    "mp3": os.path.join(desktop_folder, "MP3s"),
    "images": os.path.join(desktop_folder, "Images"),
}

# Create folders on the Desktop if they don't exist
for folder in folders.values():
    os.makedirs(folder, exist_ok=True)

# File extensions mapping
extensions = {
    ".pdf": folders["pdf"],
    ".mp4": folders["mp4"],
    ".mp3": folders["mp3"],
    ".jpg": folders["images"],
    ".jpeg": folders["images"],
    ".png": folders["images"],
    ".gif": folders["images"],
}

def organize_files():
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension and corresponding folder
        file_ext = os.path.splitext(filename)[1].lower()
        target_folder = extensions.get(file_ext)

        # If the file has a target folder, move it
        if target_folder:
            target_path = os.path.join(target_folder, filename)
            shutil.move(file_path, target_path)
            print(f"Moved: {filename} -> {target_folder}")

def main():
    print("Monitoring Downloads folder...")
    while True:
        organize_files()
        # Wait for a few seconds before scanning again
        time.sleep(10)

if __name__ == "__main__":
    main()
