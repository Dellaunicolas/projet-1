# Projet Tri - Base de la programmation - Eric Derasse (2017)
# Auteurs :

# codage utilisé pour les accents
# coding=utf-8

import os  
import random
import time

#**********************************************************************
# Couche application (Graphique)
#**********************************************************************

# Selection des fonctions
def Menu(): 
    # Déclaration du tableau principal
    maTable = [ int(z) for z in open('random.txt', 'r').read().split() ]
    reponse = 1

    while reponse < 9: 
			
        print("Menu : ")
        print("------")
        print("")
        print("01. Initialiser")
        print("02. Charger")
        print("03. Tri rapide")
        print("04. Reverse")
        print("09. Sauver")	
        print("10. Quitter")
		
	#nomFichier = ""
        reponse = int(input("Faites votre choix : "))
        
        if reponse == 1 : 
            selectMenuInit()
			
        elif reponse == 2 :
            selectMenuCharger(maTable)
				
        elif reponse == 3 :
            selectMenuTriRapide(maTable)

        elif reponse == 4 :
            selectMenuReverse(maTable)

        elif reponse == 9 :
            selectMenuSauvegarde(maTable)
		
        elif reponse == 10 :
            break
		
        input("Appuyez sur une touche pour continuer ... ")
        os.system('clear')
	
def selectMenuInit() :
	
    nomFichier = input("Quel est le nom de votre fichier ?  ")
    nb = int(input("Combien de nombre voulez-vous ? "))
	
    if not nomFichier.isalpha():
        nomFichier="iniTab.txt"
		
    initTab(nomFichier,nb)
	
def selectMenuCharger(maTable):
	nomFichier = input("Quel est le nom de votre fichier ? ")
	nb = int(input("Combien de nombre voulez-vous ? "))

	if not nomFichier.isalpha():
		nomFichier="iniTab.txt"
		
	loadTab(maTable,nomFichier,nb)
	print("Voici les nombres selectionnes : ",maTable)
    
def selectMenuTriRapide(maTable):
    data=open("./data.txt", "a")
    print ("Voici les nombres selectionnes : ")
    print (maTable)
    start_time = time.time()
    triRapide(maTable,0,len(maTable)-1)
    print("Voici les nombres tries : ")
    print (maTable)
    process=(time.time() - start_time)
    data.write(str(process) + " ; ")
    print (process)

def selectMenuReverse(maTable):
    print ("Voici les nombres selectionnes : ")
    print(maTable)
    print ("Voici les nombres inversés : ")
    Reverse(maTable)
    
def selectMenuSauvegarde(maTable) :
    nomFichier = input("Quel est le nom de votre fichier de sauvegarde ? ")
    saveTab(maTable,nomFichier)
	
	
#**********************************************************************
# Couche logique (Métier)
#**********************************************************************

def Reverse(maTable):
    x = len(maTable)-1
    i = 0
    while i < x:
        temp = maTable[i]
        maTable[i] = maTable[x]
        maTable[x] = temp
        i = i + 1
        x = x - 1
    print (maTable)
        
def triRapide(maTable, gauche, droite):
  ChoixPivot(maTable,0,len(maTable)-1)
  partitionement(maTable,premier,dernier)
def ChoixPivot(maTable,premier,dernier):
   if premier<dernier:

       pivot = partitionement(maTable,premier,dernier)

       ChoixPivot(maTable,premier,pivot-1)
       ChoixPivot(maTable,pivot+1,dernier)


def partitionement(maTable,premier,dernier):
   pivot = maTable[premier]

   gauche = premier+1
   droite = dernier

   fini = False
   while not fini:

       while gauche <= droite and maTable[gauche] <= pivot:
           gauche = gauche + 1

       while maTable[droite] >= pivot and droite >= gauche:
           droite = droite -1

       if droite < gauche:
           fini = True
       else:
           temp = maTable[gauche]
           maTable[gauche] = maTable[droite]
           maTable[droite] = temp

   temp = maTable[premier]
   maTable[premier] = maTable[droite]
   maTable[droite] = temp


   return droite



    #méthode de tri rapide récursive à complèter
 
      
#**********************************************************************
# Couche données (Data)
#**********************************************************************			

# Génération des nombres entier aléatoires et sauvegarde dans un fichier

def initTab(fichier,nb):
	fichier = open(random.txt,"w")
	for i in range(0,nb):
		nombre = random.randint(0,nb)
		print ((nombre), file = fichier)
	fichier.close()
	
# Chargement du fichier dans un tableau en mémoire
def loadTab(maTable,fichier,nb):
	fichier = open(fichier,"r")
	for i in range(nb):
		var = fichier.readline()
		maTable.append(int(var))
	fichier.close()

# Sauvegarde du tableau en mémoire dans un fichier
def saveTab(maTable,fichier):
	fichier = open(fichier,"w")	
	for i in range(0,len(maTable)-1):
		print ((maTable[i]), file = fichier)
	fichier.close()  

#**********************************************************************
# Programme principal
#**********************************************************************	
Menu()