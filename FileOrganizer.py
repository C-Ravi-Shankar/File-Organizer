#Level-3 Task-3 "Automating File Organization"

import os
import shutil
from pathlib import Path

file_categories = {
    "Images":['.jpeg','.png','.jpg','.gif','.svg'],
    "documents":['.doc','.docx','.xls','.xlsx','.ppt','.pptx','.txt'],
    "Videos":['.mp4','.mov','.mkv'],
    "Audio":['.mp3','.wav','.flac'],
    "Source codes":['.py','.js','.java','.c','.cpp','.html','.css','.'],
    "Archieves" : ['.rar','.zip']
}
#we can add extra files in the categories as our requirement

def organize_files(Directory):
    print(f"Organizing File in {Directory}")

    for category in file_categories:
        (Directory/category).mkdir(exist_ok = True)
    
    files_moved = []

    for file_path in Directory.iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()
            moved = False
        
            for category,file_extensions in file_categories.items():
                if extension in file_extensions:
                    destination_folder = Directory/category 
                    shutil.move(str(file_path),str(destination_folder/file_path.name))
                    files_moved.append((file_path.name,category))
                    moved = True
                    break
           
            if not moved:
                other_folder = Directory/"others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file_path),str(other_folder/file_path.name))
                files_moved.append((file_path.name,'others'))
    print()
    print("Files organized Succesfully...")
    print()
    for files,category in files_moved:
        print(f"Moved {files} -> {category}")

print("----------------File Organizer----------------")
print()
given_directory = input("Enter the path of folder that you want to organize atomatically:")
directory_path= Path(given_directory).expanduser()

if directory_path.exists():
    organize_files(directory_path)
else:
    print(f"{given_directory} does not exists")