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
                end = start + timedelta(minutes=task["duration"])
                if not task.get("started") and now >= start:
                    
                    messge = f" ---- TASK STARTED ----\n🚀 Task name : {task['title']}\n⏰ Time: {task['start_time'].split(" ")[-1]}\n ⏳ duration : {task['duration']} min"
                    send_message(messge)
                    task["started"] = True


                if not task.get("finished") and now >= end:
                    messge = " ---- TASK ENDED ---- "
                    send_message(messge)
                    task["finished"] = True
                    task['done'] = True

            except Exception as e:
                print("Error in task:", task, e)

        time.sleep(10)


scheduler()