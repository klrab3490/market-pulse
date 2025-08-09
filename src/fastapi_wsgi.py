from main import app
from fastapi.middleware.cors import CORSMiddleware
from fastapi_wsgi import ASGIProxy

application = ASGIProxy(app)
