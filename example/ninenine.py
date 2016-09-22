
def nine(num) : 
	result = ""
	for i in range(1 , num + 1) :
		for j in range(1 , i + 1) :
			result  += (str(j) + " * " + str(i) + " = " + str(i*j) + "\t")
		result += "\n"
	return result

num = raw_input("Give me a number \n")
print nine(int(num))
