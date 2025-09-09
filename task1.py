tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet ")
    else:
        for i, t in enumerate(tasks, 1):
            status = " Done" if t[1] else " Pending"
            print(f"{i}. {t[0]} [{status}]")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append([task, False])
        print("Task added ")

    elif choice == "3":
        show_tasks()
        try:
            n = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter updated task: ")
            tasks[n][0] = new_task
            print("Task updated ")
        except:
            print("Invalid choice ")

    elif choice == "4":
        show_tasks()
        try:
            n = int(input("Enter task number to mark done: ")) - 1
            tasks[n][1] = True
            print("Task marked as completed ")
        except:
            print("Invalid choice ")

    elif choice == "5":
        show_tasks()
        try:
            n = int(input("Enter task number to delete: ")) - 1
            removed = tasks.pop(n)
            print(f"Deleted: {removed[0]} ")
        except:
            print("Invalid choice ")

    elif choice == "6":
        print("Exiting... Bye ")
        break

    else:
        print("Invalid option ")
