import random
import time

def wordPickUp():
    words = list(["Abriter","Billard","Bretzel","Cithare","Djembe","Drapeau","Exemple","Fourmis","Grandir",
              "Iceberg","Mondial","Notable","Oxygène","Panique","Petrole","Commun","Avril","Mai","Juin",
              "Juillet","Septembre","Decembre","Coq","Air","Sensiblement","Animal","Serpent","Python",
              "java","css","ia","molengeek","Kadri"])
    return random.choice((words)).upper()

def underscore(word , LB = []):
    result = ''
    for i in word:
        if i in LB:
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


def initGame(stats_tab,name):
    solution = wordPickUp()
    nb_error = 0
    lettersBurned = []
    display = underscore(solution)

    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print(f"You already played {stats_tab['Games']} games with {stats_tab['Win']} wins and {stats_tab['Lost']} lost")
    print("\n")
    print(f"Word to guess : {display} " )

    stats_tab['Games'] += 1

    while True :
        while '_' in display and nb_error < 5 :
            letter = EnterLetter()
            if letter not in lettersBurned:
                lettersBurned += [letter]
            
            if letter not in solution:
                nb_error +=1           
        
            display = underscore( solution , lettersBurned )
        
            print(f"Word to guess : {display}        Errors : {nb_error}         Letters already used : {lettersBurned} \n")
            if nb_error==0 and '_' in display:
                print(" ============ \n")
            elif nb_error==1 and '_' in display:
                print(" ==========Y= ")
                print(" ||/       |  \n")
            elif nb_error==2 and '_' in display:
                print(" ==========Y= ")
                print(" ||/       |  ")
                print(" ||        0  \n")
            elif nb_error==3 and '_' in display:
                print(" ==========Y= ")
                print(" ||/       |  ")
                print(" ||        0  ")
                print(" ||       /|\ \n")
            elif nb_error==4 and '_' in display:
                print(" ==========Y= ")
                print(" ||/       |  ")
                print(" ||        0  ")
                print(" ||       /|\ ")
                print(" ||       / \  \n")
            elif nb_error==5 and '_' in display:  
                print(" ============ ")
                print(" ||/       Y  ")
                print(" ||        |  ")
                print(" ||        0  ")
                print(" ||       /|\ ")
                print(" ||        |\  ")                 
                print("/||\      (x)  ")
                print("==============\n")
                print("  -- YOU LOOSE -- ")
                print("Max error number reached")
                print(f"The word to guess was {solution}")
                stats_tab['Lost'] += 1
                replay = input(f"Would you like to play again {name} ? (yes/no) ").lower()
                if replay in ['yes', 'y', 'ok', 'yeah','oui','o']:
                    initGame(stats_tab,name)
                else :
                    print("\n")
                    print("THANKS FOR PLAYING MY GAME {name}!")
                    print("\n")
                    print(f"{name},you played {stats_tab['Games']} games with {stats_tab['Win']} wins and {stats_tab['Lost']} lost")
                    if stats_tab['Win'] > stats_tab['Lost']:
                        print("\n")
                        print(f"Yeah You Are Good At This Game {name}...")
                    else :
                        print("\n")
                        print(f"Nice Try {name}! You Will Do Better Next Time!")
                    exit()
            else :    
                print("\n")
                print(" ==========Y= ")
                print(" ||/          ")
                print(" ||     O U F ")
                print(" ||           ")
                print(" ||       \0/  ")  
                print(" ||        |  ")                 
                print("/||\      / \  ")
                print("==============\n")
                print("  - YOU WIN -      ")
                stats_tab['Win'] += 1  
                replay = input(f"Would you like to play again {name} ? (yes/no) ").lower()
                if replay in ['yes', 'y', 'ye', 'yo', 'ok', 'yeah','oui','o']:
                    initGame(stats_tab,name)
                else :
                    print("\n")
                    print(f"THANKS FOR PLAYING MY GAME {name}!")
                    print("\n")
                    print(f"You played {stats_tab['Games']} games with {stats_tab['Win']} wins and {stats_tab['Lost']} lost")
                    if stats_tab['Win'] > stats_tab['Lost']:
                        print("\n")
                        print("Yeah You Are Good At This Game...")
                    else :
                        print("\n")
                        print("Nice Try! You Will Do Better Next Time!")
                    exit()
                             
            
        
        
        


stats = {'Games': 0, 'Win': 0, 'Lost': 0}
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
name = input("Please enter your name : ")
initGame(stats,name)
    

