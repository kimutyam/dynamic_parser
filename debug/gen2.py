from dataclasses import dataclass
from distutils.util import strtobool
from sqlite3.dbapi2 import Date
from typing import AnyStr, Callable, TypeVar, Union

T = TypeVar("T", str, int, bool)


@dataclass(frozen=True)
class ConvertError:
    """Convert Error"""

    # cause: Exception


def convert(value: str, f: Callable[[str], Union[T, ConvertError]]) -> Union[T, ConvertError]:
    try:
        return f(value)
    except ValueError:
        return ConvertError()


# Unionの片方の指定なので通る
convert("", lambda v: v)
convert("", lambda v: int(v))
# see https://qiita.com/kanae_y/items/03b1fda7dba07aa1819d
# bool()は存在しないときに__len__になるため
# return bool(strtobool(v))
# https://dev.classmethod.jp/articles/python-isinstance-or-type/
convert("", lambda v: strtobool(v) == 1)
