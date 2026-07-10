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
# @app.route('/enrollments', methods=['GET'])
# def get_enrollments():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM enrollment")
#     rows = cur.fetchall()
#     cur.close()
#
#     return jsonify(rows)


# POST
# @app.route('/enrollments', methods=['POST'])
# def add_enrollment():
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         INSERT INTO enrollment
#         (id, student_id, course_id, enrollment_date)
#         VALUES (%s,%s,%s,%s)
#         """,
#         (
#             data["id"],
#             data["student_id"],
#             data["course_id"],
#             data["enrollment_date"]
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Enrollment Added Successfully"})
#
#
# # PUT
# @app.route('/enrollments/<int:id>', methods=['PUT'])
# def update_enrollment(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         UPDATE enrollment
#         SET student_id=%s,
#             course_id=%s,
#             enrollment_date=%s
#         WHERE id=%s
#         """,
#         (
#             data["student_id"],
#             data["course_id"],
#             data["enrollment_date"],
#             id
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Enrollment Updated Successfully"})
#
#
# # PATCH
# @app.route('/enrollments/<int:id>', methods=['PATCH'])
# def patch_enrollment(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     if "student_id" in data:
#         cur.execute(
#             "UPDATE enrollment SET student_id=%s WHERE id=%s",
#             (data["student_id"], id)
#         )
#
#     if "course_id" in data:
#         cur.execute(
#             "UPDATE enrollment SET course_id=%s WHERE id=%s",
#             (data["course_id"], id)
#         )
#
#     if "enrollment_date" in data:
#         cur.execute(
#             "UPDATE enrollment SET enrollment_date=%s WHERE id=%s",
#             (data["enrollment_date"], id)
#         )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Enrollment Updated Successfully"})
#
#
# # DELETE
# @app.route('/enrollments/<int:id>', methods=['DELETE'])
# def delete_enrollment(id):
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "DELETE FROM enrollment WHERE id=%s",
#         (id,)
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Enrollment Deleted Successfully"})


# if __name__ == "__main__":
#     app.run(port=8000, debug=True)