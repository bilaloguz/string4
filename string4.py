def subtract(_num1, _num2):
	num1 = str(max(_num1,_num2))[::-1]
	num2 = str(min(_num1,_num2))[::-1]
	for i in range(0, len(num1)-len(num2)):
		num2 += "0"
	result = ""
	in_hand = 0
	for j in range(0, len(num1)):
		if int(num1[j]) - in_hand < int(num2[j]):
			result += str(((10 + int(num1[j]) - in_hand) - int(num2[j])))
			in_hand = 1
		else:
			result += str((int(num1[j]) - in_hand) - int(num2[j]))
			in_hand = 0
	if _num2 > _num1:
		return "-" + result[::-1]
	elif _num1 > _num2:
		return result[::-1]
	else:
		return "0"
	
def add(_num1, _num2):
	num1 = str(max(_num1,_num2))[::-1]
	num2 = str(min(_num1,_num2))[::-1]
	for i in range(0, len(num1) - len(num2)):
		num2 += "0"
	result = ""
	in_hand = 0
	for j in range(0, len(num1)):
		if int(num1[j]) + int(num2[j]) + in_hand > 9:
			result += str(int(num1[j]) + int(num2[j]) + in_hand - 10)
			in_hand = 1
		else:
			result += str(int(num1[j]) + int(num2[j]) + in_hand)
			in_hand = 0
	result += str(in_hand) 
	result = str(int(result[::-1]))
	return result
	
def multiply(_num1,_num2):
	num1 = str(_num1)[::-1]
	num2 = str(_num2)[::-1]
	in_hand = 0
	result = ""
	sum_list = []
	for k in range(0, len(num1) - len(num2)):
		num2 += "0"
	for i in range(0, len(num1)):
		row_result = ""
		for j in range(0, len(num2)):
			if ((int(num1[i]) * int(num2[j])) + int(in_hand)) > 9:
				row_result += str(int(num1[i]) * int(num2[j]) + int(in_hand))[1]
				in_hand = str(int(num1[i]) * int(num2[j]) + int(in_hand))[0]
			else:
				row_result += str(int(num1[i]) * int(num2[j]) + int(in_hand))
				in_hand = 0		
		row_result = str(int(row_result[::-1]))
		sum_list.append(row_result) 
	for l in range(0, len(sum_list)):
		sum_list[l] = str(sum_list[l]) + (l * "0")
	for m in range(0, len(sum_list)):
		result = add(result,sum_list[m])
	return result

def divide(_num1, _num2):
	num1 = int(_num1)
	num2 = int(_num2)
	result = ""
	remainder = ""
	
	temp = num1
	i = 1
	while(int(temp) > int(num2)):
		temp = subtract(temp, num2)
		i = i + 1
		
	result = str(i-1)
	remainder = str(int(temp))
	
	return (result, remainder)
