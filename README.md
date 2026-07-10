# E-Learning Management System

A RESTful API based E-Learning Management System developed using Python, Flask, and MySQL. The project provides CRUD operations for managing students, teachers, courses, subjects, enrollments, assignments, quizzes, marks, attendance, and login information.

## Features

- Student Management
- Teacher Management
- Course Management
- Subject Management
- Enrollment Management
- Assignment Management
- Quiz Management
- Marks Management
- Attendance Management
- Login Management
- REST APIs using Flask
- MySQL Database Integration

## Technologies Used

- Python
- Flask
- MySQL
- Flask-MySQLdb
- Postman
- HTML
- CSS
- Git & GitHub

## Project Structure

```text
E-Learning-System
│
├── student.py
├── teacher.py
├── course.py
├── subject.py
├── enrollment.py
├── assignment.py
├── quiz.py
├── marks.py
├── attendance.py
├── login.py
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/E-Learning-System.git
```

### Move to Project Folder

```bash
cd E-Learning-System
```

### Install Dependencies

```bash
pip install flask flask-mysqldb
```

### Configure MySQL Database

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'info123'
app.config['MYSQL_DB'] = 'elearningdb'
```

### Run the Application

```bash
python student.py
```

or

```bash
python teacher.py
```

or any module you want to execute.

## API Modules

- Students API
- Teachers API
- Courses API
- Subjects API
- Enrollments API
- Assignments API
- Quizzes API
- Marks API
- Attendance API
- Login API

## Testing

The APIs can be tested using:

- Postman
- Browser (GET requests)

## Future Enhancements

- User Authentication with JWT
- Password Encryption
- Frontend using React
- Dashboard and Reports
- File Upload for Assignments
- Online Examination System


## License

This project is developed for educational and learning purposes.
