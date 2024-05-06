from typing import TypeVar

_T = TypeVar("_T")


def getval(value: _T | None) -> _T:
    """
    Return value if value is not None.

    Raised:
        - `ValueError`
    """
    if value is None:
        raise ValueError
    return value
