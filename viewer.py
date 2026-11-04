import os
DATA_DIR = "Data Proxima - Copy"    #اسم ال folder اللي خزنت فيه الصور بتاعت NASA

print("=== Processing Dataset Files ===")
if os.path.exists(DATA_DIR):
    for folder_name in os.listdir(DATA_DIR):
        folder_path = os.path.join(DATA_DIR, folder_name)
        if os.path.isdir(folder_path):
            print(f"\n[+] Object Folder: {folder_name}")
            for file_name in os.listdir(folder_path):
                print(f" - Found file: {file_name}")
else:
    print(f"Directory {DATA_DIR} not found! Check folder name in PyCharm.")     

