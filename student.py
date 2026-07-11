from fastapi import FastAPI
import pymysql

app = FastAPI()

# MySQL Connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="info123",
    database="elearningdb"
)


# GET ALL STUDENTS
@app.get("/students")
def get_students():
    cur = connection.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    cur.close()

    return {"students": rows}


# GET ONE STUDENT
@app.get("/students/{id}")
def get_student(id: int):
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM student WHERE id=%s",
        (id,)
    )
    row = cur.fetchone()
    cur.close()

    return {"student": row}


# POST
@app.post("/students")
def add_student(data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        INSERT INTO student
        (id,name,age,email,phone,course)
        VALUES (%s,%s,%s,%s,%s,%s)
        """,
        (
            data["id"],
            data["name"],
            data["age"],
            data["email"],
            data["phone"],
            data["course"]
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Student Added Successfully"}


# PUT
@app.put("/students/{id}")
def update_student(id: int, data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        UPDATE student
        SET name=%s,
            age=%s,
            email=%s,
            phone=%s,
            course=%s
        WHERE id=%s
        """,
        (
            data["name"],
            data["age"],
            data["email"],
            data["phone"],
            data["course"],
            id
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Student Updated Successfully"}


# PATCH
@app.patch("/students/{name}")
def patch_student(name: str, data: dict):

    cur = connection.cursor()

    if "age" in data:
        cur.execute(
            "UPDATE student SET age=%s WHERE name=%s",
            (data["age"], name)
        )

    if "email" in data:
        cur.execute(
            "UPDATE student SET email=%s WHERE name=%s",
            (data["email"], name)
        )

    if "phone" in data:
        cur.execute(
            "UPDATE student SET phone=%s WHERE name=%s",
            (data["phone"], name)
        )

    if "course" in data:
        cur.execute(
            "UPDATE student SET course=%s WHERE name=%s",
            (data["course"], name)
        )

    connection.commit()
    cur.close()

    return {"message": "Student Updated Successfully"}


# DELETE
@app.delete("/students/{name}")
def delete_student(name: str):

    cur = connection.cursor()

    cur.execute(
        "DELETE FROM student WHERE name=%s",
        (name,)
    )

    connection.commit()
    cur.close()

    return {"message": "Student Deleted Successfully"}