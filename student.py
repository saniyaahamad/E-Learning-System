##GET METHOD
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
# @app.route('/students', methods=['GET'])
# def get_students():
#
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM student")
#     rows = cur.fetchall()
#     cur.close()
#
#     return jsonify(rows)
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)

##POST METHOD
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
#
# @app.route('/students', methods=['POST'])
# def add_student():
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "INSERT INTO student(id,name,age,email,phone,course) VALUES(%s,%s,%s,%s,%s,%s)",
#         (data["id"],
#          data["name"],
#          data["age"],
#          data["email"],
#          data["phone"],
#          data["course"])
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message":"Student Added Successfully"})
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)

##PUT METHOD
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
#
# @app.route('/students/<int:id>', methods=['PUT'])
# def update_student(id):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         """
#         UPDATE student
#         SET name=%s,
#             age=%s,
#             email=%s,
#             phone=%s,
#             course=%s
#         WHERE id=%s
#         """,
#         (
#             data["name"],
#             data["age"],
#             data["email"],
#             data["phone"],
#             data["course"],
#             id
#         )
#     )
#
#     mysql.connection.commit()
#
#     print("Rows Updated:", cur.rowcount)   # Debug

#     cur.close()
#
#     return jsonify({"message": "Student Updated Successfully"})
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)


##PATCH METHOD

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
#
# @app.route('/students/<string:name>', methods=['PATCH'])
# def patch_student(name):
#
#     data = request.get_json()
#
#     cur = mysql.connection.cursor()
#
#     if "age" in data:
#         cur.execute(
#             "UPDATE student SET age=%s WHERE name=%s",
#             (data["age"], name)
#         )
#
#     if "email" in data:
#         cur.execute(
#             "UPDATE student SET email=%s WHERE name=%s",
#             (data["email"], name)
#         )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message":"Student Updated Successfully"})
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)

##DELETE METHOD

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
# @app.route('/students/<string:name>', methods=['DELETE'])
# def delete_student(name):
#
#     cur = mysql.connection.cursor()
#
#     cur.execute(
#         "DELETE FROM student WHERE name=%s",
#         (name,)
#     )
#
#     mysql.connection.commit()
#     cur.close()
#
#     return jsonify({"message": "Student Deleted Successfully"})
#
# if __name__ == "__main__":
#     app.run(port=8000, debug=True)