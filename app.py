from flask import Flask, request
from flask_restful import Resource, Api
from functools import wraps
import google.auth.transport.requests
import google.oauth2.id_token

app = Flask(__name__)
api = Api(app)
HTTP_REQUEST = google.auth.transport.requests.Request()


def jwt_required_gcp(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        id_token = request.headers['Authorization'].split(' ').pop()
        claims = google.oauth2.id_token.verify_firebase_token(
            id_token, HTTP_REQUEST)
        if not claims:
            return 'Unauthorized', 401
        return fn(*args, **kwargs)
    return wrapper


class HelloWorld(Resource):
    @jwt_required_gcp
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
