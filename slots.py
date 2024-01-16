import random
import itertools
from collections import Counter

high_tier = ['a','b']
low_tier= ['c','d','e','f','g','h','i','j']
emotes = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j']
combinations = list(itertools.product(emotes, repeat=3))
result = random.choice(combinations)
amount = int(input('Enter the amount you want to gamble: '))

counter = Counter(result)

count_to_multiplier = {
   2: {'a': 25, 'b': 25},
   3: {'a': 50, 'b': 50}
}

for count, multipliers in count_to_multiplier.items():
   for emote, multiplier in multipliers.items():
       if counter[emote] == count:
           amount *= multiplier
for emote in low_tier:
   if counter[emote] == 2:
       amount *= 1.5

for emote in low_tier:
   if counter[emote] == 3:
       amount *= 2.5

if len(set(result)) == len(result):
   amount *= 0

print(result)
print("Amount after betting: ", amount)

