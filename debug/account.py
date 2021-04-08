from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Account:
    id: int
    name: str


@dataclass(frozen=True)
class Accounts:
    accounts: List[Account]

    def __contains__(self, item) -> bool:
        return item in self.accounts

    # @see https://stackoverflow.com/questions/44640479/mypy-annotation-for-classmethod-returning-instance
    @classmethod
    def create(cls) -> Accounts:
        return cls([Account(id=1, name="kimura")])
