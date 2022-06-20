from flask import Flask

config = {
    "DEBUG" : True
}

app = Flask(__name__)
app.secret_key = "hello"

app.config.from_mapping(config)

from app import views