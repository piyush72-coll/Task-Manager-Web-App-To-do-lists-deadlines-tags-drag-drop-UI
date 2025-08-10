# Simple Task Manager in Python

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"✅ Task added: {task}")

def show_tasks():
    if not tasks:
        print("📋 No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"🗑️ Task removed: {removed}")
    else:
        print("❌ Invalid task number.")

while True:
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            delete_task(num)
        except ValueError:
            print("❌ Please enter a valid number.")
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
