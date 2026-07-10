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


# GET
# @app.route('/assignments', methods=['GET'])
# def get_assignments():
#
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM assignment")
#     rows = cur.fetchall()
#     cur.close()
#
#     return jsonify(rows)


# POST
# @app.route('/assignments', methods=['POST'])
# def add_assignment():
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         INSERT INTO assignment
#         (id, title, description, due_date)
#         VALUES (%s,%s,%s,%s)
#         """,
#         (
#             data["id"],
#             data["title"],
#             data["description"],
#             data["due_date"]
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Assignment Added Successfully"})
#
#
# # PUT
# @app.route('/assignments/<int:id>', methods=['PUT'])
# def update_assignment(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         UPDATE assignment
#         SET title=%s,
#             description=%s,
#             due_date=%s
#         WHERE id=%s
#         """,
#         (
#             data["title"],
#             data["description"],
#             data["due_date"],
#             id
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Assignment Updated Successfully"})
#
#
# # PATCH
# @app.route('/assignments/<int:id>', methods=['PATCH'])
# def patch_assignment(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     if "title" in data:
#         cur.execute(
#             "UPDATE assignment SET title=%s WHERE id=%s",
#             (data["title"], id)
#         )
#
#     if "description" in data:
#         cur.execute(
#             "UPDATE assignment SET description=%s WHERE id=%s",
#             (data["description"], id)
#         )
#
#     if "due_date" in data:
#         cur.execute(
#             "UPDATE assignment SET due_date=%s WHERE id=%s",
#             (data["due_date"], id)
#         )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Assignment Updated Successfully"})
#
#
# # DELETE
# @app.route('/assignments/<int:id>', methods=['DELETE'])
# def delete_assignment(id):
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "DELETE FROM assignment WHERE id=%s",
#         (id,)
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Assignment Deleted Successfully"})
#
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)