from typing import Optional

from pampy import _, match

if __name__ == "__main__":
    x = ("fii", 1)

    # a = match(
    #     x,
    #     3, "this matches the number 3",
    #     int, "matches any integer",
    #     (str, int), lambda a, b: "a tuple (a, b) you can use in a function",
    #     [1, 2, _], "any dynamic_parser of 3 elements that begins with [1, 2]",
    #     {'x': _}, "any dict with a key 'x' and any value associated",
    #     _, "anything else"
    # )
    # print(a)
    #
    y: Optional[str] = "True"

    b = match(y, None, "none jan", bool, "boo", int, "ddd", _, y)
    print(b)
