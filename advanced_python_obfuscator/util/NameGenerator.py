import random
import string


class NameGenerator:
	def __init__(self):
		pass

	@staticmethod
	def full_random(length=40):
		vName = random.choice(string.ascii_letters)
		for i in range(length):
			vName += random.choice(string.digits + string.ascii_letters)
		return vName
