"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Tomáš
email: jenda.tomas@seznam.cz
discord: jendatomas
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

line= "-"*45


# log in
users_password= {"bob": "123", 
                 "ann": "pass123", 
                 "mike": "password123",
                 "liz": "pass123"
                 }
login_user = input("Enter your username: ")
login_password = input("Enter your password: ")

if login_user in users_password.keys() and login_password in users_password[f"{login_user}"]:
    print(f"{line}\nWelcome to the app, {login_user}")
else:
    print("Unregistered user, terminating the program...")
    exit()


# choose the text´s number
quantity_of_texts = len(TEXTS)
print(f"We have {quantity_of_texts} texts to be analyzed. \n{line}")
text_number= input(
    f"Enter a number btw. 1 and {quantity_of_texts} to selected: "
    )
if text_number.isalpha():
    print(f"The entered value must be number between 1 and {quantity_of_texts}. Terminating the program")
    exit()
elif int(text_number) >= 1 and int(text_number) <= quantity_of_texts:
    print(line)
    
else:
    print(f"The entered number must be between 1 and {quantity_of_texts}. Terminating the program..")
    exit()



## analyzer text
# text preparation for analysis 
choose_text = TEXTS[(int(text_number)-1)]
extracting_words= []
for word in choose_text.split():
    remove_punctuation= word.strip(".,!?:;_@-")
    extracting_words.append(remove_punctuation)

# the number of words in the analyzed text
words_number = []
for letter in extracting_words:
    if letter.isalpha():
        words_number.append(letter)

# words start with a capital letter
start_capital=[]
for letter in extracting_words:
    if letter[0].isupper() and letter.isalpha():
        start_capital.append(letter)

# words with capital letters only
only_capital = []
for letter in extracting_words:
    if letter.isupper() and letter.isalpha():
        only_capital.append(letter)

# words with lowercase letters only
only_lowercase= [] 
for letter in extracting_words:
    if letter.islower() and letter.isalpha():
        only_lowercase.append(letter)

# number of numeral
number_numeral= []
for letter in extracting_words:
    if letter.isnumeric():
        number_numeral.append(float(letter))

# sum of numeral
suma_numeral=sum(number_numeral)

# writing data
print(f" There are {len(words_number)} words in the selected text.\n",
      f"There are {len(start_capital)} titlecase words.\n",
      f"There are {len(only_capital)} uppercase words.\n",
      f"There are {len(only_lowercase)} lowercase words.\n",
      f"There are {len(number_numeral)} numeric strings.\n",
      f"The sum of all the numbers {suma_numeral}")
print(line)


## bar graph
print("LEN |","OCCURENCES",  "|".rjust(10),"NR.")
print(line)

# length and number of words
data_graph= {}
n=1
for word in extracting_words:
    if len(word) not in data_graph.keys():
        data_graph[len(word)] = 1
    elif len(word) in data_graph.keys():
        data_graph[len(word)] = data_graph[len(word)] +1 

# sorting keys and print graph

for key in sorted(data_graph.keys()):
    alig= 20-data_graph[key]
    print(f"{key:>3}","|",
          f"{'*'* data_graph[key]}",
           "|".rjust(alig), data_graph[key])