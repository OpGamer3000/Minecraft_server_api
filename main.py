from flask import Flask

api = Flask('')

api.route('/')
def home():
  return "This is the main page!"

#no u

api.run(host = "0.0.0.0", port = 6969)
