import time
from datetime import datetime, timedelta
from notifier import send_message
from classes import TaskManager


def scheduler():
    last_report_date = None
    tm = TaskManager()
    while True:
        tm.load_tasks()
        now = datetime.now()

        print(f"Checking tasks... {now}")

        today_tasks = []

        for task in tm.tasks:
            try:
                if now.strftime("%Y-%m-%d") == task["start_time"].split(" ")[0]:
                    today_tasks.append(task)
            except KeyError:
                print("Task has no start_time:", task)

        # Daily report
        today = now.strftime("%Y-%m-%d")
        if now.strftime("%H:%M") == "15:00" and last_report_date != today:
            message = "---- TODAY TASKS ----\n\n"

            for task in today_tasks:
                message += (
                    f"☐ {task['title']} "
                    f"({task['start_time'].split(' ')[-1]})\n"
                )

            message += (
                f"\n---- {now.strftime('%Y-%m-%d')} ----"
            )
            send_message(message)
            last_report_date = today
        # Task reminders
        for task in today_tasks:

            try:
                start = datetime.strptime(
                    task["start_time"],
                    "%Y-%m-%d %H:%M"
                )

                end = start + timedelta(
                    minutes=task["duration"]
                )

                # Start notification
                if not task.get("started") and now >= start:

                    message = (
                        f"---- TASK STARTED ----\n\n"
                        f"🚀 Task name: {task['title']}\n"
                        f"📡 About task: {task.get('about', 'No description')}\n"
                        f"⏰ Time: {task['start_time'].split(' ')[-1]}\n"
                        f"⏳ Duration: {task['duration']} min"
                    )

                    send_message(message)

                    task["started"] = True
                    tm.task_save()

                # End notification
                if not task.get("finished") and now >= end:

                    message = (
                        f"---- TASK ENDED ----\n\n"
                        f"✅ Task name: {task['title']}\n"
                        f"🎉 Good job!"
                    )

                    send_message(message)

                    task["finished"] = True
                    task["done"] = True

                    tm.task_save()

            except Exception as e:
                print("Error in task:", task)
                print("Error:", e)

        time.sleep(10)


scheduler()