quotes = {
    '第一鍵': '1',
    '第二鍵': '2',
    '第三鍵': '3',
}

# 拿取鍵值 >>> quotes['第一鍵']

for stooge in quotes:
    print(stooge)

from collections import OrderedDict
# 運用Tuple 以及 OrderedDict
quotes = OrderedDict([
    ('第一鍵', '1'),
    ('第二鍵', '2'),
    ('第三鍵', '3'),
    ])

for stooge in quotes:
    print(stooge)