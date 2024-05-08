from datetime import UTC, date, datetime, time, timedelta
from typing import TypeVar

T = TypeVar("T")


def utc_now() -> datetime:
    return datetime.now(tz=UTC)


def replace_time(
    datetime_field: datetime | None = None,
    *,
    time_: time,
) -> datetime | None:
    if datetime_field is None:
        return None

    return datetime_field.replace(
        hour=time_.hour,
        minute=time_.minute,
        second=time_.second,
        microsecond=time_.microsecond,
    )


def represent_date(value: datetime | date) -> str:
    return value.strftime("%d.%m.%Y")


def represent_time(value: datetime, delta: timedelta | None = None) -> str:
    if delta:
        value = value + delta
    return value.strftime("%H:%M")
