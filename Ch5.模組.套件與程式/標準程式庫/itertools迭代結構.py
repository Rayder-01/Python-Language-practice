import itertools
for item in itertools.chain([1, 2], ['a' ,'b']):
    print(item)

# cycle 無限迭代器
for item in itertools.cycle([1, 2]):
    print(item)

# accumulate
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item) 
    