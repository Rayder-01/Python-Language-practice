letter = 'abcdefg'
letter[1]

name = 'Henny'
name[0] = 'P'  #錯誤方式

name = 'Henny'
name.replace('H','P')

'B' + name[1:]


# [:]
# [開始:]

letter = '123456789'
letter[:]      # 整串                        [:]
letter[7:]     # [開始:]                     [開始:]
letter[6:8]    # 從幾到幾                    [開始:結束]
letter[-2:]    # 到著數                   
letter[::2]    # 間隔數
letter[1:6:2]  # 從幾到幾 間隔多少
letter[4::2]   # 從幾到結束 間隔多少
letter[:8:2]   # 從開始到幾 間隔多少

# 用 len() 來取得長度

len(letter)

# 用 split() 來分割

number = '1,2,3,4,5,6,7,8,9'
number.split(',')

number.split()

# 用 join() 來加入

a_list = ['1','2','3','4','5']
crypto_string = ','.join(a_list)
print('number:',a_list)

