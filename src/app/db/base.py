import datetime
import enum

from sqlalchemy import DateTime, Enum, Interval, Time
from sqlalchemy.orm import DeclarativeBase, registry


class Base(DeclarativeBase):

    registry = registry(
        type_annotation_map={
            datetime.datetime: DateTime(timezone=True),
            enum.Enum: Enum(native_enum=False),
            datetime.time: Time,
            datetime.timedelta: Interval,
        },
    )
