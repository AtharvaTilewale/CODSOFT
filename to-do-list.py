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

def show_task_details():
    try:
        index = listbox_tasks.curselection()[0]
        task = tasks[index]
        
        # Create a new window for task details
        details_window = tk.Toplevel(root)
        details_window.title("Task Details")
        
        # Display task title
        label_title_details = tk.Label(details_window, text=f"Title: {task.title}")
        label_title_details.pack()
        
        # Display task description
        label_description_details = tk.Label(details_window, text=f"Description:")
        label_description_details.pack()
        
        text_description_details = tk.Text(details_window, height=5, width=50)
        text_description_details.insert(tk.END, task.description)
        text_description_details.pack()
        
        # Button to delete the task
        button_delete_task_details = tk.Button(details_window, text="Delete Task", command=lambda: delete_task_from_details(index, details_window))
        button_delete_task_details.pack()
        
    except IndexError:
        messagebox.showwarning("Task Details", "Please select a task to view details.")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
        tasks.pop(index)
    except IndexError:
        messagebox.showwarning("Delete Task", "Please select a task to delete.")

def delete_task_from_details(index, details_window):
    listbox_tasks.delete(index)
    tasks.pop(index)
    details_window.destroy()
    update_task_list()

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

button_show_details = tk.Button(root, text="Show Details", command=show_task_details)
button_show_details.pack()

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack()

# Start the main loop
root.mainloop()
