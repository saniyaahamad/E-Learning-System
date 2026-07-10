# #GET METHOD
# from flask import Flask, jsonify
# from flask_mysqldb import MySQL
#
# app = Flask(__name__)
#
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'info123'
# app.config['MYSQL_DB'] = 'elearningdb'
#
# mysql = MySQL(app)
#
# @app.route('/teachers', methods=['GET'])
# def get_teachers():
#
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM teacher")
#     rows = cur.fetchall()
#     cur.close()
#
#     return jsonify(rows)
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)
#

# ##POST METHOD
# from flask import Flask, request, jsonify
# from flask_mysqldb import MySQL
#
# app = Flask(__name__)
#
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'info123'
# app.config['MYSQL_DB'] = 'elearningdb'
#
# mysql = MySQL(app)
# @app.route('/teachers', methods=['POST'])
# def add_teacher():
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         INSERT INTO teacher
#         (id,name,email,phone,subject,experience)
#         VALUES (%s,%s,%s,%s,%s,%s)
#         """,
#         (
#             data["id"],
#             data["name"],
#             data["email"],
#             data["phone"],
#             data["subject"],
#             data["experience"]
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Teacher Added Successfully"})
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)


# ##PUT METHOD
# @app.route('/teachers/<int:id>', methods=['PUT'])
# def update_teacher(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         UPDATE teacher
#         SET name=%s,
#             email=%s,
#             phone=%s,
#             subject=%s,
#             experience=%s
#         WHERE id=%s
#         """,
#         (
#             data["name"],
#             data["email"],
#             data["phone"],
#             data["subject"],
#             data["experience"],
#             id
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Teacher Updated Successfully"})
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)

# @app.route('/teachers/<string:name>', methods=['PATCH'])
# def patch_teacher(name):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     if "email" in data:
#         cur.execute(
#             "UPDATE teacher SET email=%s WHERE name=%s",
#             (data["email"], name)
#         )
#
#     if "phone" in data:
#         cur.execute(
#             "UPDATE teacher SET phone=%s WHERE name=%s",
#             (data["phone"], name)
#         )
#
#     if "subject" in data:
#         cur.execute(
#             "UPDATE teacher SET subject=%s WHERE name=%s",
#             (data["subject"], name)
#         )
#
#     if "experience" in data:
#         cur.execute(
#             "UPDATE teacher SET experience=%s WHERE name=%s",
#             (data["experience"], name)
#         )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Teacher Updated Successfully"})
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)

##GET METHOD
# @app.route('/teachers/<string:name>', methods=['DELETE'])
# def delete_teacher(name):
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "DELETE FROM teacher WHERE name=%s",
#         (name,)
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Teacher Deleted Successfully"})
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)