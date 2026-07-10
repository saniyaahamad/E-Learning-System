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
# @app.route('/attendance', methods=['GET'])
# def get_attendance():
#
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM attendance")
#     rows = cur.fetchall()
#     cur.close()
#
#     return jsonify(rows)


# POST
# @app.route('/attendance', methods=['POST'])
# def add_attendance():
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         INSERT INTO attendance
#         (id, student_id, attendance_date, status)
#         VALUES (%s,%s,%s,%s)
#         """,
#         (
#             data["id"],
#             data["student_id"],
#             data["attendance_date"],
#             data["status"]
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Attendance Added Successfully"})
#
#
# # PUT
# @app.route('/attendance/<int:id>', methods=['PUT'])
# def update_attendance(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         UPDATE attendance
#         SET student_id=%s,
#             attendance_date=%s,
#             status=%s
#         WHERE id=%s
#         """,
#         (
#             data["student_id"],
#             data["attendance_date"],
#             data["status"],
#             id
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Attendance Updated Successfully"})
#
#
# # PATCH
# @app.route('/attendance/<int:id>', methods=['PATCH'])
# def patch_attendance(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     if "student_id" in data:
#         cur.execute(
#             "UPDATE attendance SET student_id=%s WHERE id=%s",
#             (data["student_id"], id)
#         )
#
#     if "attendance_date" in data:
#         cur.execute(
#             "UPDATE attendance SET attendance_date=%s WHERE id=%s",
#             (data["attendance_date"], id)
#         )
#
#     if "status" in data:
#         cur.execute(
#             "UPDATE attendance SET status=%s WHERE id=%s",
#             (data["status"], id)
#         )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Attendance Updated Successfully"})
#
#
# # DELETE
# @app.route('/attendance/<int:id>', methods=['DELETE'])
# def delete_attendance(id):
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "DELETE FROM attendance WHERE id=%s",
#         (id,)
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Attendance Deleted Successfully"})

#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)