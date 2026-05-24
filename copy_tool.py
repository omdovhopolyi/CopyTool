import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import shutil
import os

class TkViewClass:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Directory and File Selector")

        # Directory 1 selection button and label
        self.button_from = tk.Button(self.root, text="Select from directory", command=self.select_directory_from)
        self.button_from.pack(pady=5)
        self.label_dir_from = tk.Label(self.root, text="Directory from: Not selected")
        self.label_dir_from.pack(pady=5)

        # Directory 2 selection button and label
        self.button_dir_to = tk.Button(self.root, text="Select to directory", command=self.select_directory_to)
        self.button_dir_to.pack(pady=5)
        self.label_dir_to = tk.Label(self.root, text="Directory to: Not selected")
        self.label_dir_to.pack(pady=5)

        # File selection button and label
        self.button_data_file = tk.Button(self.root, text="Select data file", command=self.select_data_file)
        self.button_data_file.pack(pady=5)
        self.label_data_file = tk.Label(self.root, text="Data File: Not selected")
        self.label_data_file.pack(pady=5)

        # Prefix
        self.prefix_label = tk.Label(self.root, text="Prefix")
        self.prefix_label.pack(pady=10)
        self.prefix_input = tk.Entry(self.root, width=20)
        self.prefix_input.pack(pady=10)

        # Extention
        self.extention_label = tk.Label(self.root, text="ext")
        self.extention_label.pack(pady=10)
        self.extention_input = tk.Entry(self.root, width=20)
        self.extention_input.pack(pady=10)

        self.button_copy = tk.Button(self.root, text="Copy", command=self.copy_files)
        self.button_copy.pack(pady=5)

        self.log_widget = tk.Text(self.root, height=10, width=100)
        self.log_widget.pack()

    def run(self):
        self.root.mainloop()

    def select_directory_from(self):
        dir_from = filedialog.askdirectory(title="Select From Directory")
        if dir_from:
            self.label_dir_from.config(text=f"{dir_from}")

    def select_directory_to(self):
        dir_to = filedialog.askdirectory(title="Select To Directory")
        if dir_to:
            self.label_dir_to.config(text=f"{dir_to}")

    def select_data_file(self):
        file_path = filedialog.askopenfilename(title="Select File")
        if file_path:
            self.label_data_file.config(text=f"{file_path}")

    def copy_files(self):
        source_file_path = self.label_data_file.cget("text")
        source_dir  = self.label_dir_from.cget("text")
        target_dir  = self.label_dir_to.cget("text")
        prefix = self.prefix_input.get()
        extention = self.extention_input.get()

        self.log_widget.insert("end", source_file_path + '\n')
        self.log_widget.insert("end", source_dir + '\n')
        self.log_widget.insert("end", target_dir + '\n')
        self.log_widget.insert("end", prefix + '\n')
        self.log_widget.insert("end", extention + '\n')

        with open(source_file_path) as infile:
            for line in infile:
                file_to_copy = source_dir + "/" + prefix + line.strip() + "." + extention
                if os.path.exists(file_to_copy):
                    result_file = target_dir + "/" + prefix + line.strip() + extention
                    self.log_widget.insert("end", "copying file: " + file_to_copy + '\n')
                    try:
                        shutil.copy(file_to_copy, result_file)
                    except:
                        self.log_widget.insert("end", "Error while copying: " + file_to_copy)
                else:
                    self.log_widget.insert("end", "File not found: " + file_to_copy)

def main():
    app = TkViewClass()
    app.run()
    # Initialize Tkinter window
    # root = tk.Tk()
    # root.title("Directory and File Selector")

    # Directory 1 selection button and label
    # button_from = tk.Button(root, text="Select from directory", command=select_directory_from)
    # button_from.pack(pady=5)
    # label_dir_from = tk.Label(root, text="Directory from: Not selected")
    # label_dir_from.pack(pady=5)

    # Directory 2 selection button and label
    # button_dir_to = tk.Button(root, text="Select to directory", command=select_directory_to)
    # button_dir_to.pack(pady=5)
    # label_dir_to = tk.Label(root, text="Directory to: Not selected")
    # label_dir_to.pack(pady=5)

    # File selection button and label
    # button_data_file = tk.Button(root, text="Select data file", command=select_data_file)
    # button_data_file.pack(pady=5)
    # label_data_file = tk.Label(root, text="Data File: Not selected")
    # label_data_file.pack(pady=5)

    # Prefix
    # prefix_label = tk.Label(root, text="Prefix")
    # prefix_label.pack(pady=10)
    # prefix_input = tk.Entry(root, width=20)
    # prefix_input.pack(pady=10)

    # Extention
    # extention_label = tk.Label(root, text="ext")
    # extention_label.pack(pady=10)
    # extention_input = tk.Entry(root, width=20)
    # extention_input.pack(pady=10)

    # button_copy = tk.Button(root, text="Copy", command=copy_files)
    # button_copy.pack(pady=5)

    # log_widget = tk.Text(root, height=10, width=100)
    # log_widget.pack()

    # root.mainloop()

if __name__ == "__main__":
    main()