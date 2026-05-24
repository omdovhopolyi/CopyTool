import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import shutil
import os

class TkViewClass:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Directory and File Selector")

        self.top = tk.Frame(self.root)
        self.top.pack(side="top", fill="both", expand=True)

        self.left = tk.Frame(self.top)
        self.left.pack(side="left", fill="both", expand=True)

        # Directory 1 selection button and label
        self.button_from = tk.Button(self.left, text="Select from directory", command=self.select_directory_from)
        self.button_from.pack(pady=5, anchor="w")
        self.label_dir_from = tk.Label(self.left, text="Directory from: Not selected")
        self.label_dir_from.pack(pady=5, anchor="w")

        # Directory 2 selection button and label
        self.button_dir_to = tk.Button(self.left, text="Select to directory", command=self.select_directory_to)
        self.button_dir_to.pack(pady=5, anchor="w")
        self.label_dir_to = tk.Label(self.left, text="Directory to: Not selected")
        self.label_dir_to.pack(pady=5, anchor="w")

        # Prefix
        self.prefix_label = tk.Label(self.left, text="Prefix")
        self.prefix_label.pack(pady=10, anchor="w")
        self.prefix_input = tk.Entry(self.left, width=20)
        self.prefix_input.pack(pady=10, anchor="w")
        self.prefix_input.insert(0, "IMG_")

        # Extention
        self.extention_label = tk.Label(self.left, text="ext")
        self.extention_label.pack(pady=10, anchor="w")
        self.extention_input = tk.Entry(self.left, width=20)
        self.extention_input.pack(pady=10, anchor="w")
        self.extention_input.insert(0, "CR3")

        self.button_copy = tk.Button(self.left, text="Copy", command=self.copy_files)
        self.button_copy.pack(pady=5, anchor="w")

        self.right = tk.Frame(self.top, height=10, width=10)
        self.right.pack(side="right", fill="both", expand=True)

        self.text_box_label = tk.Label(self.right, text="Data")
        self.text_box_label.pack(anchor="n")

        self.text_box = tk.Text(self.right)
        self.text_box.pack(padx=10, pady=10, anchor="e")

        self.bottom = tk.Frame(self.root)
        self.bottom.pack(side="bottom", fill="both", expand=True)

        self.log_widgen_label = tk.Label(self.bottom, text="Log")
        self.log_widgen_label.pack(anchor="n")

        self.log_widget = tk.Text(self.bottom, height=10, width=100, bg="gray")
        self.log_widget.pack(padx=10, pady=10)
        self.log_widget.tag_config("red_line", foreground="red")
        self.log_widget.config(state="disabled")

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
        source_dir  = self.label_dir_from.cget("text")
        target_dir  = self.label_dir_to.cget("text")
        prefix = self.prefix_input.get()
        extention = self.extention_input.get()

        raw_text = self.text_box.get("1.0", tk.END)
        lines = raw_text.strip().split("\n")

        self.log_widget.insert("end", source_dir + '\n')
        self.log_widget.insert("end", target_dir + '\n')
        self.log_widget.insert("end", prefix + '\n')
        self.log_widget.insert("end", extention + '\n')

        self.log_widget.config(state="normal")
        #with open(source_file_path) as infile:
        for line in lines:
            file_to_copy = source_dir + "/" + prefix + line.strip() + "." + extention
            if os.path.exists(file_to_copy):
                result_file = target_dir + "/" + prefix + line.strip() + "." + extention
                self.log_widget.insert("end", "copying file: " + file_to_copy + '\n')
                try:
                    shutil.copy(file_to_copy, result_file)
                except:
                    self.log_widget.insert("end", "Error while copying: " + file_to_copy + '\n', "red_line")
            else:
                self.log_widget.insert("end", "File not found: " + file_to_copy + '\n', "red_line")
        self.log_widget.config(state="disabled")

def main():
    app = TkViewClass()
    app.run()

if __name__ == "__main__":
    main()