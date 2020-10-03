import unittest
import flask
from fibsum.services.health_check import HealthCheckService


class DefaultHealthCheckTest(unittest.TestCase):
    def setUp(self):
        self.app = flask.Flask(__name__)
        self.hc = HealthCheckService()
        self.client = self.app.test_client()

    def test_registry(self):
        @self.hc.register()
        def test_ok():
            return True, "OK"

        self.assertTrue(len(self.hc._registry.keys()) == 1)
        self.assertTrue(test_ok.__name__ in self.hc._registry)
        self.assertTrue(self.hc._registry[test_ok.__name__] == test_ok)