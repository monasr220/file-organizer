
📁 File Organizer with Undo (Python + Tkinter)

A simple desktop application built with Python and Tkinter that organizes your files into categorized folders (images, videos, documents, etc.) and supports undo functionality to restore the files to their original locations.

✅ Features

- Automatically organizes files by type into folders
- Undo operation to restore files back
- Simple and user-friendly GUI using Tkinter
- Safe: skips system files and logs all moved files
- One-click usage – ideal for cleaning your Downloads folder

🚀 How to Use

1. Run the App
   python file_organizer.py

2. In the GUI:
   - Click "Organize Files" and choose a folder (e.g., Downloads)
   - The app will create folders based on file types and move files
   - A log file undo_log.txt will be created automatically

3. To Undo:
   - Click "Undo Organization"
   - Select the same folder (it must contain undo_log.txt)
   - Files will be restored to their original locations

🛠️ Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- No external libraries needed

📦 Packaging (Optional)

To convert the script into an executable .exe:
   pip install pyinstaller
   pyinstaller --onefile --noconsole file_organizer.py

The .exe will be found in the dist/ folder.

📁 Folder Structure

file-organizer/
|
├── file_organizer.py      # Main application script
├── README.txt             # Project documentation
├── .gitignore             # (optional)
└── dist/                  # (optional EXE if you build it)

📄 License

This project is open source and free to use for any purpose.

👤 Author

Made with ❤️ by Mohamed
