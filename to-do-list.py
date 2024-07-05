import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

def add_task():
    title = entry_title.get()
    description = text_description.get("1.0", tk.END)
    task = Task(title, description)
    tasks.append(task)
    update_task_list()

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task.title)
    listbox_tasks.bind("<ButtonRelease-1>", show_task_description)  # Bind click event

def show_task_description(event=None):
    try:
        index = listbox_tasks.curselection()[0]
        task = tasks[index]
        text_description.delete("1.0", tk.END)  # Clear previous content
        text_description.insert(tk.END, task.description)
    except IndexError:
        text_description.delete("1.0", tk.END)  # Clear description if no task is selected

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
        tasks.pop(index)
        text_description.delete("1.0", tk.END)  # Clear description after deletion
    except IndexError:
        messagebox.showwarning("Delete Task", "Please select a task to delete.")

# Create the main application window
root = tk.Tk()
root.title("To-Do List Application")

# Task list and GUI elements
tasks = []

label_title = tk.Label(root, text="Title")
label_title.pack()

entry_title = tk.Entry(root, width=50)
entry_title.pack()

label_description = tk.Label(root, text="Description")
label_description.pack()

text_description = tk.Text(root, height=5, width=50)
text_description.pack()

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack()

listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.pack()

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack()

# Start the main loop
root.mainloop()
