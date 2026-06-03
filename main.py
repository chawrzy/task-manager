from classes import TaskManager
tm = TaskManager()
print("--- wellcome to task manager ----")
while True:
    print("How can i help you?")
    print("[1] adding a new task\n[2] removing a task\n[3] check the task\n[4] show all the tasks\n[5] save the tasks\n[6] Exit")
    user = int(input("Enter the number: "))
    match user:
        case 1:
            tm.add_task(input("Enter the title of your task: "))
            print("your task has been added!")
        case 2:
            task_remove = int(input("Enter the Id of the task: "))  
            if tm.checking_exist_task(task_remove):
                tm.remove_task(task_remove)
                print(f"the task with id {task_remove} has been removed!")
            else :
                print(f"this task with id {task_remove} is no exist!")
        case 3:
            task_check = int(input("Enter the Id of the task: "))  
            if tm.checking_exist_task(task_check):
                tm.mark_done(task_check)
                print(f"the task with id {task_check} has been marked!")
            else :
                print(f"this task with id {task_check} is now exist!")
        case 4:
            tm.task_shows()
        case 5:
            tm.task_save()
            print("the tasks has been saved!")
        case 6:
            break
    print("---------------------")    
        