from main import app  # Import your FastAPI app

# WSGI entry point
def application(scope, receive, send):
    import asyncio
    from asgiref.wsgi import WsgiToAsgi
    asgi_app = WsgiToAsgi(app)
    return asgi_app(scope, receive, send)
