import functions
import pyperclip

functions.reset_var('t')
# print(functions.get_minus(1, 2))
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

ver = input('Select version? (1/2/3) : ')
if ver == "1":
	tmp = []
	for a, d in zip(data["exponents"], convertedExps):
		# print(a > 0, a, d)
		v='' if a > 0 else '-'
		tmp.append(functions.get_2()+"^{"+v+f"{functions.convertToText([a])[0]}"+"}")
	output = functions.get_plus(tmp)
elif ver == "2":
	tmp = []
	for a, d in zip(data["exponents"], convertedExps):
		# print(a > 0, a, d)
		v='' if a > 0 else '-'
		tmp.append("{"+functions.get_2()+"^{"+v+f"{functions.convertToText([a])[0]}"+r"}}")

	out = []
	for i in range(int(len(tmp)/2)):
		# 2*i, 2*i+1
		# print(tmp[2*i+1]+"^{-"+functions.get_1()+r"}")
		out.append(functions.get_minus(tmp[2*i], "{"+tmp[2*i+1]+r"^{-"+functions.get_1()+r"}}"))
		# breakpoint()
		# print(out)
		# exit()

	if len(tmp) % 2 == 1:
		# 나머지가 있으면
		out.append(tmp[-1])
	output = functions.get_plus(["{"+x+"}"for x in out])
else:
	# $${\frac{\frac{\frac{1}{b}}{c}}{d}}^{-1}$$
	tmp = []
	for a, d in zip(data["exponents"], convertedExps):
		# print(a > 0, a, d)
		v='' if a > 0 else '-'
		tmp.append(functions.get_2()+"^{"+v+f"{functions.convertToText([a])[0]}"+"}")

	output = functions.get_1()
	for x in tmp:
		output = r"\frac{"+output+"}{"+x+"}"
	output = r"\left( "+output+r"\right)^{-"+functions.get_1()+"}"
	

print()
print(output)
print()
if input("Wanna copy to clipboard? (Write c to copy it.) : ") == "c":
	pyperclip.copy(output)
	print("Successfully copied. Ctrl + v to paste it.")
	print("")