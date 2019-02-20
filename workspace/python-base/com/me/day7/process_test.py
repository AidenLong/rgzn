from multiprocessing import Process
import time


def f(n):
    time.sleep(n)
    print(n * n)


if __name__ == "__main__":
    for i in range(10):
        p = Process(target=f, args=[i, ])
        p.start()
