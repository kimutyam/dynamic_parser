import identify as identify
from pymonad.either import Either, Error, Left, Right
from pymonad.tools import curry, identity

if __name__ == "__main__":
    a: Either[str, int] = Right(10)
    b: Either[str, int] = Left("s")
    c: Either[str, int] = Right(20)

    @curry(2)
    def add(x: int, y: int) -> int:
        return x + y

    @curry(2)
    def div(y, x):
        if y == 0:
            return Left("Notting")
        else:
            return Right(x / y)

    print(add, add(2))

    z = a.bind(lambda aa: c.map(lambda bb: aa + bb))
    zz = Either.apply(add).to_arguments(a, c)

    zzz = Either.insert(10).then(div(4)).then(add(2)).then(div(4))

    print(z, zz, zzz)
