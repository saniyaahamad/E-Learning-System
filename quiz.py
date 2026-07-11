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


# GET ALL QUIZZES
@app.get("/quizzes")
def get_quizzes():
    cur = connection.cursor()
    cur.execute("SELECT * FROM quiz")
    rows = cur.fetchall()
    cur.close()

    return {"quizzes": rows}


# GET ONE QUIZ
@app.get("/quizzes/{id}")
def get_quiz(id: int):
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM quiz WHERE id=%s",
        (id,)
    )
    row = cur.fetchone()
    cur.close()

    return {"quiz": row}


# POST
@app.post("/quizzes")
def add_quiz(data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        INSERT INTO quiz
        (id, title, total_marks, quiz_date)
        VALUES (%s,%s,%s,%s)
        """,
        (
            data["id"],
            data["title"],
            data["total_marks"],
            data["quiz_date"]
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Quiz Added Successfully"}


# PUT
@app.put("/quizzes/{id}")
def update_quiz(id: int, data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        UPDATE quiz
        SET title=%s,
            total_marks=%s,
            quiz_date=%s
        WHERE id=%s
        """,
        (
            data["title"],
            data["total_marks"],
            data["quiz_date"],
            id
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Quiz Updated Successfully"}


# PATCH
@app.patch("/quizzes/{id}")
def patch_quiz(id: int, data: dict):

    cur = connection.cursor()

    if "title" in data:
        cur.execute(
            "UPDATE quiz SET title=%s WHERE id=%s",
            (data["title"], id)
        )

    if "total_marks" in data:
        cur.execute(
            "UPDATE quiz SET total_marks=%s WHERE id=%s",
            (data["total_marks"], id)
        )

    if "quiz_date" in data:
        cur.execute(
            "UPDATE quiz SET quiz_date=%s WHERE id=%s",
            (data["quiz_date"], id)
        )

    connection.commit()
    cur.close()

    return {"message": "Quiz Updated Successfully"}


# DELETE
@app.delete("/quizzes/{id}")
def delete_quiz(id: int):

    cur = connection.cursor()

    cur.execute(
        "DELETE FROM quiz WHERE id=%s",
        (id,)
    )

    connection.commit()
    cur.close()

    return {"message": "Quiz Deleted Successfully"}