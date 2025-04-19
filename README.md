```markdown
# SQL Injection Demo - Flask Application

This project demonstrates a simple Flask web application with both secure and insecure login implementations. The purpose of this app is to showcase the risks of SQL injection vulnerabilities and how to mitigate them using secure coding practices.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- A code editor like [Visual Studio Code](https://code.visualstudio.com/)

## Setup Instructions

Follow these steps to set up and run the application:

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/your-repo/sqlinjectiondemo.git
cd sqlinjectiondemo/flask-template
```

### 2. Create a Virtual Environment
Create a Python virtual environment to isolate dependencies:
```bash
python -m venv .venv
```

Activate the virtual environment:
- On Windows:
  ```bash
  .venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies
Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database
Run the following command to initialize the SQLite database:
```bash
python app.py
```
This will create a `users.db` file with preloaded user credentials.

### 5. Run the Application
Start the Flask application:
```bash
python app.py
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Demonstrating the Application

### Insecure Login (SQL Injection Vulnerability)
1. Navigate to the insecure login page: [http://127.0.0.1:5000/login/insecure](http://127.0.0.1:5000/login/insecure).
2. Enter the following SQL injection payload in both the **Username** and **Password** fields:
   ```
   ' OR '1'='1
   ```
3. Click **Login**. You will be logged in without valid credentials, demonstrating the SQL injection vulnerability.

### Secure Login (Protected Against SQL Injection)
1. Navigate to the secure login page: [http://127.0.0.1:5000/login/secure](http://127.0.0.1:5000/login/secure).
2. Attempt the same SQL injection payload:
   ```
   ' OR '1'='1
   ```
3. Observe that the login fails, as the secure implementation uses parameterized queries to prevent SQL injection.

---

## Additional Notes

- The insecure login page is intentionally vulnerable to demonstrate SQL injection. **Do not use this code in production.**
- The secure login page demonstrates best practices for preventing SQL injection using parameterized queries.

---
