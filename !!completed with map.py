#bugs need to recognise duplicates (this can be a later step)

import enchant
import string
#letter_count = dict(zip(string.ascii_lowercase, [0]*26))

def enchant_test():
	d = enchant.Dict ("en_GB")
	print "this tests 'colour':", d.check("colour")
	print "this tests 'color':", d.check("color")

string_word = 'short'
alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#print alphabet_list[0:27]
#print "Is the user word a string?:", type(string_word) is str

# def listmake(string_word):
# 	for i in range(len(string_word))


def changer(string_word): #makes the string word a list and changes letters
	import enchant
	d = enchant.Dict ("en_GB")
	lower_word =string_word.lower()
	list_word = list(string_word.lower())
	new_words = []
	letter = 0
#	print "did the string word become a list?:", type (list_word) is list
	#for place, letter in enumerate(list_word):
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
	return new_words

test_words = ['short', 'snort', 'sport', 'shirt', 'short', 'shoot', 'short', 'shout', 'shore', 'shorn', 'short']



r=map(changer,test_words)







# def secondchanger(argument):
# 	import enchant
# 	d = enchant.Dict ("en_GB")
# 	for object in argument:
# 		lower_word =string_word.lower()
# 	list_word = list(string_word.lower())
# 	further_words = []
# 	letter = 0
# #	print "did the string word become a list?:", type (list_word) is list
# 	#for place, letter in enumerate(list_word):
# 	while letter < (len(list_word)):#, letter in enumerate(list_word):
# 		x = 0
# 		while x < len(alphabet_list):
# 			copy_list_word = list(list_word) #creates a new list to be modified
# 			copy_list_word[letter] = alphabet_list[x]
# 			if d.check(''.join(copy_list_word)):
# 				new_words.append(''.join(copy_list_word))	
# 			x= x+1
# 			if x == len(alphabet_list):
# 				letter = letter + 1
# 	print further_words

# secondchanger(new_words)

# 				# while x <len(alphabet_list):
				# 	copy_list_word = list(list_word) #creates a new list to be modified
				# 	copy_list_word[letter] = alphabet_list[x]
				# 	x= x+1
				# 	new_words = copy_list_word
				# 	print new_words


			# if x == 8:
			# 	copy_list_word[2] = alphabet_list[x]
			# 	new_words = list_word
			# 	print new_words



# 		# print place, letter
# #		#if place in letter:
# 			list_word[i] = alphabet_list[x]
# 			x=x+1
# 			print list_word
			#if x = 10:

			#new_words.append(''.join(list_word))
	#print new_words

changer(string_word)

# def wordflow(string_word):
# 	final_word =list_word.lower()
# 	print final_word
# 	for index, letter in enumerate(alphabet_list):
# 		print index, letter
# 	for letter in final_word:
# 		print letter
# 		letter = alphabet_list[0]
# 		print final_word




#wordflow(list_word)

#print alphabet['1']

#string_word = "bed"
#list_word = string_word.split()
#for letter in list_word:
#	list_word[0]=alphabet['2'] #change alphabet by +1 each time
#	print list_word


#list_input[0]= 'r'
#print string_input[0]
#print type(list_input)

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

#print "dict['Name']: ", dict['Name'];
#print "dict['Age']: ", dict['Age'];

#d = enchant.Dict("en_GB")





#for letter in word:
	#word[0]="a"
	#if d.check(word) == true:
	#	print word.check
	#else word[0] = b
	#print "fail"


#string_word = raw_input([])
#input_list = string_word.split()
#process string elements in the list and make them integers
#input_list = [int(a) for a in input_list]


#def wordplay([word]):
