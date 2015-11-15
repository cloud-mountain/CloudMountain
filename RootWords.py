#imports an instance of the Flask class and will be the WSGI application
from flask import Flask
from flask import request
from flask import render_template
import enchant
app = Flask(__name__)

d = enchant.Dict ("en_GB")

#raw_input("Enter an English word:")
#while d.check(userinput) != True:
#	userinput =raw_input("please enter a REAL English word:")



#@app.route('/')
#def hello_world():
# returns a message to display to the browser
    #return "Hellow Orld!"
#userinput = "test"

#@app.route('/')

#raw_input ("Enter an English word:)
@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
# def test():
#     return "Hello Mountains"
def rootword():
    userinput = request.form['text']
    lower_word =userinput.lower()
    list_word = list(userinput.lower())
    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_words = []
    letterposition = 0
    while letterposition < (len(list_word)):
		x = 0
		while x < len(alphabet_list):
			changeable_list_word = list(list_word) #creates new list to be modified
			changeable_list_word[letterposition] = alphabet_list[x]
			if d.check(''.join(changeable_list_word)):
				new_words.append(''.join(changeable_list_word))
			x += 1
			if x == len(alphabet_list):
				letterposition += 1
    new_words = list(set(new_words))
    #print ', '.join(new_words)
    return ', '.join(new_words)


#print rootword()


#rootword(userinput)
#print result


#Use the run function to run the local server with application
#the 'if' __name == 'main' makes sure the server
#only runs the script if the module is executed from the python interpreter
# if __name__ == '__main__':
#     app.debug = True
#     app.run()
