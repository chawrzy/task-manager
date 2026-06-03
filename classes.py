import json
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load_tasks()

    def add_task(self, title):
        task = {
            "id": self.next_id,
            "title": title,
            "done": False
        }
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
     
    def checking_exist_task(self, id):
        for task in self.tasks:
            if task["id"] == id:
                return True
        return False

    def remove_task(self, id):
        self.tasks = [t for t in self.tasks if t["id"] != id]
        self.save_tasks()
    
    def mark_done(self , id):
        for task in self.tasks:
            if task["id"] == id:
                task["done"] = True
        self.save_tasks()
    
    def task_shows(self):
        for task in self.tasks:
            check = "✅" if task["done"] else "❌"
            print(f"{task['id']} - {task['title']} - {check}")

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


