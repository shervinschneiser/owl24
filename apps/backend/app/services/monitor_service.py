from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.monitor import Monitor
from app.schemas.monitor import MonitorCreate
from app.schemas.monitor import MonitorUpdate


class MonitorService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: MonitorCreate) -> Monitor:
        monitor = Monitor(**data.model_dump())

        self.db.add(monitor)
        self.db.commit()
        self.db.refresh(monitor)

        return monitor

    def list(self) -> list[Monitor]:
        stmt = select(Monitor).order_by(Monitor.created_at.desc())

        return list(self.db.scalars(stmt).all())

    def get(self, monitor_id: UUID) -> Monitor | None:
        stmt = select(Monitor).where(Monitor.id == monitor_id)

        return self.db.scalar(stmt)

    def update(
        self,
        monitor: Monitor,
        data: MonitorUpdate,
    ) -> Monitor:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(monitor, key, value)

        self.db.commit()
        self.db.refresh(monitor)

        return monitor

    def delete(self, monitor: Monitor) -> None:
        self.db.delete(monitor)
        self.db.commit()
