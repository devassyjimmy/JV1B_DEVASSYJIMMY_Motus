import random
from colorama import init, Fore

choix = input("Jouer(0), rajouter un mot(1), supprimer un mot(2) ?\n")

listeMots=["priere","muscle","moulin","motard","guerir","humeur","habile","venger","ventre","purger"]

if choix == "0" :
    init()
    fichier = open("listeMot.txt", "r")
    listeMots = fichier.readlines()
    random = random.randint(0, len(listeMots) -1)
    mot = listeMots[random].replace("\n", "")
    motList = []
    nbErreur = 0

    victoire = False

    def vérifier (mot,proposition):
        reponse  ="" 
        for i in range(len(mot)):
                if proposition[i]==mot[i]:
                    lettre=Back.YELLOW+proposition[i]
                    reponse+=lettre

                if proposition[i] == mot[i]:
                    lettre=Back.RED+proposition[i]
                reponse+=lettre
            
        
        else :
                lettre=Back.BLUE+proposition[i]
                reponse+=lettre
            
        return reponse

    while (nbErreur < 8 and victoire == False) :
            lettre = input("Entrer lettre\n")
            erreur = True

    from colorama import init, Fore
    print(Fore,Back.RED+"lettre bien placer")
    print(Fore,Back.YELLOW+"lettre a la mauvaise place")
    print(Fore,Back.BLUE+"la lettre n'est pas dans le mot")

    print(mot)
    for i in range(0,9):
        proposition=str(input("Entrez un mot de six lettre"))
        reponse=vérifier (mot,proposition)
        print(reponse)
        victoire=victoire(mot,proposition)
        if victoire==True:
            print("Vous etes le vainqueur !!!")
        if victoire==False:
            print("Vous avez perdu")

    

    elif choix == "1" :
        ajout = input("rajouter un mot ?\n")
        fichier = open("listeMot.txt", "a")
        fichier.write("\n" + ajout)

    elif choix == "2" :
        fichier = open("listeMot.txt", "r")
        print(fichier.read() + "\n\nQue supprimer ?")
        fichier = open("listeMot.txt", "r")
        bDD = fichier.readlines()
        print(bDD)
        motASupprimer = int(input("Indiquer son index\n"))
        bDD.pop(motASupprimer)
        fichier = open("listeMot.txt", "w")
        newFile = ""