import pytest
import unittest
import jwt
from http import HTTPStatus
from unittest import mock
from flask import url_for, Flask


def create_app():
    # Remove any existing pyjwt handlers, as firebase_helper will register
    # its own.
    try:
        jwt.unregister_algorithm('RS256')
    except KeyError:
        pass

    import app
    app.app.testing = True
    return app.app


class TestHealthCheck(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def mock_token(self):
        patch = mock.patch('google.oauth2.id_token.verify_firebase_token')
        with patch as mock_verify:
            yield mock_verify

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def test_response_with_token(self):
        response = self.client.get('/',  headers={'Authorization': 'Bearer 123'})
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual({'hello': 'world'}, response.json)

    def test_response_without_token(self):
        response = self.client.get('/')
        self.assertEqual(HTTPStatus.UNAUTHORIZED, response.status_code)
