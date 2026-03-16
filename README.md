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

## Local Setup
1. Make sure Python 3.10+ is installed.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

3. Install dependencies:
   ```bash
   pip install Flask werkzeug

4. Run the server:

   ```bash
   flask run

5. Open your browser and go to the link displayed in the terminal.

---
## User Login & Logout
- User authentication is done by comparing input passwords with hashed passwords in the database.
- Logout clears the session and redirects to the homepage.

## CS50 Certificate
[CS50 Certificate](https://cs50.harvard.edu/x/)
