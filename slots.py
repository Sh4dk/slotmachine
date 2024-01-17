import random
from collections import Counter

emotes = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j']
result = random.choices(emotes, k=3)
amount = int(input('Place your bet: '))
counter = Counter(result)

high_tier = {'a','b'}
low_tier= {'c','d','e','f','g','h','i','j'}

if len(set(result)) == len(result):
   amount *= 0
for idx, (emote, count) in enumerate(counter.items()):
   if emote in high_tier:
       if count == 2:
           amount *= 25
       elif count == 3:
           amount *= 50
   else:
       if count == 2:
           amount *= 1.50
       elif count == 3:
           amount *= 2.5

print("After spinning the wheel you've got: ", dict(counter))
print('Amount after betting: ', amount)

