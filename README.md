📄 PY-TASKS-8 – File Organizer with Automation

4th Week Internship Project – Cortexis Solution Hub

📝 Project Title

File Organizer with Automation (Python + OS Handling)

🎯 Objective

The objective of this task is to build a Python program that automatically organizes files inside a selected folder into subfolders based on their file type.
This improves folder management, reduces clutter, and saves time.

⚙️ Core Requirements

Input Folder

User provides a folder path.

Program scans all files inside.

File Categorization

Images → .jpg, .jpeg, .png, .gif

Videos → .mp4, .mkv, .avi

Documents → .pdf, .docx, .txt

Music → .mp3, .wav

Others → Any other file types

Automation

Creates category subfolders automatically (if not present).

Moves each file into its respective folder.

Logs

Generates a log.txt file with details of moved files (supports UTF-8 encoding).

🛠️ Tools & Libraries Used

Python 3.x

os → File & directory handling

shutil → Moving files

datetime → Adding timestamps in logs

tkinter (optional) → GUI for browsing folders

schedule (optional) → For running the script periodically

💻 Implementation
🔹 Main Script (FileOrganizer.py)

Accepts folder path from user.

Categorizes files into predefined groups.

Creates subfolders (Images, Videos, Documents, Music, Others).

Moves files into respective folders.

Maintains log history in log.txt.

📂 Example Workflow
📁 Before Running Script
Downloads/
 ├── photo.jpg
 ├── resume.docx
 ├── song.mp3
 ├── movie.mp4
 ├── notes.txt
 └── random.exe

📁 After Running Script
Downloads/
 ├── Images/
 │    └── photo.jpg
 ├── Documents/
 │    ├── resume.docx
 │    └── notes.txt
 ├── Music/
 │    └── song.mp3
 ├── Videos/
 │    └── movie.mp4
 ├── Others/
 │    └── random.exe
 └── log.txt

📜 Example Log File
=== Run at 2025-09-17 07:30:12.123456 ===
photo.jpg → Images
resume.docx → Documents
song.mp3 → Music
movie.mp4 → Videos
notes.txt → Documents
random.exe → Others

🚀 Advanced Features (Optional)

GUI with Tkinter – User selects folder with Browse button.

Scheduling – Script runs every X minutes automatically.

Undo Option – Restore files to original location using log history.

✅ Conclusion

This project successfully demonstrates the use of Python + OS handling for file automation.
It fulfills the internship requirement by:

Organizing files into categories.

Creating folders automatically.

Maintaining logs.

Reducing manual effort and improving efficiency.

📌 Project Name: PY-TASKS-8
📌 Week: 4th Week
📌 Organization: CORTEXIS SOLUTION HUB



