from classes import TaskManager
from datetime import datetime, timedelta

tm = TaskManager()

print("--- welcome to task manager ---")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")


def get_time():
    while True:
        time_input = input("Time (HH:MM): ")
        try:
            datetime.strptime(time_input, "%H:%M")
            return time_input
        except ValueError:
            print("❌ Invalid time format! Use HH:MM")


while True:
    print("""
How can I help you?
[1] Add task
[2] Remove task
[3] Edit task
[4] Show task
[5] Filter tasks
[6] Show all tasks
[7] Save tasks
[8] Exit
""")

    user = get_int("Enter number: ")

    match user:

        case 1:
            today = datetime.now().strftime("%Y-%m-%d")
            tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

            title = input("Title: ")
            about = input("About: ")

            print(f"""
[1] Today ({today})
[2] Tomorrow ({tomorrow})
[3] Custom date
""")

            user_time = get_int("Choose date option: ")

            if user_time == 1:
                dateTask = today
                timeTask = get_time()

            elif user_time == 2:
                dateTask = tomorrow
                timeTask = get_time()

            elif user_time == 3:
                while True:
                    try:
                        dateTask = input("Date (YYYY-MM-DD): ")
                        timeTask = get_time()
                        datetime.strptime(dateTask, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("❌ Invalid date format!")

            else:
                print("❌ Invalid option")
                continue

            date_time_task = f"{dateTask} {timeTask}"

            while True:
                try:
                    duration = int(input("Duration (minutes): "))
                    if duration <= 0:
                        print("❌ Must be greater than 0")
                        continue
                    break
                except ValueError:
                    print("❌ Enter a valid number")

            tm.add_task(title, about, date_time_task, duration)
            print("✅ Task added!")

        case 2:
            task_id = get_int("Task ID: ")
            if tm.checking_exist_task(task_id):
                tm.remove_task(task_id)
                print("✅ Task removed")
            else:
                print("❌ Task not found")

        case 3:
            task_id = get_int("Task ID: ")

            if tm.checking_exist_task(task_id):
                tm.show_task(task_id)

                print("""
[1] Change title
[2] Toggle done/undone
""")

                choice = get_int("Choose: ")

                if choice == 1:
                    new_title = input("New title: ")
                    tm.edit_task(task_id, new_title)

                elif choice == 2:
                    tm.edit_task(task_id)

                else:
                    print("❌ Invalid choice")

            else:
                print("❌ Task not found")

        case 4:
            task_id = get_int("Task ID: ")
            if not tm.show_task(task_id):
                print("❌ Task not found")

        case 5:
            tm.filter_task()

        case 6:
            tasks = tm.show_all_tasks()

            if not tasks:
                print("No tasks found")
                continue

            for task in tasks:
                tm.print_task(task)

        case 7:
            tm.save_tasks()
            print("✅ Saved!")

        case 8:
            print("Goodbye 👋")
            break

    print("-" * 40)