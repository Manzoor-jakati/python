import os
from pathlib import Path

# 1. Define folder rules
DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Archives": [".zip", ".tar", ".rar"]
}

target_dir = Path.home() / "Desktop" / "TestFolder"

for item in target_dir.iterdir():
    # Skip directories, only process files
    if item.is_dir():
        continue

    file_ext = item.suffix.lower()

    # Loop through our dictionary to find where this file belongs
    for category, extensions in DIRECTORIES.items():
        if file_ext in extensions:
            # Create category folder path (e.g., TestFolder/Images)
            category_path = target_dir / category
            category_path.mkdir(exist_ok=True)

            # Move the file into the new folder
            destination = category_path / item.name
            item.rename(destination)
            print(f"Moved {item.name} -> {category}")
            break