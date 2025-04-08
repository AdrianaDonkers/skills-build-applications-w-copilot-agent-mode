import logging

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logging.debug(f"Incoming request: {request.method} {request.path}")
        response = self.get_response(request)
        logging.debug(f"Response status: {response.status_code}")
        logging.debug(f"Response headers: {response.headers}")
        return response

class CorsForceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logging.debug(f"CorsForceMiddleware applied to request: {request.method} {request.path}")
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        logging.debug(f"CORS headers added: {response.headers}")
        return response