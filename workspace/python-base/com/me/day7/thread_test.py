from threading import Thread
import time


def my_counter():
    i = 0
    for j in range(10000000):
        i = i + 1
        return True


# 串行执行两个线程
def main1():
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))


# 并行执行两个线程
def main2():
    thread_arr = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_arr[tid] = t
    for i in range(len(thread_arr)):
        thread_arr[i].join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))


if __name__ == '__main__':
    main1()
    main2()
