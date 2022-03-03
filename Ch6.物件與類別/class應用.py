class Animal():
    def __init__(self, name):
        self.name = name

def who(self):
    return self.name

a = Animal ("動物")

print(a.name) 

class Car():
    def new(self):
        print("呼叫: ex:1  Car:i am a car")

class Bike(Car): #繼承
    pass

a_car = Car()
a_bike = Bike()
a_car.new()
a_bike.new()

# 覆寫方法
# 更改 父類別的東西
class Car():
    def 呼叫(self):
        print("呼叫: ex:2  Car:i am a car")

class Bike(Car): #繼承
    def 呼叫(self):
        print("呼叫: ex:2  bike:i am not a car")
    def 顏色(self):  # <<添加方法>>
        print('顏色: ex:2 ','紅', '黃', '藍')
        

a_car = Car()
a_bike = Bike()
a_car.呼叫()
a_bike.呼叫()
#a_car.顏色() # <<添加方法 只有指定bike>> car無法
a_bike.顏色()

# 小應用

class Car():
    def __init__(self, carname):
        self.name = carname
class Size(Car):
    def __init__(self, size):
        self.name = "size:" + size
class Color(Car):
    def __init__(self, color):
        self.name ="color:" + color


車名 = Car('vovo')
尺寸 = Size('big')
顏色 = Color('black')
print(車名.name)
print(尺寸.name)
print(顏色.name)

# super 取得父類別的定義
class person():
    def __init__(self, name):
        self.name = name

class EmailPerson(person):
    def __init__(self, name, email): # 有 name 以及 email
        super().__init__(name)
        self.email =  email

bob = EmailPerson('Bob Frank', 'bob@gmail.com')

bob.name
bob.email



