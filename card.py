class card:

	def __init__(self,colour,suite,value, isHidden):
		self.colour = colour
		self.suite = suite
		self.value = value
		self.isHidden = isHidden

	def to_string(self):
		num = self.value
		s = self.suite[0]

		if(s == 's'):
			s = '\u2660'
		elif(s == 'h'):
			s = '\u2661'
		elif(s == 'd'):
			s = '\u2662'
		else:
			s = '\u2663'

		if(num == 1):
			num = 'A'
		elif(num == 11):
			num = 'J'
		elif(num == 12):
			num = 'Q'
		elif(num == 13):
			num = 'K'

		if(self.isHidden):
			num = '*'
			s = '*'

		return str(num) + s.upper()
