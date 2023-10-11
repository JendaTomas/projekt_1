"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Tomáš
email: jenda.tomas@seznam.cz
discord: JendaTomas
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
    quit()
# choose the text´s number
quantity_of_texts = len(TEXTS)
print(f"We have {quantity_of_texts} texts to be analyzed. \n{line}")
text_number= input(
    f"Enter a number btw. 1 and {quantity_of_texts} to selected: "
    )
if text_number.isalpha():
    print(f"The entered value must be number between 1 and {quantity_of_texts}. Terminating the program")
elif int(text_number) >= 1 and int(text_number) <= quantity_of_texts:
    print(line)
    quit()
else:
    print(f"The entered number must be between 1 and {quantity_of_texts}. Terminating the program..")
## analyzer text
# text preparation for analysis 
choose_text = TEXTS[(text_number)]
extracting_words= []
for word in choose_text.split():
    remove_punctuation= choose_text.strip(".,!?")
    extracting_words.append(remove_punctuation)
print(extracting_words)




