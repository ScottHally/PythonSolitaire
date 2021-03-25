class field:
	size = 28
	def __init__(self, deck):
		self.stacks = {}
		self.stacks[0] = deck.deck[:1]
		self.stacks[0][-1].isHidden = False
		self.stacks[1] = deck.deck[1:3]
		self.stacks[1][-1].isHidden = False
		#stack 3, 3 cards
		self.stacks[2] = deck.deck[3:6]
		self.stacks[2][-1].isHidden = False
		#STACK 4, cards 6 to 10, 4 cards
		self.stacks[3] = deck.deck[6:10]
		self.stacks[3][-1].isHidden = False
		#stack 5, cards 10 to 16
		self.stacks[4] = deck.deck[10:15]
		self.stacks[4][-1].isHidden = False
		#stack 6, 6 cards
		self.stacks[5] = deck.deck[15:21]
		self.stacks[5][-1].isHidden = False
		#stack 7, 7 cards
		self.stacks[6] = deck.deck[21:28]
		self.stacks[6][-1].isHidden = False

		self.rem_deck = deck.deck[28:]
		self.home = {}
		self.home[0] = []
		self.home[1] = []
		self.home[2] = []
		self.home[3] = []
	def print_stack(self, index):
		for card in self.stacks[index]:
			print(card.to_string())

	# may need to change this for dymanics
	def print_field(self):
		print('[ ', end='')
		for x in self.home:
			if(len(self.home[x]) > 0):
				print(self.home[x][-1].to_string(), end=' ')
		print(']')

		for i in range(20):
			for j in range(7):
				if(i < len(self.stacks[j])):
					last = len(self.stacks[j]) - 1
					if(last == i):
						if(self.stacks[j][i].isHidden == True):
							self.stacks[j][i].isHidden = False
					print(self.stacks[j][i].to_string(), end='\t')
				else:
					print('\t', end='')
			print()

		print("Remaining cards: [ ", end='')
		chunk = self.get_window()
		#print(chunk)
		for card1 in chunk:
			print(card1.to_string() + ' ', end='')
		print(']')

	def compute_moves(self):
		moves = []
		valid_moves = {}
		move_count = 0
		move_table = []
		empties = []
		exists = False
		ace_exists = False
		#for i in self.stacks:
		#	if(len(self.stacks[i]) != 0):
		#		for card in self.stacks[i]:
		#			if(card.isHidden == False):
		#				moves.append(card)

		#for i in range(7):
		#	for j in range(7):

		#	for card in self.stacks[i]:
		#		for card2 in self.stacks[i]:
		#			if(card.isHidden == False and card2.isHidden == False):
		#				if(card.value == card2.value -1):
		#					if(card.colour != card2.colour):
		#						valid_moves[move_count] = card.to_string() + ' to ' + card2.to_string()
		#						move_table.append(dict([(card, card2)]))
		#						move_count += 1
		for i in range(7):
			if(len(self.stacks[i]) == 0):
				empties.append(i)
			else:
				last_card = self.stacks[i][-1]
				#print('last card is:   ' + last_card.to_string())
			for card in self.stacks[i]:
				#print("screwy card:. ... " + card.to_string())
				exists = False
				ace_exists = False
				found_spot = False
				for j in range(7):
					for card2 in self.stacks[j]:
						last = self.stacks[j][-1]
						if(i != j and card.isHidden == False and card2.isHidden == False):
							if(card.value == card2.value -1 and card2 == last and card.value > 1):
								if(card.colour != card2.colour):
									valid_moves[move_count] = card.to_string() + ' to ' + card2.to_string()
									move_table.append(dict([(card, card2)]))
									move_count += 1
							elif(card.value == 13 and len(empties) > 0):
								for k in empties:
									for table in move_table:
										if(card in table):
											exists = True
									if(exists == False):
										valid_moves[move_count] = card.to_string() + ' to empty space ' + str(k)
										move_table.append(dict([(card, k)]))
										move_count += 1
							elif(card.value == 1 and ace_exists == False):
								ace_exists = True
								valid_moves[move_count] = card.to_string() + ' to home'
								move_table.append(dict([(card, -1)]))
								move_count+=1
							#else:
							
				for x in self.home:
					if(len(self.home[x]) > 0):
						if(found_spot == False):
							if(card.value == self.home[x][-1].value + 1 and card.suite == self.home[x][-1].suite and card == last_card):
								valid_moves[move_count] = card.to_string() + ' to home'
								move_table.append(dict([(card, -1)]))
								move_count+=1
								found_spot = True
#fucking use version  control, dude

		
		#for i in range(13):
		#	for j in range(7):
		#		card = self.stacks[j][i]
		#		if(moves[i].value == moves[j].value - 1):
		#			if(moves[i].colour != moves[j].colour):
		#				valid_moves[move_count] = moves[i].to_string() + ' to ' + moves[j].to_string()
		#				move_table.append(dict([(moves[i], moves[j])]))
		#				move_count += 1
		chunk = self.get_window()
		#for card in chunk:
		if(len(chunk) > 0):
			card = chunk[-1]
			if(card.value == 1):
				valid_moves[move_count] = card.to_string() + ' to home'
				move_table.append(dict([(card, -1)]))
				move_count+=1
			elif(card.isHidden == False):
				for i in range(7):
					if(len(self.stacks[i]) != 0):
						last_card = self.stacks[i][-1]
						if(card.colour != last_card.colour):
							if(card.value == last_card.value - 1 and card.value > 1):
								valid_moves[move_count] = card.to_string() + ' to ' + last_card.to_string()
								move_table.append(dict([(card, last_card)]))
								move_count += 1
					else:
						if(card.value == 13):
							valid_moves[move_count] = card.to_string() + ' to empty space ' + str(i)
							move_table.append(dict([(card, i)]))
							move_count += 1
				
				for x in self.home:
					if(len(self.home[x]) > 0):
						if(self.home[x][-1].suite == card.suite and card.value == self.home[x][-1].value + 1):
							valid_moves[move_count] = card.to_string() + ' to home'
							move_table.append(dict([(card, -1)]))
							move_count+=1
		for num, move in valid_moves.items():
			print(f'{num:3} : {move}')

		print('C/c : cycle remaining cards')
		return move_table

	def cycle_remaining(self,window):
		print('window is:   ' + str(window));
		print('window - 3 is:   ' + str(window-3))
		if(window == 1):
			chunk = self.rem_deck[window - 1: window + 2]
		elif(window == 2):
			chunk = self.rem_deck[window - 2: window + 1]
		else:
			chunk = self.rem_deck[window-3:window]
		print("PRINTING CHUNK")
		for card in chunk:
			card.isHidden = False
			print(card.to_string())

		print('PRINTING INVERSE OF CHUNK')
		inverse = list(set(self.rem_deck) - set(chunk))
		for card in inverse:
			card.isHidden = True
			print(card.to_string())
		

	def get_window(self):
		allHidden = True
		chunk = []
		for card in self.rem_deck:
			if(card.isHidden == False and allHidden == True):
				pos = self.rem_deck.index(card)
				allHidden = False
				chunk = self.rem_deck[pos:pos+3]

		if(allHidden == True):
			chunk = self.rem_deck[0:0]
		chunk.reverse()
		return chunk