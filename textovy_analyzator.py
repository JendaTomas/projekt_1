"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Tomáš
email: jenda.tomas@seznam.cz
discord: Petr Svetr#4490
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
    print(f"{line}\n Welcome to the app, {login_user} \n{line}")
else:
    print("Unregistered user, terminating the program...")
    quit()
# choose the text´s number
text_number= input(f"Enter a number btw.")








