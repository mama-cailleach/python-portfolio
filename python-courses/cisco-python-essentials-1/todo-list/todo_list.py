def display_menu():
    print("\nTodo List Menu:")
    print("1. Add task")
    print("2. List all tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("Task added!")
    else:
        print("Task cannot be empty.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        for idx, t in enumerate(tasks, 1):
            status = "Done" if t["done"] else "Todo"
            print(f"{idx}. [{status}] {t['task']}")

def mark_task_done(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Task '{removed['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
