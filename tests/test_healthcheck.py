import unittest
from unittest import mock
import flask
from fibsum.app import create_app
from fibsum.services.health_check import HealthCheckService
from fibsum.api.resources.system import HealthCheckResource


class DefaultHealthCheckTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.path = "/api/v1/health"  # @todo get from settings
        self.hc = HealthCheckService()
        self.client = self.app.test_client()

    def test_registry(self):
        @self.hc.register()
        def test_ok():
            return True, "OK"

        self.assertTrue(len(self.hc._registry.keys()) == 1)
        self.assertTrue(test_ok.__name__ in self.hc._registry)
        self.assertTrue(self.hc._registry[test_ok.__name__] == test_ok)

    def test_check_runs_checkers(self):
        test_ok = mock.Mock(return_value=(True, "OK"))
        test_ok.__name__ = 'test_ok'
        self.hc.register()(test_ok)
        self.hc.check()
        test_ok.assert_called_once()

    def test_endpoint_200_response_code(self):
        success_message = "dummy success message"

        @self.hc.register()
        def test_ok():
            return True, success_message

        with mock.patch.object(HealthCheckResource, 'checker', self.hc):
            response = self.client.get(self.path)
            self.assertEqual(200, response.status_code)
            jr = flask.json.loads(response.data)
            self.assertEqual(success_message, jr['results'][0]["output"])

    def test_endpoint_500_response_code(self):
        fail_message = "dummy failed message"

        @self.hc.register()
        def test_fails():
            return False, fail_message

        with mock.patch.object(HealthCheckResource, 'checker', self.hc):
            response = self.client.get(self.path)
            self.assertEqual(500, response.status_code)
            jr = flask.json.loads(response.data)
            self.assertEqual(fail_message, jr['results'][0]["output"])
