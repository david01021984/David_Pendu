import random


def wordPickUp():
    words = list(["Abriter","Billard","Bretzel","Cithare","Djembé","Drapeau","Exemple","Fourmis","Grandir",
              "Iceberg","Mondial","Notable","Oxygène","Panique","Pétrole","Commun","Avril","Mai","Juin",
              "Juillet","Septembre","Decembre","Coq","Air","Sensiblement","Animal","Serpent","Python",
              "java","css","ia","molengeek","Kadri"])
    return random.choice((words)).upper()

def underscore(word , L = []):
    result = ''
    for i in word:
        if i in L:
            result += i + ' '
        else:
            result += '_ '
            
    return result.strip()  #strip() supprime les "blank space"


def EnterLetter():
    while True:
        letter = input("Please pick a letter : ").upper()
        if len(letter) == 1 and letter.isalpha():
            return letter
        else:
            print("Please enter just one letter please ;-) ")


solution = wordPickUp()
print(solution)
nb_error = 0
lettersBurned = []
display = underscore(solution)
print(f"Word to guess : {display} " )
while True :
    while '_' in display and nb_error < 5 :
#        lettre = (input("Entrez une lettre : ")).upper()
        lettre = EnterLetter()
        if lettre not in lettersBurned:
            lettersBurned += [lettre]
            
        if lettre not in solution:
            nb_error +=1           
        
        display = underscore( solution , lettersBurned )
        print(f"Word to guess : {display}        Errors : {nb_error}         Letters already used : {lettersBurned} \n")
        if nb_error==0:
            print(" ============ \n")
        elif nb_error==1:
            print(" ==========Y= ")
            print(" ||/       |  \n")
        elif nb_error==2:
            print(" ==========Y= ")
            print(" ||/       |  ")
            print(" ||        0  \n")
        elif nb_error==3:
            print(" ==========Y= ")
            print(" ||/       |  ")
            print(" ||        0  ")
            print(" ||       /|\ \n")
        elif nb_error==4:
            print(" ==========Y= ")
            print(" ||/       |  ")
            print(" ||        0  ")
            print(" ||       /|\ ")
            print(" ||       / \  \n")
        elif nb_error==5:  
            print(" ==========Y= ")
            print(" ||/       |  ")
            print(" ||        0  ")
            print(" ||       /|\ ")
            print(" ||       / \  ")  
            print(" ||            ")                 
            print("/||\      (x)  ")
            print("==============\n")
            print("YOU LOOSE")
            print("Max error number reached")
            break
    else :    
        print("\n")
        print(" ==========Y= ")
        print(" ||/          ")
        print(" ||     O U F ")
        print(" ||           ")
        print(" ||        0  ")  
        print(" ||       /|\  ")                 
        print("/||\      / \  ")
        print("==============\n")
        print("  - YOU WIN -      ")
    break

