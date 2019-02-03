class People:
    def __init__(self, name):
        self.__name = name

    def hello(self, name):
        print('you are', self.__name)
        print('i am ', name)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Man(People):
    def detail(self, info):
        print(self.get_name(), ' say ：', info)


obj = People('222')
obj.hello('112')
obj.set_name('333')
obj.hello('112')

man = Man('super man')
man.detail('i want you')

print(dir(man))
