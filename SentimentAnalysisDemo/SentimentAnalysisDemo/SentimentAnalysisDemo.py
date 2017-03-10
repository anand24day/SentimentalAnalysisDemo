import nltk.classify.util



# Reads flat file and Splits into words list 
with open("C:/Users/dbolleddu/Desktop/LoganmovieAnalysis.txt","r") as f:
	x = [line.split(' ') for line in f]

print(x)

# declare a new list

y = [] 

 # this is to insert all the list values into on list

for i in range(len(x)):
	y = y+x[i]

# perfrom String operations to get make words clear for analysis purpose (to remove /n, -, '')

for i in range(len(y)): 
	if y[i] == '-' or y[i] == '':
		del y[i]

# removes special charaters from the words in the list

y = [i.rstrip() for i in y]

y = [i.rstrip(':') for i in y]

y = [i.rstrip('.') for i in y]

y = [i.rstrip(';') for i in y]

y = [i.rstrip(']') for i in y]

y = [i.lstrip('[') for i in y]

print(y)
def ListofPos(wordslist):
	Ypos = ['good','excellent','nice','awsome','remarkably']
	for i in wordslist:
		if i in Ypos:
			print(i)

def ListofNeg(wordslist):
	YNeg = ['bad','not good','savage','tough',"doesn't",'cheap']
	for i in wordslist:
		if i in YNeg:
			print(i)

ListofPos(y)

ListofNeg(y)