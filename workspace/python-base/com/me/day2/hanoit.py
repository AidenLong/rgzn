def hanoi(n, A, B, C):
    if n == 1:
        pass
        print(n, "   " + A + " --> " + B)
    else:
        hanoi(n - 1, A, C, B)
        print(n, "   " + A + " --> " + B)
        hanoi(n - 1, C, B, A)


hanoi(4, 'A', 'B', 'C')
