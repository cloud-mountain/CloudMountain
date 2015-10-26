import enchant

d = enchant.Dict ("en_GB")

userinput = raw_input("Enter an English word:")
while d.check(userinput) != True:
	userinput =raw_input("please enter a REAL English word:")

list_word = userinput
lower_word =userinput.lower()
list_word = list(userinput.lower())

#changes letters
def rootword(userinput): 
	d = enchant.Dict ("en_GB")
	alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	new_words = []
	letterposition = 0
	changeable_list_word = list(list_word) 
	while letterposition < (len(list_word)):
		x = 0
		while x < len(alphabet_list):
			changeable_list_word[letterposition] = alphabet_list[x]
			if d.check(''.join(changeable_list_word)):
				new_words.append(''.join(changeable_list_word))	
			x += 1
			if x == len(alphabet_list):
				letterposition += 1
		new_words = list(set(new_words))
		return new_words


rootword(userinput)

result = rootword(userinput)
print result

