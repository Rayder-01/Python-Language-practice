class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuoto(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer', "I am hunting wabbit")
print(hunter.who(), 'says:', hunter.says())
hunted1 = QuestionQuote('Bugs', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
hunted2 = ExclamationQuoto('Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

class a():
    def who(self):
        return 'brook'
    def says(self):
        return 'babble'
brook = a

def who_says(obj):
    print(obj.who, 'says', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)

# Duck Typing 來自古語:
# 如果她走路的樣子像鴨子,且叫聲像鴨子,那他就是隻鴨子
#                                           --俗語
