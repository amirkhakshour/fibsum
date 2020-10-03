import time
import socket
from flask_restful import Resource
from functools import reduce
from fibsum.services.chekers import health_checker


def checker_response_message(results, passed=True):
    return {
        'hostname': socket.gethostname(),
        'status': 'success' if passed else 'failure',
        'timestamp': time.time(),
        'results': results,
    }


class HealthCheckResource(Resource):
    """
    Provides health check functionality to monitor your application.
    """
    CHECK_SUCCESS_HTTP_STATUS = 200
    CHECK_FAILED_HTTP_STATUS = 500
    checker = health_checker

    def _check_reduce(self, passed, result):
        return passed and result.get('passed')

    def get(self):
        results = self.checker.check()
        passed = reduce(self._check_reduce, results, True)
        message = checker_response_message(results, passed)
        if passed:
            return message, self.CHECK_SUCCESS_HTTP_STATUS
        else:
            return message, self.CHECK_FAILED_HTTP_STATUS
