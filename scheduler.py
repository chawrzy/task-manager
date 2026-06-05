import time
from datetime import datetime, timedelta
from notifier import send_message
from classes import TaskManager


def scheduler():
    tm = TaskManager()

    while True:
        now = datetime.now()

        for task in tm.tasks:   

            try:
                start = datetime.strptime(task["start_time"], "%Y-%m-%d %H:%M")

                if not task.get("started") and now >= start:
                    send_message(f"🚀 Task Started: {task['title']}")
                    task["started"] = True

                end = start + timedelta(minutes=task["duration"])

                if not task.get("finished") and now >= end:
                    send_message(f"✅ END: {task['title']}")
                    task["finished"] = True
                    task['done'] = "✅"

            except Exception as e:
                print("Error in task:", task, e)

        time.sleep(10)


scheduler()