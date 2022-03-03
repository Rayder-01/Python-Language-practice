class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

one = Word('I am')
two = Word('i am')
three = Word('a')

one.equals(two)
one.equals(three)

# 改為特殊名稱

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
# 運用其他特殊方法
#  __str__() __reper__()
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'word("' + self.text + '")'

one = Word('ha')
one        # use __repr__
print(one) # use __str__

