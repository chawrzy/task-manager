from classes import TaskManager
tm = TaskManager()
print("--- wellcome to task manager ----")
while True:
    print("How can i help you?")
    print("[1] adding a new task\n[2] removing a task\n[3] edit the task\n[4] search in tasks\n[5] filter done / not done\n[6] show all the tasks\n[7] save the tasks\n[8] Exit")
    try:
        user = int(input("Enter the number: "))
    except ValueError:
        print("Please enter a number!")
        continue
    match user:
        case 1:
            tm.add_task(input("Enter the title of your task: "))
            print("your task has been added!")
        
        case 2:
            task_id = int(input("Enter the Id of the task: "))  
            if tm.checking_exist_task(task_id):
                tm.remove_task(task_id)
                print(f"the task with id {task_id} has been removed!")
            else :
                print(f"this task with id {task_id} is no exist!")
        
        case 3:
            task_id = int(input("Enter the task id: "))
            if tm.checking_exist_task(task_id):
                tm.show_task(task_id)
                print("what do you want to change?\n[1] title\n[2] check / uncheck")
                user_change = int(input("Enter the number: "))
                if user_change == 1:
                    tm.edit_task(task_id , input("Enter the a new title: "))
                elif user_change == 2 :
                    tm.edit_task(task_id)
                else :
                    print("Invalid input!")
            else :
                print(f"There is no task exits with id {task_id}")

        case 4:
            task_id = int(input("Enter the task id: "))
            if tm.checking_exist_task(task_id):
                tm.show_task(task_id)
            else :
                print(f"There is no task exits with id {task_id}")
        
        case 5:
            tm.filter_task()
        
        case 6:
            tm.show_all_tasks()

        case 7:
            tm.task_save()
            print("the tasks has been saved!")
        case 8:
            break
    print("---------------------")    
        