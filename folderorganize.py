import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File type categories
categories = {
    'images': ['jpg', 'jpeg', 'png', 'gif'],
    'documents': ['pdf', 'doc', 'docx', 'txt'],
    'videos': ['mp4', 'mov', 'avi'],
    'music': ['mp3', 'wav'],
    'archives': ['zip', 'rar', '7z', 'tar', 'gz'],
    'executables': ['exe', 'msi'],
    'scripts': ['py', 'js', 'sh', 'bat'],
    'spreadsheets': ['xls', 'xlsx', 'csv'],
    'presentations': ['ppt', 'pptx'],
    'fonts': ['ttf', 'otf'],
    'databases': ['db', 'sql'],
    'code': ['html', 'css', 'js', 'java', 'c', 'cpp'],
    'designs': ['psd', 'ai', 'xd'],
    'logs': ['log'],
    'backup': ['bak', 'tmp', 'temp'],
    'configurations': ['ini', 'cfg', 'conf'],
    'ebooks': ['epub', 'mobi'],
    'images_raw': ['raw', 'nef', 'cr2'],
    '3d_models': ['obj', 'fbx', 'stl'],
    'virtual_machines': ['vmdk', 'vdi'],
    'system_files': ['dll', 'sys'],
    'certificates': ['crt', 'pem'],
    'security': ['pfx', 'key'],
    'web_pages': ['html', 'htm'],
    'others': []
}

# Detect category from file extension
def get_category(file_ext):
    for category, extensions in categories.items():
        if file_ext.lower() in extensions:
            return category
    return 'others'

# Organize files
def organize_files():
    folder = filedialog.askdirectory(title="Select folder to organize")
    if not folder:
        return

    undo_log = os.path.join(folder, "undo_log.txt")
    moved_files = 0

    try:
        with open(undo_log, 'w', encoding='utf-8') as log_file:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)

                if os.path.isfile(file_path) and filename != 'undo_log.txt':
                    file_ext = os.path.splitext(filename)[1][1:]
                    category = get_category(file_ext)
                    category_folder = os.path.join(folder, category)

                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)

                    new_path = os.path.join(category_folder, filename)
                    shutil.move(file_path, new_path)
                    log_file.write(f"{new_path}|{file_path}\n")
                    moved_files += 1

        messagebox.showinfo("Done", f"✅ Organized {moved_files} files and saved undo log.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Undo organization
def undo_organization():
    folder = filedialog.askdirectory(title="Select folder that contains undo_log.txt")
    if not folder:
        return

    undo_log = os.path.join(folder, "undo_log.txt")

    if not os.path.exists(undo_log):
        messagebox.showwarning("Not Found", "❌ undo_log.txt not found.")
        return

    restored = 0
    try:
        with open(undo_log, 'r', encoding='utf-8') as log_file:
            lines = log_file.readlines()

        for line in lines:
            moved_path, original_path = line.strip().split('|')
            if os.path.exists(moved_path):
                shutil.move(moved_path, original_path)
                restored += 1

        # Delete empty folders and undo log
        for folder_name in os.listdir(folder):
            folder_path = os.path.join(folder, folder_name)
            if os.path.isdir(folder_path) and not os.listdir(folder_path):
                os.rmdir(folder_path)

        os.remove(undo_log)
        messagebox.showinfo("Undo Completed", f"✅ Restored {restored} files to original locations.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("📁 File Organizer with Undo - By Mohamed")
root.geometry("400x250")
root.resizable(False, False)

label = tk.Label(root, text="Choose an action:", font=("Arial", 14))
label.pack(pady=20)

btn1 = tk.Button(root, text="📂 Organize Files", font=("Arial", 12), command=organize_files, width=30)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="🔄 Undo Organization", font=("Arial", 12), command=undo_organization, width=30)
btn2.pack(pady=10)

root.mainloop()
