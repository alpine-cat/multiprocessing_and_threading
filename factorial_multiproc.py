from multiprocessing import Pool
from time import time
import logging


def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


if __name__ == "__main__":
    logging.basicConfig(filename="factorial.log", level = logging.INFO, filemode="w")

    ns = [3, 5, 7]
    pool = Pool(processes=3)
    start = time()
    for n in ns:
        p = pool.apply_async(fact, [n])

    pool.close()
    pool.join()
    end = time()

    logging.info("Время выполнения: %s" % str(end-start))