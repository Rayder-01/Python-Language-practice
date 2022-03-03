# function 函式

def 表單(words, 函式):
    for 字 in words:
        print(函式(字))

字單 = ['哈','喔','恩','好']

def 生成(字):
    return 字.capitalize() + '!'

表單(字單, 生成)

#lambda用法
#小型函式

表單(字單, lambda 字: 字.capitalize() + '!')




