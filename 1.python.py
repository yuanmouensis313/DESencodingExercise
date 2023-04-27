import timeit
import numpy as np
if __name__ == "__main__":
    def sum1():
        arr = np.random.rand(10000)
        sum(arr)

    def sum2():
        arr = np.random.rand(10000)
        np.sum(arr)

    result = timeit.timeit(sum1, number=1000)
    print(result)
    result = timeit.timeit(sum2, number=1000)
    print(result)