class MyClass:
    def __call__(self, *args, **kwargs):
        print('you can call cla() directly.')


cls = MyClass()
cls()

print(callable(cls))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))
