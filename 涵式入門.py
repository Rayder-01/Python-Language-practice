#涵式練習
# * - 串列
# ** - 字典

def doc_it(func):        
     def new_it(*ag1,**ag2): 
         print('func_name:',func.__name__)   
         print('position argument', ag1)   
         print('keyword argument', ag2)    
         result = func(*ag1, **ag2) 
         print('Result:', result)       
         return result              
     return new_it

def add_it(a,b):
    return a + b

new_add_it = doc_it(add_it)
new_add_it(3,5)

@doc_it
def add_it(a, b):
    return a + b
add_it(3,5)

