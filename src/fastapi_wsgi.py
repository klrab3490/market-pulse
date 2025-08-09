# src/fastapi_wsgi.py
import os
import sys

# Ensure your project src is in the path
sys.path.append('/home/klrab7200/market-pulse/src')

from main import app  # Import your FastAPI app object

# WSGI entrypoint for PythonAnywhere
def application(scope, receive, send):
    return app(scope, receive, send)
