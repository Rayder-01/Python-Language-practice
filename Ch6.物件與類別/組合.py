# 當你希望主類別的動作大多都像富類別一樣相同
# 繼承是很好的技術
# 但有時候組合 (composition) 或 聚合 (aggregation)

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('這隻鴨子有一個', self.bill.description,
         '尾巴還有一個', self.tail.length, 'tail')

tail = Tail('long')
bill = Bill('wide orang')
duck = Duck(bill, tail)
duck.about()


