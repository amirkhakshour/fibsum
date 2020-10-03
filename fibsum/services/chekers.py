from .health_check import health_checker


@health_checker.register()
def dummy_checker():
    """Check dummy service."""
    return True, "OK"


@health_checker.register()
def dummy_checker_fails():
    """Check dummy service fails."""
    return False, "Failed"


@health_checker.register()
def check_db_available():
    """check if DB is available."""
    return True, "DB is OK"


@health_checker.register()
def check_redis_available():
    """Use redis client and check if connection to redis is successful."""
    return True, "Redis is OK"


@health_checker.register()
def check_external_api_one_available():
    """Check external API #1 connectivity!"""
    return False, "External API Failed!"
