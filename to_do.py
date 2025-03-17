import sys

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def list_tasks():
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks found.")

def remove_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Removed: {removed}")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("\nOptions: add, list, remove, exit")
        choice = input("Enter command: ").strip().lower()

        if choice == "add":
            task = input("Enter task: ").strip()
            add_task(task)
        elif choice == "list":
            list_tasks()
        elif choice == "remove":
            list_tasks()
            try:
                index = int(input("Enter task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "exit":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
