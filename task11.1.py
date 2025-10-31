import tkinter as tk
from tkinter import messagebox
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()
    if name == "" or age == "" or course == "":
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}\nCourse: {course}")
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("350x250")
tk.Label(root, text="Student Registration", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack()
tk.Label(root, text="Age:").pack()
entry_age = tk.Entry(root, width=30)
entry_age.pack()
tk.Label(root, text="Course:").pack()
entry_course = tk.Entry(root, width=30)
entry_course.pack()
tk.Button(root, text="Submit", command=submit_form, bg="blue", fg="white").pack(pady=15)
root.mainloop()
