class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, task_index):
        try:
            del self.tasks[task_index]
        except IndexError:
            print("Task index out of range.")

    def mark_completed(self, task_index):
        try:
            self.tasks[task_index]["completed"] = True
        except IndexError:
            print("Task index out of range.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index + 1}. {task['task']} - {status}")


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == "2":
            task_index = int(input("Enter the task index to delete: ")) - 1
            todo_list.delete_task(task_index)
            print("Task deleted successfully!")
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            todo_list.mark_completed(task_index)
            print("Task marked as completed!")
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
