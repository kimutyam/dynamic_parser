from typing import Generator, Iterable


# TODO Iteratorでもいけるの？ -> 多分いけないよ
def even_filter(nums: Iterable[int]) -> Generator[int, None, None]:
    for num in nums:
        if num % 2 == 0:
            yield num


if __name__ == "__main__":
    a = even_filter([1, 2, 3, 4])
    print(a)
    print(next(a))
    print(a)
