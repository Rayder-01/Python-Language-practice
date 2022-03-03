字典 = {'第一鍵': 1, '第二鍵': 2}
新物件 = 字典.setdefault('新物件', 3) # setdefault() 函式就像get()
print(新物件)
print(字典)

#指派已經存在的鍵他會回傳原本的值，不會改變

第一鍵 = 字典.setdefault('第一鍵' ,  3) # 試著將字典裡的第一鍵更改為3
第一鍵                                 # 結果無法更改 回傳原有的值

# defaultdict
# 字典被建立時,為任何新鍵指定預設值,並回傳引數式個函式
from collections import defaultdict
字典 = defaultdict(int) # 可使用 int() dict() lsit()
字典['一'] = 1 
字典['二']
# 回傳 0
# >>> 字典
# defaultdict(<class 'int'>, {'一': 1, '二': 0})


def no_idea():
     return 'Huh?'
     
表格 = defaultdict(no_idea)
表格['A'] = 'a'   
表格['B']

#  >>> 表格['B']  
#  'Huh?'
#回傳進沒有的值


# lambda 應用
表格 = defaultdict(lambda: 'Huh?')
表格['C']

# 
食物計數器 = defaultdict(int)
for 食物 in ['spam', 'spam', 'egg', 'spam']:
     食物計數器[食物] += 1

for 食物, 計數器 in 食物計數器.items():
     print(食物, 計數器)

# 如果食物計數器是一般的字典,當我們試著遞增字典元素,
# 食物計數器[食物] 都會發生例外,因為他尚未被初始化
# 以下示範

dict_食物計數器 = {}
for 食物物件 in ['spam', 'spam', 'egg', 'spam']:
     if not 食物 in dict_食物計數器:
          dict_食物計數器[食物物件] = 0
     dict_食物計數器[食物物件] += 1

for 食物, 計數器 in dict_食物計數器.items():
     print(食物, 計數器)