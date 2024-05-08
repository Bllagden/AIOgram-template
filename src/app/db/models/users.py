from datetime import datetime

from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column

from app.db import Base, int64, str_16, str_320, uuid_pk
from lib.utils import utc_now


class Users(MappedAsDataclass, Base, kw_only=True):
    __tablename__ = "users"

    id: Mapped[uuid_pk] = mapped_column(init=False)
    telegram_id: Mapped[int64]

    full_name: Mapped[str_320]
    email: Mapped[str_320]
    phone_number: Mapped[str_16] = mapped_column(unique=True)

    is_active: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default_factory=utc_now)
