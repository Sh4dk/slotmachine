import random
from collections import Counter

emotes = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j']
amount = 5000
print('You start this game with 5000 points')
print('------------------------------------')
high_tier = {'a','b'}
low_tier= {'c','d','e','f','g','h','i','j'}

while amount > 0:
    bet = int(input('Place your bet: '))
    if bet <= amount:
        result = random.choices(emotes, k=3)
        counter = Counter(result)
        if len(set(result)) == len(result):
            amount -= bet
            bet *= 0
        for idx, (emote, count) in enumerate(counter.items()):
            if emote in high_tier:
                if count == 2:
                    bet *= 25
                    amount += bet
                elif count == 3:
                    bet *= 50
                    amount += bet
            else:
                if count == 2:
                    bet *= 1.50
                    amount += bet
                elif count == 3:
                    bet *= 2.5
                    amount += bet
        print("After pulling the lever you've got: ", dict(counter))
        print("You win: ",bet,'points')
        print('Your total points: ', amount)
        print('----------------------------')
    else:
        print('You dont have', bet, 'points')
    
