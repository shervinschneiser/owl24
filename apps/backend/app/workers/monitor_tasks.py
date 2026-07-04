from app.core.celery_app import celery_app


@celery_app.task(
    name="monitor.ping",
)
def ping() -> str:
    return "pong"