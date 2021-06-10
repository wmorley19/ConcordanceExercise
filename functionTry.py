text = open('C:/Users/wmorl/Concordance Program/GettysburgAddress.txt', 'r')
t = text.read()
t = t.replace(',', '')
t = t.replace(';', '')
t = t.replace('-', '')
t = t.replace('"', '')
t = t.replace('?', '.')
t = t.replace('!', '.')
t = t.replace("'", '')
t = t.replace('\n', '')
t = t.replace('\r','')
t = t.lstrip()
t = t.strip()
t = t.upper()
sents = t.split(".")
words = t.split(" ")
words = words
myDict = dict()
keyList = []

def makeConcordance(f):
	i=0
	for word in words:
		word = word.replace('.','')
		if word in myDict:
			
			myDict[word] = myDict[word]+1
		else:
			myDict[word] = 1

	#for key in sorted(myDict):
		#print(key,':', myDict[key])
	for key in sorted(myDict):
		newkeyList = []
		i=0 
		while i < len(sents):
			if key in sents[i]:
				newkeyList.append(int(i+1))
				i+=1
			else:
				i+=1
		print(key, ':', myDict[key], newkeyList)


makeConcordance(t)
