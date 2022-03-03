from collections import Counter
早餐 = ['吐司', '吐司', '蛋', '吐司']
早餐_counter = Counter(早餐)
早餐_counter

# most_common
早餐_counter.most_common() # 以降冪回傳所有元素
早餐_counter.most_common(1)

中餐 = ['蛋', '蛋', '培根']
中餐_counter = Counter(中餐)
早餐_counter + 中餐_counter
早餐_counter - 中餐_counter
早餐_counter & 中餐_counter #交集
早餐_counter | 中餐_counter #聯集


