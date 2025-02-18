import tkinter as tk
from tkinter import messagebox


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Set the background color of the window to black
        self.root.configure(bg='black')

        # Set up the UI components
        self.task_entry = tk.Entry(self.root, width=30, bg='white', fg='black')
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task, bg='yellow')
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.update_button = tk.Button(self.root, text="Update Task", width=20, command=self.update_task, bg='lightblue')
        self.update_button.grid(row=1, column=1, padx=10, pady=10)

        self.remove_button = tk.Button(self.root, text="Remove Task", width=20, command=self.remove_task, bg='red')
        self.remove_button.grid(row=2, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=40, height=10, bg='gray', fg='white', font=("Arial", 12))
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, rowspan=2)

        self.show_tasks()

        

    def add_task(self):
        """Adds a new task and updates the listbox."""
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.show_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task(self):
        """Updates a selected task."""
        try:
            selected_task_index = self.task_listbox.curselection()[0] // 2  # Adjust for separator lines
            new_task = self.task_entry.get()

            if new_task:
                self.tasks[selected_task_index] = new_task
                self.task_entry.delete(0, tk.END)
                self.show_tasks()
            else:
                messagebox.showwarning("Input Error", "Please enter the updated task.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def remove_task(self):
        """Removes the selected task and its separator line."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            actual_task_index = selected_index // 2  # Adjust because of separators

            if 0 <= actual_task_index < len(self.tasks):
                del self.tasks[actual_task_index]
                self.show_tasks()
            else:
                messagebox.showwarning("Selection Error", "Please select a valid task.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def show_tasks(self):
        """Updates the task list display with serial numbers and borders."""
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")
            self.task_listbox.insert(tk.END, "------------------------")  # Border separator

# Setting up the main window
root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
