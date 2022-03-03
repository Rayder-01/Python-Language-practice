# deque (唸 deck ) 雙頭序列　有 堆疊 +　序列　的功能
# 當想要從任何一端 加入 或 刪除
# popleft() 將 deque 最 左邊 的項目移除並回傳
# pop() 將最 右邊 的項目移除並回傳

def 回文(字):
    from collections import deque
    dq = deque(字)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True

# 回文檢查器 slice型式
def slice_回文(字):
    return 字 == 字[::-1]

    