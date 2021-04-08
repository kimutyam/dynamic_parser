from typing import Collection, Optional, TypeVar

T = TypeVar("T")


# TODO Tの境界を考える
def head_option(c: Collection[T]) -> Optional[T]:
    if c:
        head, *_ = c
        return head
    else:
        return None
