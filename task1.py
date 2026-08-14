#Hello everyone i have taken a challenge to master python language 

#in this i will be creating a python program that scans a folder and automatically sorts every file into folder based on its file extention , with any unknown file type moved into an other folder .

import os 
import pathlib as path

DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".txt", ".docx", ".pdf", ".xls"],
    "Archieves": [".zip", ".tar", ".rar"],
    "Others":[]
}

target_dir = path.Local Disk (C:)() / "Desktop" / "TestFolder"

for item in target_dir.iterdir():
    # iterdir is an built in tool which is used to list the content of directory 
    if item.is_der():
        continue

    file_ext = item.suffix.lower()

    for category , extentions in DIRECTORIES.items():
        if file_ext in extentions:

            category_path = target_dir / category
            category_path.mkdir(exists_ok=True)

            if file_ext != extentions:
                destination = target_dir / "Other"
                item.rename(destination)
                print(f"Moved {item.name} -> {category}")

            destination = target_dir / "Other"
            item.rename(destination)
            print(f"Moved {item.name} -> {category}")
            break

# PS C:\Python Final> python -u "c:\Python Final\python\task1.py"
# Traceback (most recent call last):
#   File "c:\Python Final\python\task1.py", line 15, in <module>
#     target_dir = path.home() / "Desktop" / "TestFolder"
# PS C:\Python Final> python -u "c:\Python Final\python\task1.py"
# Traceback (most recent call last):
#   File "c:\Python Final\python\task1.py", line 15, in <module>
#     target_dir = path.home() / "Desktop" / "TestFolder"
# AttributeError: module 'pathlib' has no attribute 'home'
# PS C:\Python Final> python -u "c:\Python Final\python\task1.py"
#   File "c:\Python Final\python\task1.py", line 15
#     target_dir = path.C:() / "Desktop" / "TestFolder"
#                        ^
# SyntaxError: invalid syntax
# PS C:\Python Final> python -u "c:\Python Final\python\task1.py"
# Traceback (most recent call last):
#   File "c:\Python Final\python\task1.py", line 15, in <module>
#     target_dir = path.C() / "Desktop" / "TestFolder"
# AttributeError: module 'pathlib' has no attribute 'C'
# PS C:\Python Final> python -u "c:\Python Final\python\task1.py"
#   File "c:\Python Final\python\task1.py", line 15
#     target_dir = path.Local Disk (C:)() / "Desktop" / "TestFolder"
#                             ^^^^
# SyntaxError: invalid syntax
# PS C:\Python Final> 