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


# GET ALL LOGINS
@app.get("/login")
def get_login():
    cur = connection.cursor()
    cur.execute("SELECT * FROM login")
    rows = cur.fetchall()
    cur.close()

    return {"login": rows}


# GET ONE LOGIN
@app.get("/login/{id}")
def get_one_login(id: int):
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM login WHERE id=%s",
        (id,)
    )
    row = cur.fetchone()
    cur.close()

    return {"login": row}


# POST
@app.post("/login")
def add_login(data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        INSERT INTO login
        (id, username, password, role)
        VALUES (%s,%s,%s,%s)
        """,
        (
            data["id"],
            data["username"],
            data["password"],
            data["role"]
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Login Added Successfully"}


# PUT
@app.put("/login/{id}")
def update_login(id: int, data: dict):

    cur = connection.cursor()

    cur.execute(
        """
        UPDATE login
        SET username=%s,
            password=%s,
            role=%s
        WHERE id=%s
        """,
        (
            data["username"],
            data["password"],
            data["role"],
            id
        )
    )

    connection.commit()
    cur.close()

    return {"message": "Login Updated Successfully"}


# PATCH
@app.patch("/login/{id}")
def patch_login(id: int, data: dict):

    cur = connection.cursor()

    if "username" in data:
        cur.execute(
            "UPDATE login SET username=%s WHERE id=%s",
            (data["username"], id)
        )

    if "password" in data:
        cur.execute(
            "UPDATE login SET password=%s WHERE id=%s",
            (data["password"], id)
        )

    if "role" in data:
        cur.execute(
            "UPDATE login SET role=%s WHERE id=%s",
            (data["role"], id)
        )

    connection.commit()
    cur.close()

    return {"message": "Login Updated Successfully"}


# DELETE
@app.delete("/login/{id}")
def delete_login(id: int):

    cur = connection.cursor()

    cur.execute(
        "DELETE FROM login WHERE id=%s",
        (id,)
    )

    connection.commit()
    cur.close()

    return {"message": "Login Deleted Successfully"}