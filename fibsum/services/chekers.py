from .health_check import health_checker


@health_checker.register()
def dummy_checker():
    """Check dummy service."""
    return True, "OK"


@health_checker.register()
def dummy_checker_fails():
    """Check dummy service fails."""
    return False, "Failed"
