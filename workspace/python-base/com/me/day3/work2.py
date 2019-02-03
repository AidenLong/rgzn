"""
3、矩阵转换：给定矩阵A，令矩阵B里每个元素B[i][j]的值等于A[0][0]到A[i][j]子矩阵元素的和
4、反转单向链表
    class ListNode
        def__init_(self, val;, next = None):
            self.val = val
            self.next = next
"""


def convert(source):
    ret = []
    rows = len(source)
    if rows == 0:
        return ret
    columns = len(source[0])
    x, y = 0, 0
    for i in range(rows):
        for j in range(columns):
            tmp = 0
            


convert([[1], [2]])
