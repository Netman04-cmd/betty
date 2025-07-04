"""
Le mot clé def est utilisé pour créer une fonction utlisateur
Le module os
"""
#Exempler fonction qui permet de controler la saisie d'un entier
def controle():
    while True:
        n=input("entrer un entier:")
        if n.isdigit():
            break
        else:
            print("la valeur saisie est incorecte")
    return int (n)
#n=controle()
#print("la valeur saisie est ",n)
#fonction qui permet de créer un dossier dont le nom est saisi
import os #os :operating system
def creationDossier():
    nomD=input("Entrer le nom du dossier à créer:")
    os.mkdir(nomD)
    print("Le dossier",nomD,"est créer avec succés")

#creationDossier()
#Fonction qui crée un lot de 10000 dossiers
def creationDossiers():
    nomDossier="ESMT_ASR_CS_"
    for i in range(10000):
        os.mkdir(nomDossier+str(i))
        print("Le dossier ",nomDossier+str(i),"est crée")
        
#creationDossiers()
#Fonction qui supprime les 10000 dossiers
def supprimeDossiers():
    nomDossier="ESMT_ASR_CS_"
    for i in range(10000):
         if os.path.exists(nomDossier+str(i)):
             os.rmdir(nomDossier+str(i))
             print("Dossier",nomDossier+str(i),"Supprimer avec succés")
         else:
                 print("le dossier n'existe pas")
#supprimeDossiers()
#Fonction qui créé un dossier dans C:
def creationDossierDansC():
    nomDossier=input("Entrer le nom du dossier à créer:")
    os.chdir("C:/")
    if os.path.exists(nomDossier):

        print("Le dossier existe de meme nom existe deja")
    else:
        os.mkdir(nomDossier)
        print("Le dossier est créé dans C:")
        
#creationDossierDansC()
#Fonction qui affche le conteu de C:
def afficheContenuRacineC():
    os.chdir("C:/")
    contenu=os.listdir()
    print("le contenu de la racine C est ")
    for c in contenu:
        print(c,end="  ")
#afficheContenuRacineC()
# fonction qui affiche le contenu de son bureau
def afficheContenubureau():
    os.chdir=("C:/Users/pc/Desktop")
    contenu=os.listdir()
    print("le contenu du bureau est ")
    for b in contenu:
        print(b,end=" ")
        
#afficheContenubureau()











                 
                 
       
    
    
