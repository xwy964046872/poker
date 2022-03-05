import copy

card_type = {
    'High card':0,
    'Pair':1,
    'Two pairs':2,
    'Three of a kind':3,
    'Straight':4,
    'Flush':5,
    'Full house':6,
    'Four of a kind':7,
    'Straight flush':8,
    'Royal flush':9
}




hand_card = [[['♦', 'A']], [['♦', '10']]]

table_card = [[['♦', '9']], [['♥', '10']], [['♠', '10']], [['♠', '9']]]#, [['♣', '5']]]

comb_card = copy.deepcopy(table_card)

# print(type(card_type))

# print(card_type['High card'])

# test = 'High card'
#
# print(card_type[test])


for i in hand_card:
    comb_card.append(i)

print(comb_card)
print(len(comb_card))




