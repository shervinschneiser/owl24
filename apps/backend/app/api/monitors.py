from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.monitor import MonitorCreate
from app.schemas.monitor import MonitorResponse
from app.schemas.monitor import MonitorUpdate
from app.services.monitor_service import MonitorService

router = APIRouter(
    prefix="/monitors",
    tags=["Monitors"],
)


@router.post(
    "",
    response_model=MonitorResponse,
    status_code=201,
)
def create_monitor(
    payload: MonitorCreate,
    db: Session = Depends(get_db),
):
    service = MonitorService(db)

    return service.create(payload)


@router.get(
    "",
    response_model=list[MonitorResponse],
)
def list_monitors(
    db: Session = Depends(get_db),
):
    service = MonitorService(db)

    return service.list()


@router.get(
    "/{monitor_id}",
    response_model=MonitorResponse,
)
def get_monitor(
    monitor_id: UUID,
    db: Session = Depends(get_db),
):
    service = MonitorService(db)

    monitor = service.get(monitor_id)

    if monitor is None:
        raise HTTPException(
            status_code=404,
            detail="Monitor not found",
        )

    return monitor


@router.put(
    "/{monitor_id}",
    response_model=MonitorResponse,
)
def update_monitor(
    monitor_id: UUID,
    payload: MonitorUpdate,
    db: Session = Depends(get_db),
):
    service = MonitorService(db)

    monitor = service.get(monitor_id)

    if monitor is None:
        raise HTTPException(
            status_code=404,
            detail="Monitor not found",
        )

    return service.update(
        monitor,
        payload,
    )


@router.delete(
    "/{monitor_id}",
    status_code=204,
)
def delete_monitor(
    monitor_id: UUID,
    db: Session = Depends(get_db),
):
    service = MonitorService(db)

    monitor = service.get(monitor_id)

    if monitor is None:
        raise HTTPException(
            status_code=404,
            detail="Monitor not found",
        )

    service.delete(monitor)
