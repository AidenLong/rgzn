"""
作业1 字符串反转，包含空格
    'i love   china!' --> 'china!   love i'
作业2 打印100以内的素数
作业3 自己实现一个方法，支持可变参数
作业3 自己实现函数解决hanoi塔问题
作业4 实现一个sort函数，通过参数指定比较函数用来实现不同顺序进行排序
"""


def revert(s):
    list1 = s.split(" ")
    tmp = ''
    for i in list1:
        if len(i) > 0:
            tmp += i[::-1]
            tmp += ' '
        else:
            tmp += ' '
    return tmp[-2::-1]


def su_shu(n):
    for i in range(2, n + 1):
        is_su_shu = True
        for j in range(2, int(i / 2 + 1)):
            if i % j == 0:
                is_su_shu = False
                break
        if is_su_shu:
            print(i, end='\t')


def func(*args, **kvs):
    print(args)
    print(kvs)


def hanoi(n, a, b, c):
    if n == 1:
        pass
        print(n, "   " + a + " --> " + b)
    else:
        hanoi(n - 1, a, c, b)
        print(n, "   " + a + " --> " + b)
        hanoi(n - 1, c, b, a)


def bubble_sort(data, cp=None):
    for i in range(len(data)):  # 外循环，每循环一次使得有序的数增加一个
        indicator = False  # 设置指示器，没有交换时表示array已经有序，用于结束循环
        for j in range(len(data) - 1 - i):  # 内循环，每循环一次将无须数中最大数提取
            if cp:
                cpFlag = cp(data[j], data[j + 1])
            else:
                cpFlag = data[j] > data[j + 1]

            if cpFlag:
                data[j], data[j + 1] = data[j + 1], data[j]
                indicator = True

        if not indicator:  # 没有交换时，结束循环
            break


def my_cp(i1, i2):
    if i1 < i2:
        return True
    else:
        return False


print(revert('i love   china!'))
su_shu(10)
func(*(1, 2, 3))
func(*(1, 2, 3), **({'name': '小明', 'sex': '男'}))
hanoi(4, 'A', 'B', 'C')
array = [1, 2, 5, 3, 4]
bubble_sort(array)
print(array)
bubble_sort(array, my_cp)
print(array)
