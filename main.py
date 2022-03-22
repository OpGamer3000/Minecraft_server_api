from flask import Flask, request
from threading import Thread
from replit import db  #the db which i will use
import os
from dotenv import load_dotenv
import time

load_dotenv()

PASS = os.getenv("PASS")

current_time = time.time()

api = Flask('')


@api.route('/')
def home():
    return "yes"


@api.route("/stat")
def stat():
    stat = db["stat"]
    return stat


@api.route("/setStat")
def setStat():
    request.args["pass"]
    stat = request.args.get("stat")
    password = request.args.get("pass")

    if password == PASS:
        if stat == "true":
            db["stat"] = "true"
            return "OK"
        elif stat == "false":
            global current_time
            current_time = time.time()
            db["stat"] = "false"
            return "OK"
        else:
            return "ERROR"
    else:
        return "wrong password"


@api.route("/getDowntime")
def getDowntime():
    stat = db["stat"]
    if stat == "false":
        global current_time
        now = time.time()
        total = int(now - current_time)
        return str(total)
    elif stat == "true":
        return "true"
    else:
        return "ERROR"


def run():
    api.run(host="0.0.0.0", port=6969)


t = Thread(target=run)
t.start()
