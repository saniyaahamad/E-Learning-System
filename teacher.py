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


# GET ALL TEACHERS
@app.get("/teachers")
def get_teachers():
    cur = connection.cursor()
    cur.execute("SELECT * FROM teacher")
    rows = cur.fetchall()
    cur.close()

    return {"teachers": rows}


# GET ONE TEACHER BY ID
@app.get("/teachers/{id}")
def get_teacher(id: int):
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM teacher WHERE id=%s",
        (id,)
    )
    row = cur.fetchone()
    cur.close()

    return {"teacher": row}


# POST
@app.post("/teachers")
def add_teacher(data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        INSERT INTO teacher
        (id,name,email,phone,subject,experience)
        VALUES (%s,%s,%s,%s,%s,%s)
        """,
        (
            data["id"],
            data["name"],
            data["email"],
            data["phone"],
            data["subject"],
            data["experience"]
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Teacher Added Successfully"}


# PUT
@app.put("/teachers/{id}")
def update_teacher(id: int, data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        UPDATE teacher
        SET name=%s,
            email=%s,
            phone=%s,
            subject=%s,
            experience=%s
        WHERE id=%s
        """,
        (
            data["name"],
            data["email"],
            data["phone"],
            data["subject"],
            data["experience"],
            id
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Teacher Updated Successfully"}


# PATCH
@app.patch("/teachers/{name}")
def patch_teacher(name: str, data: dict):

    cur = connection.cursor()

    if "email" in data:
        cur.execute(
            "UPDATE teacher SET email=%s WHERE name=%s",
            (data["email"], name)
        )

    if "phone" in data:
        cur.execute(
            "UPDATE teacher SET phone=%s WHERE name=%s",
            (data["phone"], name)
        )

    if "subject" in data:
        cur.execute(
            "UPDATE teacher SET subject=%s WHERE name=%s",
            (data["subject"], name)
        )

    if "experience" in data:
        cur.execute(
            "UPDATE teacher SET experience=%s WHERE name=%s",
            (data["experience"], name)
        )

    connection.commit()
    cur.close()

    return {"message": "Teacher Updated Successfully"}


# DELETE
@app.delete("/teachers/{name}")
def delete_teacher(name: str):

    cur = connection.cursor()

    cur.execute(
        "DELETE FROM teacher WHERE name=%s",
        (name,)
    )

    connection.commit()
    cur.close()

    return {"message": "Teacher Deleted Successfully"}