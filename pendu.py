import random

words = ["hello","unicorn","tea","time","person","thing","week","women","men","place","government","company","good","new","high","important","same","come","up","down"]
choice = random.choice(words)

print(choice)

def trait(word):
    a=['_ ' for i in range(len(word))]
    return a

affichage = trait(choice)

print(affichage)
print("Guess the following word : ",affichage)

letter = input("enter a letter : ")
Answers = []

def turn():
    b = False
    i=0
    while i < len(choice):
      if letter == choice[i]:
         affichage[i] = letter
         b=True

    if b == False:
        Answers+=letter
    print(affichage)
    print(Answers)
    i+=1

def appartient_a(l,word):
    longu = len(word)
    b=False
    for i in range(longu):
        if l==
def tour_de_jeu():
    word=random.choice(words)
    longu = len(word)
    secret = '_ '*longu
    nb_errors = 0
    nb_errors_max=11
    print("Guess the word :")
    
    while nb_errors<nb_errors_max:
        letter = input("Enter a letter : ")
        
    
    
    