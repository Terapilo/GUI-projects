import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import json

FILENAME = "passwords.json"

#---------------------------------------functions------------------------------------------------------------
def save_password():
    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if not website or not username or not password:
        messagebox.showwarning("Missing info", "Please fill in all fields")
        return
    data = {
        website : {
            "username" : username, 
            "password" : password,
            "saved_at" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }
    try:
        with open (FILENAME, "r") as file:
            file_data = json.load(file)
    except  (FileNotFoundError, json.JSONDecodeError):
        file_data={}

    file_data.update(data)

    try:
        with open (FILENAME, "w") as file:
            json.dump(file_data, file, indent=4)
        messagebox.showinfo("Saved!", f"Credentials for {website} saved successfully.")
        website_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error","Could not save data" )

def view_all_passwords():
    try:
        with open (FILENAME, "r") as file:
            data = json.load(file)
        
        if not data:
            messagebox.showinfo("Passwords", "No passwords stored yet." )
            return
        output = ""
        for site, creds in data.items():
            output += f"\n🔐 {site}\nUsername: {creds['username']}\nPassword: {creds['password']}\nSaved at: {creds['saved_at']}\n"

        messagebox.showinfo("Stored Credentials", output)
    except FileNotFoundError:
        messagebox.showerror("Not found.", "Password storage file does not exist yet.")
    except Exception as e:
        messagebox.showerror("Error.", "Could not read file.")

#----------------------------------------GUI setup------------------------------------------------------------------
window = tk.Tk()
window.title("Password manager")
window.geometry("400x300")
window.configure(bg="#f8f8f8")

# ---------------------------------------Labek and entries--------------------------------------------------------
tk.Label(window, text="Website", font=("Arial", 11), bg="#f8f8f8").pack(pady=(10, 0) )
website_entry =tk.Entry(window, font=("Arial", 12))
website_entry.pack(pady=5)

tk.Label(window, text="Username", font=("Arial", 11), bg="#f8f8f8").pack(pady=(10, 0) )
username_entry =tk.Entry(window, font=("Arial", 12))
username_entry.pack(pady=5)

tk.Label(window, text="Password", font=("Arial", 11), bg="#f8f8f8").pack(pady=(10, 0) )
password_entry =tk.Entry(window, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

#Buttons
save_button = tk.Button(window, text="Save", font=("Arial", 11), bg="#4CAF50", fg="white",
                        command=save_password).pack(pady=5)

view_button = tk.Button(window, text="View All", font=("Arial", 11), bg="#4CAF50", fg="white",
                        command=view_all_passwords).pack()
window.mainloop()