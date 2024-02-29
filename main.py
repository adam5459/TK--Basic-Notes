import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
import os


current_folder = ""
current_filename = 'Untitled'


def update_title():
    title_label.config(text=f"Current Folder {current_folder} | Current File Name {current_filename} ")


def save_note():
    global current_folder, current_filename
    current_filename = simpledialog.askstring("Save as", "Enter File Name: ", parent=root)
    if current_filename:
        folder_path = os.path.join("notes", current_folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(os.path.join(folder_path, current_filename+'.txt'), 'w') as file:
            note_text = text.get("1.0", tk.END)
            file.write(note_text)
            update_title()

def load_note():
    global current_folder, current_filename

    folder_path = filedialog.askdirectory()

    if folder_path:
        current_folder = os.path.basename(folder_path)
        file_path = filedialog.askopenfilename(initialdir=folder_path, title="Select File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                note_text = file.read()
                text.delete("1.0", tk.END)
                text.insert(tk.END, note_text)
                update_title()

def clear_note():
    global current_folder, current_filename
    
    folder_path = filedialog.askdirectory()
    if folder_path:
        current_folder = os.path.basename(folder_path)
        file_path = filedialog.askopenfilename(initialdir=folder_path, title="Select File", filetypes=[("Text files", "*.txt")])
        if file_path:
            current_filename = os.path.basename(file_path)[:-4]
            confirmation = messagebox.askyesno("Clear Note", f"Are you sure you want to clear the note {current_filename}? ")
            if confirmation:
                with open(file_path, 'w') as file:
                    file.write("")
                text.delete("1.0", tk.END)
                messagebox.showinfo("Note Cleared", "The Note has been cleared")

def delete_note():
    global current_folder, current_filename

    folder_path = filedialog.askdirectory()
    if folder_path:
        current_folder = os.path.basename(folder_path)
        file_path = filedialog.askopenfilename(initialdir=folder_path, title="Select File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            current_filename = os.path.basename(file_path)[:-4]
            confirmation = messagebox.askyesno("Delete File", f"Would you like to delete {current_filename}? ")
            if confirmation:
                os.remove(file_path)
                messagebox.showinfo("File Deleted", "File has been deleted")
    update_title()


    update_title()
root = tk.Tk()


root.title("Notes")

title_frame = tk.Frame(root)
title_frame.pack(fill=tk.X)

title_label = tk.Label(title_frame, text=f"Current Folder {current_folder} | Current File Name {current_filename}", anchor='w')
title_label.pack(fill=tk.X)

text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X)

save_button = tk.Button(button_frame, text="Save", command=save_note)
save_button.pack(side=tk.LEFT)


load_button = tk.Button(button_frame, text="Load", command=load_note)
load_button.pack(side=tk.LEFT)

clear_button = tk.Button(button_frame, text="Clear", command=clear_note)
clear_button.pack(side=tk.LEFT)

del_button = tk.Button(button_frame, text="Delete", command=delete_note)
del_button.pack(side=tk.LEFT)

root.mainloop()

