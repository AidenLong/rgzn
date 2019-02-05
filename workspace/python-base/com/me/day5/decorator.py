def hello(fn):
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)

    return wrapper


@hello
def foo():
    print("i am foo")


foo()


def make_html_tag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
            if "css_class" in kwds else ""

        def wrapped(*args, **kwds):
            return "<" + tag + css_class + ">" + fn(*args, **kwds) + "</" + tag + ">"

        return wrapped

    return real_decorator


@make_html_tag(tag="b", css_class="bold_css")
@make_html_tag(tag="i", css_class="italic_css")
def hello():
    return "hello world"


print(hello())


# 使用class 的形式
class makeHtmlTagClass(object):

    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
            if css_class != "" else ""

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class + ">" \
                   + fn(*args, **kwargs) + "</" + self._tag + ">"

        return wrapped


@makeHtmlTagClass(tag="b", css_class="bold_css")
@makeHtmlTagClass(tag="i", css_class="italic_css")
def hello(name):
    return "Hello, {}".format(name)


print(hello("Baby"))

'''
装饰器的副作用：
因为decorator的因素，我们原本的函数其实已经变成了一个叫wrapper函数。
比如，你再调用__name__的时候，他会告诉你，这是 wrapper, 而不是 foo 或者 hello。
'''
from functools import wraps


def hello(fn):
    @wraps(fn)
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)

    return wrapper


@hello
def foo():
    '''foo help doc'''
    print("i am foo")
    pass


foo()
print(foo.__name__)
print(foo.__doc__)
