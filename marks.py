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
# @app.route('/marks', methods=['GET'])
# def get_marks():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM marks")
#     rows = cur.fetchall()
#     cur.close()
#
#     return jsonify(rows)
#
#
# # POST
# @app.route('/marks', methods=['POST'])
# def add_marks():
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         INSERT INTO marks
#         (id, student_id, subject_id, marks)
#         VALUES (%s,%s,%s,%s)
#         """,
#         (
#             data["id"],
#             data["student_id"],
#             data["subject_id"],
#             data["marks"]
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Marks Added Successfully"})
#
#
# # PUT
# @app.route('/marks/<int:id>', methods=['PUT'])
# def update_marks(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         UPDATE marks
#         SET student_id=%s,
#             subject_id=%s,
#             marks=%s
#         WHERE id=%s
#         """,
#         (
#             data["student_id"],
#             data["subject_id"],
#             data["marks"],
#             id
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Marks Updated Successfully"})
#
#
# # PATCH
# @app.route('/marks/<int:id>', methods=['PATCH'])
# def patch_marks(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     if "student_id" in data:
#         cur.execute(
#             "UPDATE marks SET student_id=%s WHERE id=%s",
#             (data["student_id"], id)
#         )
#
#     if "subject_id" in data:
#         cur.execute(
#             "UPDATE marks SET subject_id=%s WHERE id=%s",
#             (data["subject_id"], id)
#         )
#
#     if "marks" in data:
#         cur.execute(
#             "UPDATE marks SET marks=%s WHERE id=%s",
#             (data["marks"], id)
#         )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Marks Updated Successfully"})
#
#
# # DELETE
# @app.route('/marks/<int:id>', methods=['DELETE'])
# def delete_marks(id):
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "DELETE FROM marks WHERE id=%s",
#         (id,)
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Marks Deleted Successfully"})


# if __name__ == "__main__":
#     app.run(port=8000, debug=True)