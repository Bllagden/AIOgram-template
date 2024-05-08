import uuid
from decimal import Decimal
from typing import Annotated

from sqlalchemy import BigInteger, Integer, Numeric, String
from sqlalchemy.orm import mapped_column

uuid_pk = Annotated[
    uuid.UUID,
    mapped_column(primary_key=True, default=uuid.uuid4, default_factory=uuid.uuid4),
]
int32_pk = Annotated[
    int,
    mapped_column(
        Integer,
        primary_key=True,
    ),
]
int64_pk = Annotated[
    int,
    mapped_column(
        BigInteger,
        primary_key=True,
    ),
]

int64 = Annotated[int, mapped_column(BigInteger)]
numeric_10_2 = Annotated[Decimal, mapped_column(Numeric(precision=10, scale=2))]
numeric_10_3 = Annotated[Decimal, mapped_column(Numeric(precision=10, scale=3))]

str_3 = Annotated[str, mapped_column(String(3))]
str_16 = Annotated[str, mapped_column(String(16))]
str_32 = Annotated[str, mapped_column(String(32))]
str_64 = Annotated[str, mapped_column(String(64))]
str_128 = Annotated[str, mapped_column(String(128))]
str_256 = Annotated[str, mapped_column(String(256))]
str_320 = Annotated[str, mapped_column(String(320))]
str_1024 = Annotated[str, mapped_column(String(1024))]
str_2083 = Annotated[str, mapped_column(String(2083))]
