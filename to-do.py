import tkinter as tk
from tkinter import messagebox

class TodoApp:

    def __init__(self, root):
        self.tasks = []

        # Title and window size
        root.title("To-Do App")
        root.geometry("400x400")

        # Entry widget and associated label
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=1, padx=20, pady=(20,0))
        self.task_label = tk.Label(root, text="Enter Task:")
        self.task_label.grid(row=0, column=0, padx=20, pady=(20,0))

        # Add button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=1, column=0, columnspan=2, pady=20)

        # Task list (Listbox widget)
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=20)

        # Complete and delete buttons
        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.grid(row=3, column=0, padx=20, pady=20)

        self.delete_button = tk.Button(root, text="Remove Completed", command=self.remove_completed)
        self.delete_button.grid(row=3, column=1, padx=20, pady=20)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Warning", "Please enter a task!")

    def mark_complete(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index] + " (Completed)"
            self.tasks[index] = task
            self.update_listbox()
        except:
            messagebox.showinfo("Warning", "Please select a task!")

    def remove_completed(self):
        self.tasks = [task for task in self.tasks if not task.endswith(" (Completed)")]
        self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

