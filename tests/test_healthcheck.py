import unittest
import flask
from fibsum.services.health_check import HealthCheckService


class DefaultHealthCheckTest(unittest.TestCase):
    def setUp(self):
        self.app = flask.Flask(__name__)
        self.hc = HealthCheckService()
        self.client = self.app.test_client()

    def test_registry(self):
        pass
