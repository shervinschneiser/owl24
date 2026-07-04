from app.core.celery_app import celery_app
from app.monitoring.checker import HTTPMonitorChecker


@celery_app.task(name="monitor.ping")
def ping() -> str:
    return "pong"


@celery_app.task(name="monitor.check")
def check_monitor(
    url: str,
    timeout: int = 10,
) -> dict:
    checker = HTTPMonitorChecker()

    return checker.check(
        url=url,
        timeout=timeout,
    )