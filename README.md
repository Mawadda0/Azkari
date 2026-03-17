# Azkari 🌙

**Azkari** is a web application designed to make daily dhikr, easier by displaying Arabic texts and allowing users to count repetitions of each dhikr using digital counters. The project uses **Flask**, **HTML/CSS/JS**, and **SQLite**.

---
## Features
- Clean and user-friendly interface.
- Display dhikr texts in Arabic with clear formatting.
- Counters for each dhikr to track repetitions.
- Reset button to start counting from zero.
- User authentication with login and logout.
- Session-based tracking of counters.
- Responsive design for all devices.

---
## Technologies Used
- **Python** + **Flask** (Backend)
- **HTML / CSS / JavaScript** (Frontend)
- **SQLite** database for storing users
- **Werkzeug** for password hashing and verification


---
## ⚙️ Setup Instructions

#### Follow these steps to run the project locally:

1. Install Python, Make sure Python 3.10+ is installed.

2. Install pip

```bash
python -m ensurepip --upgrade
```

3. Install required libraries

```bash
pip install flask flask-session cs50 werkzeug
```

5. Run the application

```bash
flask run
```

6. Open your browser and go to the link displayed in the terminal.

#### if you are facing any problem at running locally after followin the steps, make sure that every file matches the right place in the repository.

---
## User Login & Logout
- User authentication is done by comparing input passwords with hashed passwords in the database.
- Logout clears the session and redirects to the homepage.
  
---
## [CS50 Certificate 😋](https://certificates.cs50.io/aab8a235-8a70-43a8-a3eb-67fcde0fb13b.png?size=letter)
