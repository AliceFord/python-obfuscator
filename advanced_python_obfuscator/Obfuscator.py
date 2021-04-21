import re
from .util import NameGenerator


class Obfuscator:
	def __init__(self, code, options):
		self.code = code
		self.options = options  # Obfuscation options

	def obfuscate(self):
		functions = re.findall(r"def (.*)\(.*\):", self.code)

		nameGenerator = NameGenerator()

		# Obfuscate function names

		for function in functions:
			currentName = nameGenerator.full_random()
			self.code = re.sub(r"{}(?=\(.*\))".format(function), currentName, self.code)

		# Replace text with hex values

		writtenStrings = re.finditer(r"(?<=[\"\'])(.*?)(?=[\"\'])", self.code)

		extraStringLength = 0
		for writtenString in writtenStrings:
			for i in range(writtenString.start(0), writtenString.end(0)):
				temp = list(self.code)
				temp[i+extraStringLength] = hex(ord(self.code[i+extraStringLength])).replace("0x", r"\x")
				self.code = ''.join(temp)

				extraStringLength += 3

		# Remove comments

		linesToRemove = []
		for i, line in enumerate(self.code.split("\n")):
			if line.startswith('#'):
				linesToRemove.append(i)

		for line in reversed(linesToRemove):
			self.code = '\n'.join([l for i, l in enumerate(self.code.split('\n')) if i != line])

		variables = re.findall(r"([a-zA-Z][a-zA-Z1-9]*?) *(?!==)(?:=)", self.code)

		for var in variables:
			varName = nameGenerator.full_random()
			self.code = re.sub(r"(?<!\"){}(?!\")".format(var), varName, self.code)

		return self.code
