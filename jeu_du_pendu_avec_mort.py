# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:42:51 2022

@author: colin
"""

import random

dictionnary = ["hello",
               "unicorn",
               "tea",
               "time",
               "person",
               "thing",
               "week",
               "women",
               "men",
               "place",
               "government",
               "company",
               "good",
               "new",
               "high",
               "important",
               "same",
               "come",
               "up",
               "down",
               "please",
               "luck",
               "misunderstood",
               "mother",
               "father",
               "child",
               "children",
               "daughter",
               "son",
               "grandmother",
               "grandfather",
               "brother",
               "sister",
               "food",
               "drink",
               "vegetables",
               "breakfast",
               "special",
               "monday",
               "tuesday",
               "wednesday",
               "thursday",
               "friday",
               "saturday",
               "sunday",
               "january",
               "february",
               "march",
               "april",
               "may",
               "june",
               "july",
               "august",
               "september",
               "october",
               "november",
               "december",]

##functions
def underscore(word):
    at=['_ ' for i in range(len(word))]
    return at

def affiche(tab):
    co=''
    for i in range(len(tab)):
        co+=tab[i]
    return co

def inputLetter():
    letter=''
    letter = input("Enter a lowercase letter : ")
    print("")
    if len(letter)>2:
        inputLetter
    else:
        return letter
    
def letterInTheWord(let,word):
    bool=False
    for i in range(len(word)):
        if let==word[i]:
            bool=True
            return bool
    return bool

def changeUp(let,aff,wor):
    for i in range(len(wor)):
        if let==wor[i]:
            aff[i]=let
    return aff   
 
def finito(tab):
    bool=False
    for i in range(len(tab)):
        if tab[i]!='_ ':
            bool=True
        else:
            bool=False
            break
    return bool

def poteau(nb):
    s=''
    if(nb==0):
        s="\n   \n   \n  \n======"
    elif(nb==1):
        s="\n   \n   \n|  \n======"
    elif(nb==2):
        s="\n   \n|   \n|  \n======"
    elif(nb==3):
        s="\n|   \n|   \n|  \n======"
    elif(nb==4):
        s="__\n|   \n|   \n|  \n======"
    elif(nb==5):
        s="____\n|   \n|   \n|  \n======"
    elif(nb==6):
        s="____\n|  Ó \n|   \n|  \n======"
    elif(nb==7):
        s="____\n|  Ó \n|  | \n|  \n======"
    elif(nb==8):
        s="____\n|  Ó \n| /| \n|  \n======"
    elif(nb==9):
        s="____\n|  d \n| /|\ \n|  \n======"
    elif(nb==10):
        s="____\n|  Ó \n| /|\ \n| /  \n======"
    elif(nb==11):
        s="____\n|  Ó \n| /|\ \n| / \ \n======"
    return s    

def tour():
    ##initialisation
    db=False
    nb_errors = 0
    wordToGuess = random.choice(dictionnary)
    print("//",wordToGuess)
    aff = underscore(wordToGuess)
    lettersAlreadyPlayed = []
    print("Word to guess : ")
    print(affiche(aff),"\n")    
    
    ##debut boucle principale

    while nb_errors<11:
        letter = inputLetter()#enter a letter
        br=letterInTheWord(letter,wordToGuess) #is the letter in the word at least once ?     
        
        if br:#b = True
            aff=changeUp(letter,aff,wordToGuess)#put the letter in the word
            db=finito(aff)#is the word completed ?

        
        else:#b = False
            lettersAlreadyPlayed.append(letter)#take note of the letter
            nb_errors+=1 #increase the number of errors
            
            if nb_errors==11:#if number of errors maximum
                print("You lost, the word to guess was : ", wordToGuess)
                print(poteau(nb_errors))

                return "End"
            
        print("Word to guess : ",affiche(aff))
        print(poteau(nb_errors))
        print("Number of errors : ",nb_errors,"/11\n")  
        print("Letters already played :",lettersAlreadyPlayed)


        if db:##if end by winning
            print(affiche(aff))
            print("The end, you made : ",nb_errors," errors : ",lettersAlreadyPlayed)
            print(poteau(nb_errors))

            xy=input("\nDo you want to play again ? [Y/N]\n")
            if xy=="Y":
                tour()
            return "End"
                                    
##Main : 
tour()