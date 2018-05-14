from random import randint


class Die:
	"""掷骰子的类"""

	def __init__(self, num_sides=6):
		"""初始化"""
		self.num_sides = num_sides

	def roll(self):
		"""掷骰子"""
		return randint(1, self.num_sides)
