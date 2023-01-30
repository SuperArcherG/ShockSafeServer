import socket
import os
from PIL import Image
from waitress import serve
from werkzeug.utils import secure_filename
from flask import Flask, flash, json, send_file, request, redirect, url_for
from contextlib import nullcontext

Prod = False
Port = 1567
DevPort = 1567
Ip = '192.168.0.126'
DevIP = '192.168.0.126'

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        op = (str)(request.get_json()).split('{')[1].split('}')[0]
        print(op)
    return ""

# @app.route("/assets")
# def assets():
#     return send_file(os.path.join("levels", "assets.zip"))


# @app.route("/change_password", methods=['GET', 'POST'])
# def change_password():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         oldPassowrd = request.form.get('old')
#         newPassowrd = request.form.get('new')
#         # Check if the user exists
#         users = os.listdir(USERS_FOLDER)
#         found = False
#         for x in users:
#             if x == username + '.txt':
#                 found = True
#         if not found:
#             return "err000 User not found: \"" + username + "\""  # err000
#         ValidLogin = open(os.path.join(
#             USERS_FOLDER, username + ".txt")).read() == oldPassowrd
#         if not ValidLogin:
#             return "err004 incorrect password for user \"" + username + "\""  # err004
#         if ValidLogin:
#             os.remove(os.path.join(USERS_FOLDER, username + ".txt"))
#             user = open(os.path.join(
#                 USERS_FOLDER, str(username)) + '.txt', 'x')
#             user.write(str(newPassowrd))
#             return open('Success.html')
#     return open('change_password.html')


# @app.route("/delete_user", methods=['GET', 'POST'])
# def deleteUser():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         # Check if the user exists
#         users = os.listdir(USERS_FOLDER)
#         found = False

#         # Check for user
#         for x in users:
#             if x == username + '.txt':
#                 found = True
#         if not found:
#             return "err000 User not found: \"" + username + "\""  # err000

#         # Check password
#         ValidLogin = open(os.path.join(
#             USERS_FOLDER, username + ".txt")).read() == password
#         if not ValidLogin:
#             return "err004 incorrect password for user \"" + username + "\""  # err004

#         # delete data
#         if ValidLogin:
#             os.remove(os.path.join(USERS_FOLDER, username + ".txt"))
#             return open('Success.html')
#     return open("delete_user.html")


@ app.route("/favicon.ico")
def favicon():
    fav = open("favicon.ico")
    return send_file("favicon.ico", mimetype='image/ico')


# @app.route("/owns")
# def owns():
#     filename = request.args.get('usr') + ".txt"
#     return send_file(OWNS_FOLDER + filename)


# @app.route("/owner")
# def owner():
#     filename = request.args.get('id') + ".txt"
#     # return 0
#     return send_file(OWNERS_FOLDER + filename)


# @app.route("/users")
# def users():
#     return str(os.listdir(USERS_FOLDER)).replace(".txt", "")


# # @app.route("/user")
# # def user2():
# #     return user()


# @app.route("/user")
# def uses():
#     username = request.args.get('usr')
#     return str(username)
#     # ADD MORE INFO


# @app.route("/cover", methods=['GET', 'POST'])
# def cover():
#     filename = request.args.get('id') + ".png"
#     return send_file(COVER_FOLDER+filename, mimetype='image/png')


# @ app.route("/icon", methods=['GET', 'POST'])
# def icon():
#     filename = request.args.get('id') + ".jpeg"
#     return send_file('levels/icon/' + filename, mimetype='image/jpeg')


# # @ app.route("/uploads", methods=['GET', 'POST'])
# # def uploads():
# #     filename = request.args.get('name')
# #     return send_file('levels/uploads/' + filename)


# @ app.route("/info", methods=['GET', 'POST'])
# def info():
#     filename = request.args.get('id') + ".json"
#     return send_file("levels/info/" + filename)


# @ app.route("/data")
# def data():
#     filename = request.args.get('id') + ".json"
#     return send_file("levels/data/" + filename)


if __name__ == '__main__':
    if Prod:
        serve(app, host=Ip, port=Port)
    else:
        app.run(host=DevIP, port=DevPort, debug=True)
