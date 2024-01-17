import random
import itertools
from collections import Counter
high_tier = ['a','b']
low_tier= ['c','d','e','f','g','h','i','j']
emotes = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j']
combinations = list(itertools.product(emotes, repeat=3))
result = random.choice(combinations)  
amount = int(input('Place your bet: '))
counter = Counter(result)
if len(set(result)) == len(result):
   amount *= 0
for emote, count in counter.items():
    if emote in high_tier:
        if count == 2:
            amount *= 25
        elif count == 3:
            amount *= 50
    else:
        if count == 2:
            amount *= 1.5
        elif count == 3:
            amount *= 2.5
print("After spinning the wheel you've got: ",dict(counter))
print('Amount after betting: ', amount)
