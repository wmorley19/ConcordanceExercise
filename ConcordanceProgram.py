# This program is designed to create a concordance of a .txt file and includes which sentence each word occurs in




text = open('C:/Users/wmorl/Concordance Program/script.txt', 'r') # open a file in read mode
t = text.read()

# clean the .txt file of various special charecters to avoid false mismatches and delimit sentences correctly
t = t.replace(',', '')
t = t.replace(';', '')
t = t.replace('-', '')
t = t.replace('"', '')
t = t.replace('?', '.')
t = t.replace('!', '.')
t = t.replace("--", '')
t = t.replace("-",'')
t = t.replace("(", '')
t = t.replace(")", '')
t = t.replace('\n', '')
t = t.replace('\r','')
t = t.lstrip()
t = t.strip()
t = t.upper()

# split file into sentences 
sents = t.split(".")
#split file into words 
words = t.split(" ")
 #initialize a dictionary to hold words 
myDict = dict()


def makeConcordance(f):


	for word in words:

		word = word.replace('.','') # replace periods at the end of a word to keep track of words at the end of sentences

		# this if statement will go through each word and create a count of how many times the word appears
		if word in myDict:
			myDict[word] = myDict[word]+1
		else:
			myDict[word] = 1

		# this loop will go through a pre-sorted list of words and check which sentences they appear in the create an empty list for the next word
	for key in sorted(myDict):
		newkeyList = []
		i=0 
		while i < len(sents):
			#add a spce to the end of the word and end of sentence to avoid root owrds appearing in other sentences
			if key+' ' in sents[i]+' ':
				newkeyList.append(int(i+1))
				i+=1
			else:
				i+=1
		print(key, ':', myDict[key], newkeyList)


#function call
makeConcordance(t)

