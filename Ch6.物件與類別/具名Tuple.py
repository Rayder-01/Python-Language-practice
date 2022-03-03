from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orang','long')
duck
duck.bill
duck.tail

# 用字典製作Tuple
parts = {'bill': 'wide orang', 'tail': 'long'}
duck2 = Duck(**parts) # **parts 關鍵字引數 取出部分的字典鍵與值 
# >>> duck2
# Duck(bill='wide orang', tail='long')
# 效果相當於下方
duck2 = Duck(bill = 'wide orang', tail = 'long')

# Tuple 做更改
duck3 = duck2._replace(tail = 'a', bill = 'b')
duck3

# 將Duck 定義為字典
duck_dict = {'bill': 'wide orang', 'tail': 'long'}
duck_dict

# 將欄位加入字典
duck_dict = {'bill': 'wide orang', 'tail': 'long'}
duck_dict['color'] = 'green'

# 而不是加到具體Tuple
duck.color = 'green'

#    << Tuple 優點 >>
# 外觀 行為都像不可變物件
# 省空間 時間
# 句點標記法來取代字典方括號取屬性
# 可以當字典鍵來使用
