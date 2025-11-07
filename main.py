import functions
import pyperclip

functions.reset_var('t')

targetNum = input("Write a number to approximate : ")
try:
	data = functions.getNumData(int(targetNum))
except:
	try:
		data = functions.getNumData(float(targetNum))
	except:
		print(f"Failed to convert. Please check if '{targetNum}' is a number.")
		exit()

print(data)

exps = data["exponents"]
convertedExps = functions.convertIt(exps)

functions.reset_var(input("Write a variable(length : 1) to make the formula. (ex : t) : "))

tmp = []
for a, d in zip(data["exponents"], convertedExps):
	# print(a > 0, a, d)
	v='' if a > 0 else '-'
	tmp.append(functions.get_2()+"^{"+v+f"{functions.convertToText([a])[0]}"+"}")
output = functions.get_plus(tmp)

print()
print(output)
print()
if input("Wanna copy to clipboard? (Write c to copy it.) : ") == "c":
	pyperclip.copy(output)
	print("Successfully copied. Ctrl + v to paste it.")
	print("")