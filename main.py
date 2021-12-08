from flask import Flask

api = Flask(__name__)

@api.route('/')
def home():
	return "This is the main page!"

@api.route('/stat')
def stat():
	return "no"

api.run(host = "0.0.0.0", port = 6969)
