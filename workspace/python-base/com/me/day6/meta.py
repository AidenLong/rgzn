def add(self, value):
    self.append(value)


class ListMetaClass(type):
    def __new__(cls, name, base, attrs):
        print(cls)
        print(name)
        attrs['add'] = lambda self, value: self.append(value)
        # attrs['add'] = add
        attrs['name'] = 'Tom'
        return type.__new__(cls, name, base, attrs)


class MyList(list, metaclass=ListMetaClass):
    pass


mli = MyList()
mli.add(1)
mli.add(2)
mli.add(3)
print(mli.name)
print(mli)
