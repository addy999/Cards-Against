from flask import Flask
web_app = Flask(__name__)

from app.services import routes

if __name__ == "__main__":
  web_app.run()