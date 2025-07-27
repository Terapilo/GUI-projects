import tkinter as tk
from tkinter import messagebox
from datetime import datetime

#Create functions

FILENAME = "notes.txt"

def save_note():
    note = text_input.get("1.0", tk.END).strip()
    if note == "":
        messagebox.showwarning("Empty Note", "Please write something before saving.")
        return
    timestamp=datetime.now().strftime("%d-%m-%Y")
    with open (FILENAME, "a") as f:
        f.write(f"[{timestamp}] {note}")
    messagebox.showinfo("Saved", "Note saved successfully.")
    text_input.delete("1.0", tk.END)

def view_note():
    try:
        with open (FILENAME, )as f:
            note=f.read()
            if note == "":
                notes = "No notes saved yet."
    except FileNotFoundError:
        notes = "File not found."   
    messagebox.showinfo("Your notes", notes)   

def clear_note():
    confirm = messagebox.askyesno("Are you sure you want to delete notes?")
    if confirm:
        open(FILENAME, "w").close()
    messagebox.showinfo("Deleted.", "All notes have been cleared.")

#GUI setup
window = tk.Tk()
window.title="Notes app"
window.geometry("400x400")
window.resizable(False, False)

label_title=tk.Label(window, text="Write your note below", font=("Arial", 12))
label_title.pack(pady=5)

text_input=tk.Text(window, height=10, width=40, font=("Arial", 12))
text_input.pack(pady=10)

btn_save = tk.Button(window, text="Save note", command=save_note, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_save.pack(pady=5)

btn_view = tk.Button(window, text="View all notes", command=view_note, font=("Arial", 12), bg="#2196F3", fg="white")
btn_view.pack(pady=5)

btn_clear = tk.Button(window, text="Clear all notes", command=clear_note, font=("Arial", 12), bg="#FF0000", fg="white")
btn_clear.pack(pady=5)

window.mainloop()