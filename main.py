from flask import Flask, request
from threading import Thread
from replit import db #the db which i will use
import os
from dotenv import load_dotenv

load_dotenv()

PASS = os.getenv("PASS")

db["stat"] = "flase"

api = Flask('')


@api.route('/')
def home():
	return "no"


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
			db["stat"] = "false"
			return "OK"
		else:
			return "ERROR"
	else:
		return "wrong password"
	


def run():
	api.run(host="0.0.0.0", port=6969)


t = Thread(target=run)
t.start()
