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


# GET ALL ASSIGNMENTS
@app.get("/assignments")
def get_assignments():
    cur = connection.cursor()
    cur.execute("SELECT * FROM assignment")
    rows = cur.fetchall()
    cur.close()

    return {"assignments": rows}


# GET ONE ASSIGNMENT
@app.get("/assignments/{id}")
def get_assignment(id: int):
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM assignment WHERE id=%s",
        (id,)
    )
    row = cur.fetchone()
    cur.close()

    return {"assignment": row}


# POST
@app.post("/assignments")
def add_assignment(data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        INSERT INTO assignment
        (id, title, description, due_date)
        VALUES (%s,%s,%s,%s)
        """,
        (
            data["id"],
            data["title"],
            data["description"],
            data["due_date"]
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Assignment Added Successfully"}


# PUT
@app.put("/assignments/{id}")
def update_assignment(id: int, data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        UPDATE assignment
        SET title=%s,
            description=%s,
            due_date=%s
        WHERE id=%s
        """,
        (
            data["title"],
            data["description"],
            data["due_date"],
            id
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Assignment Updated Successfully"}


# PATCH
@app.patch("/assignments/{id}")
def patch_assignment(id: int, data: dict):

    cur = connection.cursor()

    if "title" in data:
        cur.execute(
            "UPDATE assignment SET title=%s WHERE id=%s",
            (data["title"], id)
        )

    if "description" in data:
        cur.execute(
            "UPDATE assignment SET description=%s WHERE id=%s",
            (data["description"], id)
        )

    if "due_date" in data:
        cur.execute(
            "UPDATE assignment SET due_date=%s WHERE id=%s",
            (data["due_date"], id)
        )

    connection.commit()
    cur.close()

    return {"message": "Assignment Updated Successfully"}


# DELETE
@app.delete("/assignments/{id}")
def delete_assignment(id: int):

    cur = connection.cursor()

    cur.execute(
        "DELETE FROM assignment WHERE id=%s",
        (id,)
    )

    connection.commit()
    cur.close()

    return {"message": "Assignment Deleted Successfully"}