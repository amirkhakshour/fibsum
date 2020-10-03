import time
from fibsum import config


class HealthCheckService:
    def __init__(self):
        self._registry = dict()
        self._cache = dict()

    def register(self):
        """
        Register a health check service.

        @todo add priority as parameter to order checker call.
        :param expires: ttl in seconds
        :return:
        """

        def wrapper(checker_service):
            self._registry[checker_service.__name__] = checker_service
            return checker_service

        return wrapper

    def check(self):
        results = []
        for checker_name, checker in self._registry.items():
            if checker in self._cache and self._cache[checker].get('expires') >= time.time():
                result = self._cache[checker]
            else:
                result = self.run_checker(checker)
                self._cache[checker] = result
            results.append(result)

        return results

    def run_checker(self, checker):
        passed, output = checker()
        timestamp = time.time()
        if passed:
            expires = timestamp + config.HEALTH_SUCCESS_TTL
        else:
            expires = timestamp + config.HEALTH_FAILED_TTL

        result = {
            'checker': checker.__name__,
            'output': output,
            'passed': passed,
            'timestamp': timestamp,
            'expires': expires,
        }
        return result


# default health checker service
health_checker = HealthCheckService()
