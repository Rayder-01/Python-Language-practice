# 有些資料 (屬性) 與函式 (方法) 是類別本身的一部分
# 有些是類別所建立的物件的一部分

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

one_a = A()
two_a = A()
three_a = A()
A.kids()

# 靜態方法

class a():
    @staticmethod
    def commercail():
        print('this goods is sellout')
a.commercail()