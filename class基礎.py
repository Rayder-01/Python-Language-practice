# 物件內的 屬性( ttribute ) 及 方法( method )
class Object:
    def method1(self, value):
        self.attribute = value
a = Object()
a.method1("1")
print(a.attribute)

# __init__
class Object2:
    def __init__(self, i):
        self.i = i
    def methon2(self):
        print("word", self.i)

b = Object2(2)
b.methon2()

# __str__
class Object3():
    pass

c = Object3()
print(c)

class Object4():
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return str(self.i)
d = Object4(4)
print(d)


#第一種

class Student:

    def __init__(self):#兩者之間的區別

        self.name = None

        self.score = None
##第二種

    def __init__(self, name, score):

        self.name = name

        self.score = score

# student = Student("sansan", 90)

student = Student()

student.name= "sansan"

student.score = 90

# susan = Student("sunny", 78)

susan = Student()

susan.name = "susan"

susan.score = 78