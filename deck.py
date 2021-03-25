from card import card
from Lib import random
class deck:
	def __init__(self):
		self.deck = []
		for i in range(13):
			self.deck.append(card("red","hearts",i+1))
		for i in range(13):
			self.deck.append(card("red","diamonds",i+1))
		for i in range(13):
			self.deck.append(card("black","clubs",i+1))
		for i in range(13):
			self.deck.append(card("black","spades",i+1))
		self.size = len(self.deck)
	def print_deck(self):
		for card in self.deck:
			print(card.to_string())

	def shuffle_deck(self):
		random.shuffle(self.deck)

	