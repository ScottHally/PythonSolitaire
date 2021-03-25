class card:

	def __init__(self,colour,suite,value):
		self.colour = colour
		self.suite = suite
		self.value = value
		self.isHidden = True

	def to_string(self):
		num = self.value
		s = self.suite[0]
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
