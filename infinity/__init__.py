class Infinity:
	def __init__(self, negative=False):
		self.negative = negative
	def __lt__(self, other):
		if type(other) not in [Infinity, int, float]:
			raise ValueError(f"Invalid operand with type Infinity and {type(other)}")
		if type(other) == Infinity and other.negative == self.negative:
			return False

		if self.negative:
			return True
		
		return False
	def __gt__(self, other):
		if type(other) not in [Infinity, int, float]:
			raise ValueError(f"Invalid operand with type Infinity and {type(other)}")
		if type(other) == Infinity and other.negative == self.negative:
			return False

		if self.negative:
			return False
		
		return True
	def __le__(self, other):
		if type(other) not in [Infinity, int, float]:
			raise ValueError(f"Invalid operand with type Infinity and {type(other)}")
		if type(other) == Infinity and other.negative == self.negative:
			return True

		if self.negative:
			return True
		
		return False
	def __ge__(self, other):
		if type(other) not in [Infinity, int, float]:
			raise ValueError(f"Invalid operand with type Infinity and {type(other)}")
		if type(other) == Infinity and other.negative == self.negative:
			return True

		if self.negative:
			return False
		
		return True
	def __eq__(self, other):
		if type(other) not in [Infinity, int, float]:
			raise ValueError(f"Invalid operand with type Infinity and {type(other)}")
		if type(other) == Infinity and other.negative == self.negative:
			return True
		return False
	def __ne__(self, other):
		if type(other) not in [Infinity, int, float]:
			raise ValueError(f"Invalid operand with type Infinity and {type(other)}")
		return not self.__eq__(other)
