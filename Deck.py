#Deck
class Deck:
	# '''Definition of a card deck.'''

	def __init__(self,hasJoker=False):
		self.suits  = ['H','D','S','C']
		self.values = [str(x) for x in range(2,11)] #2-10 cards
		self.values.extend(['J','Q','K','A']) #Face cards
		#Assemble deck
		self.cards = [(v+s) for v in self.values for s in self.suits]
		#Add Joker cards (2) as 'W' if needed
		if(hasJoker):
			self.cards.extend(['W1','W2'])
