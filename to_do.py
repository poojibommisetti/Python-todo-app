
#define list to store tasks
tasks = []

#adding tasks and storing into lists   
def add_tasks():
    x = input("Enter task to add:")
    x_clean = x.strip()
    if x_clean:
        tasks.append(x_clean)
    else:
        print("Invalid input!..")
    print("Tasks are added successfully!...")

#view all tasks
def view_tasks():
    if not tasks :
        print("No tasks are available")
    else:
         for i in range(len(tasks)):
            print(i + 1,tasks[i])
    print("Tasks are displayed successfully!...")

#deleting task
def delete_tasks():
    if not tasks:
        print("No tasks are available for deletion!...")
        return
     
    view_tasks()

    num = int(input("Enter number u want to delete:"))

    if(1<= num <= len(tasks)):
        index = num - 1
        deleted_task = tasks.pop(index)
        print("Deleted tasks:", deleted_task)
    else:
        print("Enter valid number!") 

#updating tasks 
def update_tasks():
    if not tasks:
        print("No tasks are available to update!...")
        return
    
    view_tasks()

    num = int(input("Enter number u want to update:"))

    if(1<= num <= len(tasks)):
        index = num - 1
    else:
        print("Enter valid number!...")
        return

    new_task = input("Enter new task:")
    new_task_clean = new_task.strip()

    if new_task_clean:
        tasks[index] = new_task_clean
        print("Task updated successfully!...")

    else:
        print("Invalid input!...")
    

# menu list

while True:
    print("1.add task")
    print("2.view tasks")
    print("3.delete task")
    print("4.update tasks")
    print("5.Exit")

    choice = input("Enter option you want to perform:")

    if choice == "1":
        add_tasks()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_tasks()
    elif choice == "4":
        update_tasks()
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid Option")

 

    


