
from typing import Counter


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name 
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fow1 = Duck('Howard')
fow1.name
fow1.get_name()
fow1.name = 'Daffy'
fow1.name
fow1.set_name('MiMi')

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name 
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    
fow1 = Duck('vovo')
fow1.name
fow1.name = 'Donald'
fow1.name

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
c.radius
c.diameter
c.radius = 7     # 可以更改值
c.diameter
#c.diameter = 7     這是不行的

# 搞砸私用名稱
# 將hidden 改為 __name
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


#　簡單範例　：互動案例-存款與取款
class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0
        
    def deposit(self, amount):  #存款動作: amount代表存入金額
        if amount <= 0:
            raise ValueError('must be positive')
        self.balance += amount
        
    def withdraw(self, amount): #取款動作: amount代表取款金額
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('balance not enough')

acct1 = Account('123–456–789', 'Justin') #開一個帳戶
acct1.deposit(100)
acct1.withdraw(50)
print(acct1.balance) #餘額是 70