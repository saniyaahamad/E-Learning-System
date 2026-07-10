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
# @app.route('/subjects', methods=['GET'])
# def get_subjects():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM subject")
#     rows = cur.fetchall()
#     cur.close()
#     return jsonify(rows)


# POST
# @app.route('/subjects', methods=['POST'])
# def add_subject():
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         INSERT INTO subject
#         (id, subject_name, course_name, credits)
#         VALUES (%s,%s,%s,%s)
#         """,
#         (
#             data["id"],
#             data["subject_name"],
#             data["course_name"],
#             data["credits"]
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Subject Added Successfully"})

#
# # PUT
# @app.route('/subjects/<int:id>', methods=['PUT'])
# def update_subject(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         UPDATE subject
#         SET subject_name=%s,
#             course_name=%s,
#             credits=%s
#         WHERE id=%s
#         """,
#         (
#             data["subject_name"],
#             data["course_name"],
#             data["credits"],
#             id
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Subject Updated Successfully"})
#
#
# # PATCH
# @app.route('/subjects/<int:id>', methods=['PATCH'])
# def patch_subject(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     if "subject_name" in data:
#         cur.execute(
#             "UPDATE subject SET subject_name=%s WHERE id=%s",
#             (data["subject_name"], id)
#         )
#
#     if "course_name" in data:
#         cur.execute(
#             "UPDATE subject SET course_name=%s WHERE id=%s",
#             (data["course_name"], id)
#         )
#
#     if "credits" in data:
#         cur.execute(
#             "UPDATE subject SET credits=%s WHERE id=%s",
#             (data["credits"], id)
#         )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Subject Updated Successfully"})
#
#
# # DELETE
# @app.route('/subjects/<int:id>', methods=['DELETE'])
# def delete_subject(id):
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "DELETE FROM subject WHERE id=%s",
#         (id,)
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Subject Deleted Successfully"})
#
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)