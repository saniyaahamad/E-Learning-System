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


# GET ALL COURSES
@app.get("/courses")
def get_courses():
    cur = connection.cursor()
    cur.execute("SELECT * FROM course")
    rows = cur.fetchall()
    cur.close()

    return {"courses": rows}


# GET ONE COURSE
@app.get("/courses/{id}")
def get_course(id: int):
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM course WHERE id=%s",
        (id,)
    )
    row = cur.fetchone()
    cur.close()

    return {"course": row}


# POST
@app.post("/courses")
def add_course(data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        INSERT INTO course
        (id, course_name, duration, fees)
        VALUES (%s,%s,%s,%s)
        """,
        (
            data["id"],
            data["course_name"],
            data["duration"],
            data["fees"]
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Course Added Successfully"}


# PUT
@app.put("/courses/{id}")
def update_course(id: int, data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        UPDATE course
        SET course_name=%s,
            duration=%s,
            fees=%s
        WHERE id=%s
        """,
        (
            data["course_name"],
            data["duration"],
            data["fees"],
            id
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Course Updated Successfully"}


# PATCH
@app.patch("/courses/{id}")
def patch_course(id: int, data: dict):

    cur = connection.cursor()

    if "course_name" in data:
        cur.execute(
            "UPDATE course SET course_name=%s WHERE id=%s",
            (data["course_name"], id)
        )

    if "duration" in data:
        cur.execute(
            "UPDATE course SET duration=%s WHERE id=%s",
            (data["duration"], id)
        )

    if "fees" in data:
        cur.execute(
            "UPDATE course SET fees=%s WHERE id=%s",
            (data["fees"], id)
        )

    connection.commit()
    cur.close()

    return {"message": "Course Updated Successfully"}


# DELETE
@app.delete("/courses/{id}")
def delete_course(id: int):

    cur = connection.cursor()

    cur.execute(
        "DELETE FROM course WHERE id=%s",
        (id,)
    )

    connection.commit()
    cur.close()

    return {"message": "Course Deleted Successfully"}