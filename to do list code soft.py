import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=20)

        self.entry_task = tk.Entry(self.root, width=50)
        self.entry_task.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            pass

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = ToDoListApp(root)
    root.mainloop()