import tkinter as tk
from tkinter import filedialog
import subprocess


def import_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        print("Selected file:", file_path)
        if file_path.endswith("07llr_book_2024.pdf"):
            print("File is a PDF")
            # If the specific PDF file is selected, execute main_romana.py
            subprocess.run([r"C:\Users\Radu\PycharmProjects\pythonProject\venv\Scripts\python.exe", "main_romana.py"], check=True)

# Create the main Tkinter window
root = tk.Tk()
root.title("Import File Example")

# Set the window size
window_width = 400
window_height = 300

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center position
center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# Set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Create an "Import File" button
import_button = tk.Button(root, text="Import File", command=import_file)
import_button.pack(pady=100)

# Run the Tkinter event loop
root.mainloop()
