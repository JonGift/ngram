from nltk.corpus import wordnet

def generateAnagram(word):
	length = len(word)
	str = list(word)
	wordList = []
	
	permutation(str, 0, length-1, wordList)
	
	if word in wordList:
		wordList.remove(word)
	
	if len(wordList):
		print(wordList)
	else:
		print("No anagrams found.")
	
def permutation(str, index, end, wlist):
	if index == end:
		if wordnet.synsets((''.join(str))):
			wlist.append(''.join(str))
	else:
		for i in range(index, end+1):
			str[index], str[i] = str[i], str[index]
			permutation(str, index+1, end, wlist)
			str[index], str[i], = str[i], str[index]

if __name__ == '__main__':
	generateAnagram("John")