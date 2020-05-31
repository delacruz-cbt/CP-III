import string

cripto = 0

with open("poneismalditosn.txt", "w") as arq: 
		data = arq.write(result)
		
alf = list(string.ascii_lowercase)
result = ""

	for index in range (0, 26):
		cripto = index
		for char in data:
			if char in alf:
				pos = alf.index(char)
				pos = (pos + cripto) 
				result = result + alf[pos]
			else:
				result = result + char

		result = result + "\n"

		print("ARQUIVO CRIPTOGRAFADO: \n", result)
		




