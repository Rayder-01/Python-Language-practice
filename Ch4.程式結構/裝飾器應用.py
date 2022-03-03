def f1(name):
    return ":" + name

def f2(func):
    def f3(附加字串):
        return "姓名" + func(附加字串)
    return f3

f4 = f2(f1)
print(f4("John"))

# 經過裝飾器簡化
@f2
def f5(name):
    return ":" + name
def f2(func):
    def f3(數值):
        return "姓名" + func(數值)
    return f3

print(f5("Peter"))




def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional argument:', args)
        print('keyword argument:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
    return new_function

def add_ints(a, b):
    return a + b
add_ints(3, 5)

a_add_ints =document_it(add_ints)
a_add_ints(3, 8)

@document_it
def add_ints(a, b):
    return a + b
add_ints(1, 5)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a, b):
    return a + b
add_ints(1, 4)




