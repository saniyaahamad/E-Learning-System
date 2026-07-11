from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'info123'   # Put your actual password here
app.config['MYSQL_DB'] = 'elearningdb'

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('login.html')


# Login button action
@app.route('/check_login', methods=['POST'])
def check_login():

    username = request.form.get('username')
    password = request.form.get('password')

    # Accept any username and password
    if username and password:
        return redirect('/dashboard')
    else:
        return "Please enter Username and Password"


# ================= DASHBOARD =================
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# ================= STUDENTS =================
@app.route('/students')
def students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    cur.close()
    return render_template('students.html', students=data)


# ================= TEACHERS =================
@app.route('/teachers')
def teachers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM teacher")
    data = cur.fetchall()
    cur.close()
    return render_template('teachers.html', teachers=data)


# ================= COURSES =================
@app.route('/courses')
def courses():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM course")
    data = cur.fetchall()
    cur.close()
    return render_template('courses.html', courses=data)


# ================= SUBJECTS =================
@app.route('/subjects')
def subjects():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM subject")
    data = cur.fetchall()
    cur.close()
    return render_template('subjects.html', subjects=data)


# ================= ENROLLMENTS =================
@app.route('/enrollments')
def enrollments():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM enrollment")
    data = cur.fetchall()
    cur.close()
    return render_template('enrollments.html', enrollments=data)


# ================= ASSIGNMENTS =================
@app.route('/assignments')
def assignments():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM assignment")
    data = cur.fetchall()
    cur.close()
    return render_template('assignments.html', assignments=data)


# ================= QUIZZES =================
@app.route('/quizzes')
def quizzes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM quiz")
    data = cur.fetchall()
    cur.close()
    return render_template('quizzes.html', quizzes=data)


# ================= MARKS =================
@app.route('/marks')
def marks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM marks")
    data = cur.fetchall()
    cur.close()
    return render_template('marks.html', marks=data)


# ================= ATTENDANCE =================
@app.route('/attendance')
def attendance():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM attendance")
    data = cur.fetchall()
    cur.close()
    return render_template('attendance.html', attendance=data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)