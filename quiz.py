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
# @app.route('/quizzes', methods=['GET'])
# def get_quizzes():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM quiz")
#     rows = cur.fetchall()
#     cur.close()
#
#     return jsonify(rows)


# POST
# @app.route('/quizzes', methods=['POST'])
# def add_quiz():
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         INSERT INTO quiz
#         (id, title, total_marks, quiz_date)
#         VALUES (%s,%s,%s,%s)
#         """,
#         (
#             data["id"],
#             data["title"],
#             data["total_marks"],
#             data["quiz_date"]
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Quiz Added Successfully"})
#
#
# # PUT
# @app.route('/quizzes/<int:id>', methods=['PUT'])
# def update_quiz(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         UPDATE quiz
#         SET title=%s,
#             total_marks=%s,
#             quiz_date=%s
#         WHERE id=%s
#         """,
#         (
#             data["title"],
#             data["total_marks"],
#             data["quiz_date"],
#             id
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Quiz Updated Successfully"})
#
#
# # PATCH
# @app.route('/quizzes/<int:id>', methods=['PATCH'])
# def patch_quiz(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     if "title" in data:
#         cur.execute(
#             "UPDATE quiz SET title=%s WHERE id=%s",
#             (data["title"], id)
#         )
#
#     if "total_marks" in data:
#         cur.execute(
#             "UPDATE quiz SET total_marks=%s WHERE id=%s",
#             (data["total_marks"], id)
#         )
#
#     if "quiz_date" in data:
#         cur.execute(
#             "UPDATE quiz SET quiz_date=%s WHERE id=%s",
#             (data["quiz_date"], id)
#         )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Quiz Updated Successfully"})
#
#
# # DELETE
# @app.route('/quizzes/<int:id>', methods=['DELETE'])
# def delete_quiz(id):
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "DELETE FROM quiz WHERE id=%s",
#         (id,)
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Quiz Deleted Successfully"})
#
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)