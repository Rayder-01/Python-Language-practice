from sources import daily,weekly

print("Daily forecase", daily.forecase())
print("weekly forecase:")
for number, outlook in enumerate(weekly.forecase(),1):
    print(number, outlook)
