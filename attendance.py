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


# GET ALL ATTENDANCE
@app.get("/attendance")
def get_attendance():
    cur = connection.cursor()
    cur.execute("SELECT * FROM attendance")
    rows = cur.fetchall()
    cur.close()

    return {"attendance": rows}


# GET ONE ATTENDANCE RECORD
@app.get("/attendance/{id}")
def get_one_attendance(id: int):
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM attendance WHERE id=%s",
        (id,)
    )
    row = cur.fetchone()
    cur.close()

    return {"attendance": row}


# POST
@app.post("/attendance")
def add_attendance(data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        INSERT INTO attendance
        (id, student_id, attendance_date, status)
        VALUES (%s,%s,%s,%s)
        """,
        (
            data["id"],
            data["student_id"],
            data["attendance_date"],
            data["status"]
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Attendance Added Successfully"}


# PUT
@app.put("/attendance/{id}")
def update_attendance(id: int, data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        UPDATE attendance
        SET student_id=%s,
            attendance_date=%s,
            status=%s
        WHERE id=%s
        """,
        (
            data["student_id"],
            data["attendance_date"],
            data["status"],
            id
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Attendance Updated Successfully"}


# PATCH
@app.patch("/attendance/{id}")
def patch_attendance(id: int, data: dict):

    cur = connection.cursor()

    if "student_id" in data:
        cur.execute(
            "UPDATE attendance SET student_id=%s WHERE id=%s",
            (data["student_id"], id)
        )

    if "attendance_date" in data:
        cur.execute(
            "UPDATE attendance SET attendance_date=%s WHERE id=%s",
            (data["attendance_date"], id)
        )

    if "status" in data:
        cur.execute(
            "UPDATE attendance SET status=%s WHERE id=%s",
            (data["status"], id)
        )

    connection.commit()
    cur.close()

    return {"message": "Attendance Updated Successfully"}


# DELETE
@app.delete("/attendance/{id}")
def delete_attendance(id: int):

    cur = connection.cursor()

    cur.execute(
        "DELETE FROM attendance WHERE id=%s",
        (id,)
    )

    connection.commit()
    cur.close()

    return {"message": "Attendance Deleted Successfully"}