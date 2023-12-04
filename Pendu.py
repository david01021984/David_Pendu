import random

words = list(["Abriter","Billard","Bretzel","Cithare","Djembé","Drapeau","Exemple","Fourmis","Grandir",
              "Iceberg","Mondial","Notable","Oxygène","Panique","Pétrole","Commun","Avril","Mai","Juin",
              "Juillet","Septembre","Decembre","Coq","Air","Sensiblement"])

word = (random.choice((words)).upper())

def underscore(mot , L = []):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '
            
    return r[:-1]
#print(underscore(word))
 
print(word)

def EnterLetter():
    letter = input("Entre une lettre : ")
    if len(letter)>1 :
        return EnterLetter()
    else :
        return letter.upper


solution = word
erreur = 0
lettresBrulees = []
affichage = underscore(solution)
print( 'Mot à deviner : ' , affichage )
while True :
    while '_' in affichage and erreur < 5 :
        lettre = (input("Entrez une lettre : ")).upper()
        if lettre not in lettresBrulees:
            lettresBrulees += [lettre]
            
        if lettre not in solution:
            erreur +=1           
        
        affichage = underscore( solution , lettresBrulees )
        print( 'Mot à deviner : ' , affichage , "Nombre d'erreur : " , erreur, " Lettres deja utilisées : ", lettresBrulees )
        if erreur==0:
            print(" ==========Y= ")
        elif erreur==1:
            print(" ==========Y= ")
            print(" ||/       |  ")
        elif erreur==2:
            print(" ==========Y= ")
            print(" ||/       |  ")
            print(" ||        0  ")
        elif erreur==3:
            print(" ==========Y= ")
            print(" ||/       |  ")
            print(" ||        0  ")
            print(" ||       /|\ ")
        elif erreur==4:
            print(" ==========Y= ")
            print(" ||/       |  ")
            print(" ||        0  ")
            print(" ||       /|\ ")
            print(" ||       / \  ")
        elif erreur==5:  
            print(" ==========Y= ")
            print(" ||/       |  ")
            print(" ||        0  ")
            print(" ||       /|\ ")
            print(" ||       / \  ")  
            print(" ||            ")                 
            print("/||\      (x)  ")
            print("==============\n")
            print("YOU LOOSE : Max error number reached")
            break
    else :    
        print("YOU WIN")
        print(" ==========Y= ")
        print(" ||/          ")
        print(" ||     O U F ")
        print(" ||           ")
        print(" ||        0  ")  
        print(" ||       /|\  ")                 
        print("/||\      / \  ")
        print("==============\n")
    break

