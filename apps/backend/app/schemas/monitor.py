from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl


class MonitorBase(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
    )

    url: HttpUrl

    interval: int = Field(
        ge=10,
        le=86400,
        default=60,
    )

    timeout: int = Field(
        ge=1,
        le=300,
        default=10,
    )

    is_active: bool = True


class MonitorCreate(MonitorBase):
    pass


class MonitorUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    url: HttpUrl | None = None

    interval: int | None = Field(
        default=None,
        ge=10,
        le=86400,
    )

    timeout: int | None = Field(
        default=None,
        ge=1,
        le=300,
    )

    is_active: bool | None = None


class MonitorResponse(MonitorBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime
