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


# GET ALL ENROLLMENTS
@app.get("/enrollments")
def get_enrollments():
    cur = connection.cursor()
    cur.execute("SELECT * FROM enrollment")
    rows = cur.fetchall()
    cur.close()

    return {"enrollments": rows}


# GET ONE ENROLLMENT
@app.get("/enrollments/{id}")
def get_enrollment(id: int):
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM enrollment WHERE id=%s",
        (id,)
    )
    row = cur.fetchone()
    cur.close()

    return {"enrollment": row}


# POST
@app.post("/enrollments")
def add_enrollment(data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        INSERT INTO enrollment
        (id, student_id, course_id, enrollment_date)
        VALUES (%s,%s,%s,%s)
        """,
        (
            data["id"],
            data["student_id"],
            data["course_id"],
            data["enrollment_date"]
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Enrollment Added Successfully"}


# PUT
@app.put("/enrollments/{id}")
def update_enrollment(id: int, data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        UPDATE enrollment
        SET student_id=%s,
            course_id=%s,
            enrollment_date=%s
        WHERE id=%s
        """,
        (
            data["student_id"],
            data["course_id"],
            data["enrollment_date"],
            id
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Enrollment Updated Successfully"}


# PATCH
@app.patch("/enrollments/{id}")
def patch_enrollment(id: int, data: dict):

    cur = connection.cursor()

    if "student_id" in data:
        cur.execute(
            "UPDATE enrollment SET student_id=%s WHERE id=%s",
            (data["student_id"], id)
        )

    if "course_id" in data:
        cur.execute(
            "UPDATE enrollment SET course_id=%s WHERE id=%s",
            (data["course_id"], id)
        )

    if "enrollment_date" in data:
        cur.execute(
            "UPDATE enrollment SET enrollment_date=%s WHERE id=%s",
            (data["enrollment_date"], id)
        )

    connection.commit()
    cur.close()

    return {"message": "Enrollment Updated Successfully"}


# DELETE
@app.delete("/enrollments/{id}")
def delete_enrollment(id: int):

    cur = connection.cursor()

    cur.execute(
        "DELETE FROM enrollment WHERE id=%s",
        (id,)
    )

    connection.commit()
    cur.close()

    return {"message": "Enrollment Deleted Successfully"}