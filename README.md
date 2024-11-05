File Organizer Automation
This is a Python script that automatically organizes downloaded files by moving them into specific folders on your Desktop based on their file type. For example, all .pdf files are moved to a "PDFs" folder, .mp4 files to an "MP4s" folder, and so on. The script continuously monitors the Downloads folder, so any new files downloaded are sorted and placed in the appropriate folder automatically.

Features
Automated Sorting: Automatically moves files to designated folders based on file extension.
Continuous Monitoring: Runs continuously, checking for new files every 10 seconds.
Customizable: You can easily add more file types or change folder locations.
Setup Instructions
Requirements:

Python 3.x installed on your computer.
Folder Structure:

By default, this script will move files from your Downloads folder to folders on your Desktop.
Ensure the PDFs, MP4s, MP3s, and Images folders exist on your Desktop, or the script will create them for you.
How to Use:

Download or clone this repository to your machine.

Open a terminal or command prompt and navigate to the directory containing the script.

Run the script by typing:

bash
Copy code
python file_organizer.py
The script will start monitoring your Downloads folder and will automatically sort any new .pdf, .mp4, .mp3, .jpg, .jpeg, .png, or .gif files it finds.

Configuration
Folder Paths: The script is configured to work with a standard Downloads and Desktop setup on Windows. If you want to change the destination folders, edit the desktop_folder variable and the folders dictionary.
Extensions: You can add more file types by adding entries to the extensions dictionary in the script.
Example
If you download a file called example.pdf, the script will detect it in your Downloads folder and move it to the "PDFs" folder on your Desktop.

Notes
The script runs in an infinite loop, checking for new files every 10 seconds.
To stop the script, press Ctrl+C in the terminal.
