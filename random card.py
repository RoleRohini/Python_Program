
import random
card_points = ['A', 'K', 'Q', 'J', '2',
               '3', '4', '5', '6', '7', '8', '9', '10']

card_signs = ['Heart', 'CLUB', 'DIAMOND', 'SPADE']

randm_card = random.choice(card_points)

randm_sign = random.choice(card_signs)

rndm_crd = randm_card, randm_sign

print("The random card from a deck of cards = ", rndm_crd)