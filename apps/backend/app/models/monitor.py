from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class MonitorType(str, Enum):
    HTTP = "http"


class Monitor(BaseModel):
    __tablename__ = "monitors"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String(2048),
        nullable=False,
    )

    monitor_type: Mapped[MonitorType] = mapped_column(
        SqlEnum(MonitorType, name="monitor_type"),
        nullable=False,
        default=MonitorType.HTTP,
    )

    interval: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=60,
    )

    timeout: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=10,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )