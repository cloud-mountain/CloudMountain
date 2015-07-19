
userinput = "test"#raw_input("Enter an English word:")
 
def rootword(userinput): #makes the string word a list and changes letters
	import enchant
	#import string
	alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	d = enchant.Dict ("en_GB")
	lower_word =userinput.lower()
	list_word = list(userinput.lower())
	#	print "did the string word become a list?:", type (list_word) is list
	new_words = []
	letter = 0
	while letter < (len(list_word)):#, letter in enumerate(list_word):
		x = 0
		while x < len(alphabet_list):
			copy_list_word = list(list_word) #creates a new list to be modified
			copy_list_word[letter] = alphabet_list[x]
			if d.check(''.join(copy_list_word)):
				new_words.append(''.join(copy_list_word))	
			x= x+1
			if x == len(alphabet_list):
				letter = letter + 1
	print new_words

	#return global new_words

#print rootword.new_words
#test =['best', 'jest', 'lest', 'nest', 'pest', 'rest', 'test', 'vest', 'west', 'zest', 'test', 'teat', 'tent', 'test', 'text', 'test']

#r=map(rootword,test)

rootword(userinput)

#bugs need to recognise duplicates (this can be a later step)

