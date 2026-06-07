# 🧠 Task Manager (Python CLI + Telegram Bot)

A powerful command-line Task Manager built with Python, featuring task scheduling, persistence with JSON, and Telegram notifications.

This project is designed as a real-world productivity tool with OOP structure and automation features.

---

## 🚀 Features

### 📋 Task Management
- ➕ Add tasks with title, description, date & time  
- ❌ Remove tasks by ID  
- ✏️ Edit task title or toggle status  
- 🔍 View single task details  
- 📑 View all tasks  
- 📂 Filter tasks (done / not done)

### 💾 Data Persistence
- Auto-save tasks to `tasks.json`  
- Auto-load tasks on startup  
- Stable ID system for tasks  

### ⏰ Scheduler System
- Background task scheduler  
- Start and end time tracking  
- Automatic notifications when:
  - Task starts  
  - Task ends  
- Daily report at fixed time (15:00)

### 📲 Telegram Integration
- Sends task notifications via Telegram Bot API  
- Daily summary messages  
- Start/finish alerts  

---

## 🛠️ Tech Stack

- Python 3  
- Object-Oriented Programming (OOP)  
- JSON file storage  
- `datetime` module  
- `requests` (Telegram API)  
- Background scheduler loop  

---

## 📁 Project Structure

task-manager/  
│  
├── main.py          # CLI interface (user menu)  
├── classes.py       # TaskManager logic (OOP core)  
├── scheduler.py     # Background task notifier  
├── notifier.py      # Telegram message sender  
├── tasks.json       # Stored tasks (auto-generated)  
└── README.md  

---

## ▶️ How to Run

### 1. Clone the repository

git clone https://github.com/chawrzy/task-manager.git

### 2. Enter project directory

cd task-manager

### 3. Install dependencies

pip install requests

### 4. Run the CLI app

python main.py

### 5. (Optional) Run scheduler

python scheduler.py

---

## ⚙️ Telegram Setup

1. Create a bot using @BotFather  
2. Get your BOT TOKEN  
3. Get your CHAT ID  
4. Put them inside `notifier.py`:

TOKEN = \"YOUR_BOT_TOKEN\"  
CHAT_ID = \"YOUR_CHAT_ID\"

---

## 💡 Example Menu

--- welcome to task manager ---

[1] Add task  
[2] Remove task  
[3] Edit task  
[4] Show task  
[5] Filter tasks  
[6] Show all tasks  
[7] Save tasks  
[8] Exit  

---

## 🧠 Key Design Ideas

- Separation of CLI and business logic  
- Persistent data with JSON  
- Scheduler loop for automation  
- Real-time notifications via Telegram  
- Clean OOP structure  

---

## 📌 Future Improvements

- 🌐 Web version (FastAPI / Django)  
- 🖥 GUI (Tkinter / PyQt / React frontend)  
- 🔍 Search by keyword  
- 🏷 Task priority system  
- 📅 Calendar view  
- 🔔 Desktop notifications  
- ☁️ Cloud database (PostgreSQL / Firebase)  

---

## 👨‍💻 Author

Made by **Hesam** ✨  
Python developer building real-world projects for portfolio & job readiness  

---

## ⭐ Support

If you like this project:
- Give it a ⭐ on GitHub  
- Fork it  
- Improve it 🚀  
