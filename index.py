def display_menu():
    print("To-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def add_task(task_list):
    task = input("Enter the task: ")
    task_list.append({"task": task, "completed": False})
    print("Task added.")
def view_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(task_list, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['task']} - {status}")

def mark_completed(task_list):
    view_tasks(task_list)
    task_index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_index < len(task_list):
        task_list[task_index]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(task_list):
    view_tasks(task_list)
    task_index = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_index < len(task_list):
        del task_list[task_index]
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    task_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            mark_completed(task_list)
        elif choice == '4':
            delete_task(task_list)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()