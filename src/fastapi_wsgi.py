from fastapi import FastAPI
from mangum import Mangum  # Optional if you need AWS-style handler

from main import app  # Your FastAPI app instance

# WSGI wrapper for PythonAnywhere
from starlette.middleware.wsgi import WSGIMiddleware
from flask import Flask

flask_app = Flask(__name__)
flask_app.wsgi_app = WSGIMiddleware(app)

application = flask_app
