class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print('print will call __str__ first')
        return 'hello ' + self.name + '!'


print(MyClass('Tom'))
