from pathlib import Path

# 1. Define the file categories
DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".txt", ".docx", ".pdf", ".xls"],
    "Archives": [".zip", ".tar", ".rar"]
}

# 2. Define the folder we want to organize
target_dir = Path.home() / "Desktop" / "TestFolder"

# 3. Look at every item inside the target folder
for item in target_dir.iterdir():

    # 4. Ignore folders
    if item.is_dir():
        continue

    # 5. Get the file extension
    file_ext = item.suffix.lower()

    # 6. Assume the file is unknown
    category = "Other"

    # 7. Check which category the extension belongs to
    for folder, extensions in DIRECTORIES.items():
        if file_ext in extensions:
            category = folder
            break

    # 8. Create the category folder if it doesn't exist
    category_path = target_dir / category
    category_path.mkdir(exist_ok=True)

    # 9. Create the final destination
    destination = category_path / item.name

    # 10. Move the file
    item.rename(destination)

    print(f"Moved {item.name} -> {category}")
