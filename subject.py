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


# GET ALL SUBJECTS
@app.get("/subjects")
def get_subjects():
    cur = connection.cursor()
    cur.execute("SELECT * FROM subject")
    rows = cur.fetchall()
    cur.close()

    return {"subjects": rows}



# POST
@app.post("/subjects")
def add_subject(data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        INSERT INTO subject
        (id, subject_name, course_name, credits)
        VALUES (%s,%s,%s,%s)
        """,
        (
            data["id"],
            data["subject_name"],
            data["course_name"],
            data["credits"]
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Subject Added Successfully"}


# PUT
@app.put("/subjects/{id}")
def update_subject(id: int, data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        UPDATE subject
        SET subject_name=%s,
            course_name=%s,
            credits=%s
        WHERE id=%s
        """,
        (
            data["subject_name"],
            data["course_name"],
            data["credits"],
            id
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Subject Updated Successfully"}


# PATCH
@app.patch("/subjects/{id}")
def patch_subject(id: int, data: dict):

    cur = connection.cursor()

    if "subject_name" in data:
        cur.execute(
            "UPDATE subject SET subject_name=%s WHERE id=%s",
            (data["subject_name"], id)
        )

    if "course_name" in data:
        cur.execute(
            "UPDATE subject SET course_name=%s WHERE id=%s",
            (data["course_name"], id)
        )

    if "credits" in data:
        cur.execute(
            "UPDATE subject SET credits=%s WHERE id=%s",
            (data["credits"], id)
        )

    connection.commit()
    cur.close()

    return {"message": "Subject Patched Successfully"}


# DELETE
@app.delete("/subjects/{id}")
def delete_subject(id: int):

    cur = connection.cursor()

    cur.execute(
        "DELETE FROM subject WHERE id=%s",
        (id,)
    )

    connection.commit()
    cur.close()

    return {"message": "Subject Deleted Successfully"}