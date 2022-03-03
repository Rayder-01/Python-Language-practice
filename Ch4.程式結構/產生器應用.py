#　產生器 ( generator )
#  序列建立物件
#  可以迭代大數目

sum(range(1, 100))

#生產器函式
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number            #用yield的陳述式來回傳
        number += step

my_range

ranger = my_range(0, 10)
ranger

for x in ranger:
    print(x)
