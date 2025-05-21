from FONCTIONS.gestion_emprunts import gestion_emprunts
from FONCTIONS.gestion_lecteurs import gestion_lecteurs
from FONCTIONS.gestion_livres import gestion_livres

import os

def menu(instance_emprunts,instance_lecteurs,instance_livres):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # supprimer la console
        print("\n----------------------------------Menu Principal---------------------------------------------------- :")
        print("1. Gérer les emprunts   ||  2. Gérer les livres   ||  3. Gérer les lecteurs   ||  4. Quitter")
        choix = input("Entrez votre choix: ")

        match choix:
            case "1":
                #os.system('cls' if os.name == 'nt' else 'clear')
                print("-----------------------------Menu du gestion des emprunts----------------------------- :")
                print("1. Demander un emprunt   ||  2. Rendre un emprunt  ||  3. Liste emprunts en cours  ||  4. Quitter")
                choix = input("Entrez votre choix: ")
                instance_emprunts.menu(str(choix),instance_lecteurs,instance_livres)  # Passer instance_lecteurs et instance_livres ici
            case "2":
                print("----------------------------Menu du gestion des livres:------------------------------ :") 
                print("1. Ajouter livre   ||  2. modifier livre  ||  3. supprimer livre  ||  4. Liste des livres  ||  5. Quitter")
                choix = input("Entrez votre choix: ")     
                instance_livres.menu(str(choix))

            case "3":
                print("----------------------------Menu du gestion des lecteurs------------------------------ :")
                print("1. Ajouter un lecteur  ||  2. Modifier Lecteur  ||  3. supprimer Lecteur  ||  4. Liste des Lecteurs  || 5. Quitter")
                choix = input("Entrez votre choix: ")
                instance_lecteurs.menu(str(choix))


            case "4":
                print("Quitter")
                break
            case _:
                print("Choix invalide, veuillez réessayer.")

        


def main():
    gestion_emprunts_instance = gestion_emprunts()
    gestion_livres_instance = gestion_livres()
    gestion_lecteurs_instance = gestion_lecteurs()

  
    menu(gestion_emprunts_instance, gestion_lecteurs_instance, gestion_livres_instance)  # Pass None for livres and lecteurs for now

if __name__ == "__main__":
    main()