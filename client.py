import socket
import os
from PIL import Image
from waitress import serve
from werkzeug.utils import secure_filename
from flask import Flask, flash, json, send_file, request, redirect, url_for
from contextlib import nullcontext
import RPi.GPIO as GPIO
from time import sleep

Prod = False
Port = 1567
DevPort = 1567
Ip = '192.168.0.126'
DevIP = '192.168.0.126'

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, 0)


@app.route("/", methods=['GET', 'POST'])
def OpenClose():
    if request.method == 'POST':
        pwm = GPIO.PWM(11, 50)
        pwm.start(0)
        op = (str)(request.get_json()).split(
            '{')[1].split('}')[0].split('\'')[3]
        if op == '1':
            print("open")
            pwm.ChangeDutyCycle(7)  # neutral position
            GPIO.output(13, 1)
            sleep(0.1)
            GPIO.output(13, 0)
            sleep(0.1)
            GPIO.output(13, 1)
            sleep(0.1)
            GPIO.output(13, 0)
        else:
            print("closed")
            pwm.ChangeDutyCycle(2.4)  # left -90 deg position
            sleep(0.2)
            i = 10
            while i > 0:
                GPIO.output(13, 1)
                sleep(0.05)
                GPIO.output(13, 0)
                sleep(0.05)
                i -= 1
        pwm.stop()
    return ""


@ app.route("/favicon.ico")
def favicon():
    fav = open("favicon.ico")
    return send_file("favicon.ico", mimetype='image/ico')


if __name__ == '__main__':
    if Prod:
        serve(app, host=Ip, port=Port)
    else:
        app.run(host=DevIP, port=DevPort, debug=True)
