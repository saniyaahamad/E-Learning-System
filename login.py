# from flask import Flask, request, jsonify
# from flask_mysqldb import MySQL
#
# app = Flask(__name__)
#
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'info123'
# app.config['MYSQL_DB'] = 'elearningdb'

mysql = MySQL(app)


# GET
# @app.route('/login', methods=['GET'])
# def get_login():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM login")
#     rows = cur.fetchall()
#     cur.close()
#
#     return jsonify(rows)


# POST
# @app.route('/login', methods=['POST'])
# def add_login():
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         INSERT INTO login
#         (id, username, password, role)
#         VALUES (%s,%s,%s,%s)
#         """,
#         (
#             data["id"],
#             data["username"],
#             data["password"],
#             data["role"]
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Login Added Successfully"})
#
#
# # PUT
# @app.route('/login/<int:id>', methods=['PUT'])
# def update_login(id):
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         UPDATE login
#         SET username=%s,
#             password=%s,
#             role=%s
#         WHERE id=%s
#         """,
#         (
#             data["username"],
#             data["password"],
#             data["role"],
#             id
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Login Updated Successfully"})

#
# # PATCH
# @app.route('/login/<int:id>', methods=['PATCH'])
# def patch_login(id):
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     if "username" in data:
#         cur.execute(
#             "UPDATE login SET username=%s WHERE id=%s",
#             (data["username"], id)
#         )
#
#     if "password" in data:
#         cur.execute(
#             "UPDATE login SET password=%s WHERE id=%s",
#             (data["password"], id)
#         )
#
#     if "role" in data:
#         cur.execute(
#             "UPDATE login SET role=%s WHERE id=%s",
#             (data["role"], id)
#         )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Login Updated Successfully"})
#
#
# # DELETE
# @app.route('/login/<int:id>', methods=['DELETE'])
# def delete_login(id):
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "DELETE FROM login WHERE id=%s",
#         (id,)
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Login Deleted Successfully"})
# #
# #
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)