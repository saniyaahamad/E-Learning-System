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


# GET ALL MARKS
@app.get("/marks")
def get_marks():
    cur = connection.cursor()
    cur.execute("SELECT * FROM marks")
    rows = cur.fetchall()
    cur.close()

    return {"marks": rows}


# GET ONE MARK
@app.get("/marks/{id}")
def get_one_mark(id: int):
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM marks WHERE id=%s",
        (id,)
    )
    row = cur.fetchone()
    cur.close()

    return {"mark": row}


# POST
@app.post("/marks")
def add_marks(data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        INSERT INTO marks
        (id, student_id, subject_id, marks)
        VALUES (%s,%s,%s,%s)
        """,
        (
            data["id"],
            data["student_id"],
            data["subject_id"],
            data["marks"]
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Marks Added Successfully"}


# PUT
@app.put("/marks/{id}")
def update_marks(id: int, data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        UPDATE marks
        SET student_id=%s,
            subject_id=%s,
            marks=%s
        WHERE id=%s
        """,
        (
            data["student_id"],
            data["subject_id"],
            data["marks"],
            id
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Marks Updated Successfully"}


# PATCH
@app.patch("/marks/{id}")
def patch_marks(id: int, data: dict):

    cur = connection.cursor()

    if "student_id" in data:
        cur.execute(
            "UPDATE marks SET student_id=%s WHERE id=%s",
            (data["student_id"], id)
        )

    if "subject_id" in data:
        cur.execute(
            "UPDATE marks SET subject_id=%s WHERE id=%s",
            (data["subject_id"], id)
        )

    if "marks" in data:
        cur.execute(
            "UPDATE marks SET marks=%s WHERE id=%s",
            (data["marks"], id)
        )

    connection.commit()
    cur.close()

    return {"message": "Marks Updated Successfully"}


# DELETE
@app.delete("/marks/{id}")
def delete_marks(id: int):

    cur = connection.cursor()

    cur.execute(
        "DELETE FROM marks WHERE id=%s",
        (id,)
    )

    connection.commit()
    cur.close()

    return {"message": "Marks Deleted Successfully"}