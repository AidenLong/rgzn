"""
1、给定一个m * n要素的矩阵。按照螺旋顺序，返回该矩阵的所有要素
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
     应该返回[1, 2, 3, 6, 9, 8, 7, 4, 5]

2、用栈（使用list）实现队列：支持push(element),pop()和top()方法。pop和top方法都应该返回第一个元素。比如执行以下操作序列;push(1),
    pop(),push(2),push(3),top(),pop(),应该返回1,3和2。
"""


def spiral_order(matrix):
    ret = []
    rows = len(matrix)
    if rows == 0:
        return ret
    columns = len(matrix[0])
    x, y = 0, 0  # 方阵的左上角坐标
    while (rows > 0) and (columns > 0):
        for k in range(y, y + columns):  # 第一行
            ret.append(matrix[x][k])
        if rows > 1:  # 行数大于1
            for k in range(x + 1, x + rows):  # 最右列
                ret.append(matrix[k][y + columns - 1])
            if columns > 1:  # 列数大于1
                for k in range(y + columns - 2, y - 1, -1):  # 最下行
                    ret.append(matrix[x + rows - 1][k])
                for k in range(x + rows - 2, x, -1):  # 最左列
                    ret.append(matrix[k][y])
        rows -= 2
        columns -= 2
        x += 1
        y += 1
    return ret


list_queue = []


def push(e):
    global list_queue
    tmp = []
    if len(list_queue) == 0:
        tmp.append(e)
    else:
        revers = list_queue[::-1]
        revers.append(e)
        tmp.extend(revers)
    list_queue = tmp[::-1]


def pop():
    global list_queue
    e = list_queue[0]
    list_queue.remove(e)
    return e


def top():
    return pop()


print(spiral_order([]))
print(spiral_order([[1]]))
print(spiral_order([[1, 2], [3, 4]]))
print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral_order([[1, 2, 3, 'a'], [4, 5, 6, 'b'], [7, 8, 9, 'c']]))

push(1)
print(pop())
push(2)
push(3)
print(top())
print(pop())
