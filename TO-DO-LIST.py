tasks = []

while True:
    print("\nTo-Do List Menu:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        if not tasks:
            print("No tasks available.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    elif choice == '2':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
