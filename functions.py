# ============ About printing =============
def reset_var(targetText : str):
	global varNum, varText
	varNum = 0
	varText = targetText

# def get_var():
# 	global varNum
# 	varNum += 1
# 	return varText + "_{" + varText*varNum + "}"

import math

def get_var():
	global varNum
	varNum += 1
	mapSize = int(math.sqrt(varNum))+1
	x,y=0,0
	d=[[False for __ in range(mapSize)] for _ in range(mapSize)]

	boxSize = 0
	for _ in range(varNum):
		d[y][x]=True
		if x == 0 and y == boxSize:
			boxSize += 1
			x=boxSize
			y=0
		elif y < boxSize:
			y += 1
		elif y == boxSize:
			x -= 1

	output = ""
	for k in d:
		cnt = sum(k)
		tmp = ""
		if cnt > 0:
			tmp = varText
			for j in range(cnt-1):
				tmp = varText+"_{"+tmp+"}"
		output += tmp
	return varText+"_{"+output+"}"

def get_1():
	return r"\frac{"+varText+r"}{"+varText+r"}"

def get_2():
	return r"\int_{-\frac{"+varText+r"}{"+varText+r"}}^{\frac{"+varText+r"}{"+varText+r"}}d"+get_var()

def get_3():
	v = get_var()
	return r"\sum_{"+v+r"="+get_1()+"}^{"+get_2()+"}"+v

def get_4():
	return r"\int_{-"+get_1()+r"}^{"+get_1()+r"}\int_{-"+get_1()+r"}^{"+get_1()+r"}"+f"d{get_var()}d{get_var()}"

def get_x_factorial(x):
	x=str(x)
	v = get_var()
	return r"\prod_{"+v+r"=\frac{"+varText+r"}{"+varText+r"}}^{"+x+"}"+v

def get_x_plus_one(x):
	x=str(x)
	v = get_var()
	return r"\sum_{"+v+"="+get_1()+r"}^{"+x+"}"+v+r"\frac{"+get_2()+r"}{"+x+r"}"

def get_ln_x(x):
	x=str(x)
	v = get_var()
	return r"\int_{"+get_1()+"}^{"+x+r"}"+v+r"^{-"+get_1()+"}d"+v

def get_0():
	return r"\int_{"+get_1()+"}^{"+get_1()+"}d"+get_var()

def get_e_x(x):
	x=str(x)
	v=get_var()
	return r"\sum_{"+v+r"="+get_0()+r"}^{"+get_4()+r"}\frac{"+x+r"^{"+v+r"}}{"+v+"!}"

def get_plus(d : list):
	output = ""
	for x in d:
		output += get_e_x("{"+x+"}")
	return get_ln_x("{"+output+"}")

def get_minus(a,b):
	return "{"+get_ln_x(r"\frac{"+get_e_x(a)+"}{"+get_e_x(b)+"}")+"}"

# ============== About converting data ==========

def getNumData(num):
	output = {
		"original" : num,
		"positive" : num > 0,
		"integer" : bin(int(abs(num)))[2:],
		"decimal" : 0,
		"exponents" : [],
	}
	k = []
	d=abs(num)
	
	last = d-int(d)
	for i in range(1,10):
		tmp = last - 2**(-i)
		if tmp >= -0.0000001:
			last = tmp
			k += '1'
		else:
			k += '0'

	lastPos = 0
	for i, x in enumerate(k):
		if x == '1':
			lastPos = i
	output['decimal'] = ''.join(k)[:lastPos+1]


	intLen = len(output['integer'])
	for i, x in enumerate(output['integer']):
		if x == "1":
			output["exponents"].append(intLen-i-1)
	for i, x in enumerate(output["decimal"]):
		if x == "1":
			output["exponents"].append(-i-1)
	return output

def convertIt(datas):
	output = []
	for x in datas:
		if abs(x) > 1:
			output.append(convertIt(getNumData(x)["exponents"]))
		else:
			output.append(x)
	return output

def convertToText(datas):
	output = []
	for x in datas:
		if abs(x) > 1:
			d = []
			for k in convertIt(getNumData(x)["exponents"]):
				d.append(get_2()+"^{"+str(k)+"}")
			# output.append(f"({'+'.join(d)})")
			output.append(r"\left( "+get_plus(d)+r" \right) ")
		else:
			if abs(x) == 1:
				output.append("{"+get_1()+"}")
			elif abs(x) == 0:
				output.append("{"+get_0()+"}")
			else:
				output.append("{"+get_2()+"^{"+abs(x)+"}"+"}")
	return output