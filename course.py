##GET METHOD
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'info123'
app.config['MYSQL_DB'] = 'elearningdb'

mysql = MySQL(app)
# @app.route('/courses', methods=['GET'])
# def get_courses():
#
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM course")
#     rows = cur.fetchall()
#     cur.close()
#
#     return jsonify(rows)
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)


##POST METHOD
# @app.route('/courses', methods=['POST'])
# def add_course():
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         INSERT INTO course
#         (id, course_name, duration, fees)
#         VALUES (%s, %s, %s, %s)
#         """,
#         (
#             data["id"],
#             data["course_name"],
#             data["duration"],
#             data["fees"]
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Course Added Successfully"})
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)

##PUT METHOD
# @app.route('/courses/<int:id>', methods=['PUT'])
# def update_course(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         UPDATE course
#         SET course_name=%s,
#             duration=%s,
#             fees=%s
#         WHERE id=%s
#         """,
#         (
#             data["course_name"],
#             data["duration"],
#             data["fees"],
#             id
#         )
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Course Updated Successfully"})
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)

##PATCH METHOD
# @app.route('/courses/<int:id>', methods=['PATCH'])
# def patch_course(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     if "course_name" in data:
#         cur.execute(
#             "UPDATE course SET course_name=%s WHERE id=%s",
#             (data["course_name"], id)
#         )
#
#     if "duration" in data:
#         cur.execute(
#             "UPDATE course SET duration=%s WHERE id=%s",
#             (data["duration"], id)
#         )
#
#     if "fees" in data:
#         cur.execute(
#             "UPDATE course SET fees=%s WHERE id=%s",
#             (data["fees"], id)
#         )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Course Updated Successfully"})
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)


# ##DELETE METHOD
# @app.route('/courses/<int:id>', methods=['DELETE'])
# def delete_course(id):
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "DELETE FROM course WHERE id=%s",
#         (id,)
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Course Deleted Successfully"})
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)