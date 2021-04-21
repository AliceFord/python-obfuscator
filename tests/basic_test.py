from advanced_python_obfuscator import Obfuscator


def test_1():
	code = """
hi = "Hello"
y = 1
YER=3
print(4==3)
for i in range(32):
	print(hi + " " + str(i))
	
print(True)

def yay(woo):
	print(woo)

yay("hi")

#yay("hi")
# woo
	"""
	obfuscator = Obfuscator(code, "")
	newCode = obfuscator.obfuscate()
	print(newCode)
	exec(newCode)

test_1()