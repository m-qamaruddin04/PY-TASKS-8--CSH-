import os
import shutil
from datetime import datetime

# Define categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"]
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    log_entries = []

    # Scan through files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find category
        category = "Others"
        for cat, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                category = cat
                break

        # Create category folder if not exists
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)

        # Move file
        new_path = os.path.join(category_path, filename)
        shutil.move(file_path, new_path)

        # Log entry
        log_entries.append(f"{filename} → {category}")

    # Write logs (UTF-8 to avoid UnicodeEncodeError)
    log_file = os.path.join(folder_path, "log.txt")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write("\n=== Run at " + str(datetime.now()) + " ===\n")
        for entry in log_entries:
            f.write(entry + "\n")

    print("✅ Files organized successfully. Log saved in log.txt")


# ----------------- RUN -----------------
if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()
    organize_files(folder)

