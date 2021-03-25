from deck import deck
from card import card
from field import field
test = card("red", "hearts", 10)
deck = deck()
print(test.colour)
print(deck.deck[0].suite)

deck.print_deck()
deck.shuffle_deck()
print("PRINTING NEW SHUFFLED DECK")
deck.print_deck()
print(deck.size)


field = field(deck)

print("STACK 1")
field.print_stack(0)
print("STACK 2")
field.print_stack(1)
print("STACK 3")
field.print_stack(2)
print("STACK 4")
field.print_stack(3)
print("STACK 5")
field.print_stack(4)
print("STACK 6")
field.print_stack(5)
print("STACK 7")
field.print_stack(6)

field.print_field()

moves = field.compute_moves()


command = input()
window = len(field.rem_deck)
ace_count = 0
while(command != "Q" and command != "q"):
	command_num = None
	found_card = False
	if(command.isnumeric()):
		command_num = int(command)
	move_card = []
	if(command_num is not None):
		for card1, card2 in moves[command_num].items():
			if(isinstance(card2,card) and isinstance(card1, card)):
				print(card1.to_string(), card2.to_string())
				move_card.append(card1)
				move_card.append(card2)
			else:
				move_card.append(card1)
				move_card.append(card2)

		for i in field.stacks:
			if(move_card[0] in field.stacks[i]):
				print('FOUND CARD IN STACK: ' + str(i + 1))
				found_card = True
				move_point = field.stacks[i].index(move_card[0])
				cards = field.stacks[i][move_point:]
				del field.stacks[i][move_point:]
				#card1 = field.stacks[i].pop(field.stacks[i].index(card1))
				#print('popped ' + card1.to_string())
				for j in field.stacks:
					if(move_card[1] in field.stacks[j]):
						field.stacks[j].extend(cards)
					elif(j == move_card[1]):
						field.stacks[move_card[1]].extend(cards)

				if(move_card[1] == -1):
					if(move_card[0].value == 1):
						field.home[ace_count].extend(cards)
						ace_count += 1
						
						#print('ADDED ' + card1.to_string() + ' TO STACK ' + str(j + 1))
					else:
						for x in field.home:
							if(len(field.home[x]) > 0):
								if(field.home[x][-1].suite == cards[0].suite):
									field.home[x].extend(cards)
		if(found_card == False):
			move_point = field.rem_deck.index(move_card[0])
			print("move point: " + str(move_point))
			#if(move_point - 2 >= 0):
			for x in field.rem_deck:
				print(x.to_string(), end=' ')

			print()
			if(move_point + 3 < len(field.rem_deck)):
				field.rem_deck[move_point + 3].isHidden = False
			del field.rem_deck[move_point]
			#field.rem_deck[move_point - 2].isHidden = False
			for x in field.rem_deck:
				print(x.to_string(), end=' ')

			print()
			if(move_card[1] == -1):
				if(move_card[0].value == 1):
					field.home[ace_count].extend(move_card[0:1])
					ace_count += 1
				else:
					for x in field.home:
						if(len(field.home[x]) > 0):
							if(field.home[x][-1].suite == move_card[0].suite):
								field.home[x].extend(move_card[0:1])
			else:
				for j in field.stacks:
					if(move_card[1] in field.stacks[j]):
						field.stacks[j].append(move_card[0])
					elif(j == move_card[1]):
						print("Should enter here; " + move_card[0].to_string() + " to stack: " + str(j))
						field.stacks[move_card[1]].extend(move_card[0:1])
						print('we should get a card here: ')
						#print(field.stacks[move_card[1]][0])
	elif(command == 'c' or command == 'C'):
		field.cycle_remaining(window)					
		window-=3
		if(window < 0):
			window = len(field.rem_deck)
	field.print_field()
	moves = field.compute_moves()
	command = input()