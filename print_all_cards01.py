import random
from random import shuffle


def define_cards():
    rank_string = ("ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king")
    suit_string = ("clubs", "diamonds", "hearts", "spades")
    
    for suit in suit_string:  # you can obtain the items of the iterate list directly, no need of rank access
        for rank in rank_string:
            card_string = rank + " of " + suit
            yield card_string


#---Option 1-------------------------------
# this way will display list of cards in order
print ("The cards are:")
cards_iterator = define_cards()
cards = define_cards()
for i, card in enumerate(cards):  # use the iterator power ;)
    print (i, card)
#------------------------------------------
    
#---Option 2---------------------------------    
# this way will display the list of 52 numbers - shuffle way    
# cards = define_cards()
# i1 = [[i] for i, card in enumerate(cards)]
# shuffle(i1)
# print(i1)
#------------------------------------------
    
    
    
    
