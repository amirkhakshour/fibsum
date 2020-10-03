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


# default health checker service
health_checker = HealthCheckService()
