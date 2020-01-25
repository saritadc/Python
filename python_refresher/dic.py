
class Euler22():

	def __init__(self):
		self.rule = self.generate_rule()

	def read_fine(self):
		file = open("names.txt","r")
		lines = file.readlines()
		file.close()
		names = lines[0].split(",")
		refinedNames = []
		for name in names:
			refinedNames.append(name.strip('"'))
		return refinedNames
		
	
	def calculate_score(self):
		print("calculating score")
		names = self.read_fine()
		names.sort()
		overall_score = 0
		for name in names:
			name_score = self.find_score(name)
			position = names.index(name) + 1
			product = name_score * position
			overall_score = overall_score + product
		print(overall_score)

	def find_score(self, name):
		sum = 0
		for letter  in name:
			sum = sum + self.rule[letter]
		return sum
		

	def generate_rule(self): 
		string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		strDict = {}
		for i in range(26):
			strDict[string[i]] = i+1
		return strDict


euler = Euler22()
euler.calculate_score()




'''file = open("names.txt", "r")

lines = file.readlines()
print(lines)'''