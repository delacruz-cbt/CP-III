import string

descripto = 0

with open("poneismalditosn.txt", "r") as arq: 
		data = arq.read()
		
alf = list(string.ascii_lowercase)
result = ""

	for index in range (0, 26):
		for char in result1:
			if char in alf:
				pos = alf.index(char)
				pos = (pos - descripto) 
				result = result1 + alf[pos]
			else:
				result = result1 + char

		result = result1 + "\n"

		print("ARQUIVO DESCRIPTOGRAFADO: \n", result)
		




