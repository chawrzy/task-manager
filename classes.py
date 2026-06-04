import json
from datetime import datetime, timedelta


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load_tasks()

    def add_task(self, title, about,start_time, duration):

        if start_time is None or duration is None:
            print("❌ Invalid task data")
            return

        task = {
            "id": self.next_id,
            "title": title,
            "about": about ,
            "done": False,
            "start_time": start_time,
            "duration": duration,
            "status": "pending"
        }

        self.tasks.append(task)
        self.next_id += 1
        self.task_save()

    def checking_exist_task(self, id):
        for task in self.tasks:
            if task["id"] == id:
                return True
        return False

    def remove_task(self, id):
        self.tasks = [t for t in self.tasks if t["id"] != id]
        self.task_save()

    def mark_done(self, id):
        for task in self.tasks:
            if task["id"] == id:
                task["done"] = True
        self.task_save()

    def edit_task(self, id, title=None):
        for task in self.tasks:
            if task["id"] == id:

                if title:
                    task["title"] = title
                    print("The title has been change!")
                else:
                    task["done"] = not task["done"]
                    print("The task status has been changed!")

                break

        self.task_save()

    def show_task(self, id):
        for task in self.tasks:
            if task["id"] == id:
                check = "✅" if task["done"] else "❌"
                start = datetime.strptime(task["start_time"], "%Y-%m-%d %H:%M")
                end = start + timedelta(minutes=task["duration"])
                print("------------------------------")
                print(f"{task['id']} - {task['title']} - {check} - {task['start_time']} - {end}")
                print(task['about'])
                print("------------------------------")

    def show_all_tasks(self):
        return self.tasks

    def filter_task(self):
        print("\n❌ Not Done:")
        for task in self.tasks:
            if not task["done"]:
                print(f"{task['id']} - {task['title']}")

        print("\n✅ Done:")
        for task in self.tasks:
            if task["done"]:
                print(f"{task['id']} - {task['title']}")

    def task_save(self):
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def load_tasks(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                self.tasks = json.load(f)

                if self.tasks:
                    self.next_id = max(t["id"] for t in self.tasks) + 1

        except FileNotFoundError:
            self.tasks = []