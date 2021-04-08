import numpy as np
import pandas as pd

np.random.randn(2, 3)

# frame1: pd.DataFrame = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=["A", "B", "C"])
# frame2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=["X", "A", "B", "D"])
# print(frame1)
# print(frame1["b"].map(lambda x: x - 1))
# print(frame2)
# print(frame1.add(frame2, fill_value=0))

# chunker = pd.read_csv("/Users/a_kimura/workdir/pydata-book/examples/ex6.csv", chunksize=1000)
# tot = pd.DataFrame([], dtype="float64")
# for piece in chunker:
#     tot = tot.add(piece["key"].value_counts(), fill_value=0)
# print(tot[:100].to_parquet("./df.parquet"))

if __name__ == '__main__':
    frame = pd.DataFrame(
        np.arange(6).reshape(2, 3),
        index=pd.Index(["Ohio", "Colorado"], name="state", dtype=np.float64),
        columns=pd.Index(["one", "two", "three"], name="number", dtype=np.float64)
    )

    print(frame)
    print(frame.stack())
    print(frame.stack().unstack(0))

