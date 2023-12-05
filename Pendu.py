import random


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


def initGame(stats_tab):
    solution = wordPickUp()
    #print(solution)
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
    print(f"You already played : {stats_tab['Games']} with {stats_tab['Win']} wins and {stats_tab['Lost']} lost")
    print("\n")
    print(f"Word to guess : {display} " )
    stats_tab['Games'] += 1
    while True :
        while '_' in display and nb_error < 5 :
#        letter = (input("Entrez une letter : ")).upper()
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
                print(" ==========Y= ")
                print(" ||/       |  ")
                print(" ||        0  ")
                print(" ||       /|\ ")
                print(" ||        |\  ")  
                print(" ||            ")                 
                print("/||\      (x)  ")
                print("==============\n")
                print("  -- YOU LOOSE -- ")
                print("Max error number reached")
                print(f"The word to guess was {solution}")
                stats_tab['Lost'] += 1
                replay = input("Play again ? (yes/no) ").lower()
                if replay == 'yes':
                    initGame(stats_tab)
                else :
                    exit()
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
                stats_tab['Win'] += 1  
                replay = input("Play again ? (yes/no) ").lower()
                if replay == 'yes':
                    initGame(stats_tab)
                else :
                    exit()
                             
            
        
        #print(stats_tab)
        


stats = {'Games': 0, 'Win': 0, 'Lost': 0}
initGame(stats)
    

