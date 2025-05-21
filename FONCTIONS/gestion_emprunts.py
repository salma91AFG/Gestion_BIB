import json
import os
from FONCTIONS.gestion_livres import gestion_livres
from FONCTIONS.gestion_lecteurs import gestion_lecteurs
from datetime import date


livres=gestion_livres()
lecteurs=gestion_lecteurs()

base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../DATA/emprunts.json")

class emprunt(object):
    def __init__(self,id_lecteur,liste_id_livres):    
        self.id_lecteur= id_lecteur 
        self.livres= liste_id_livres

    def to_dict(self):
        return {
            "id_lecteur": self.id_lecteur,
            "livres": self.livres
        }


class gestion_emprunts: 
    def __init__(self):
        with open(data_path,"r") as f:
            self.liste_emprunts=json.load(f)
        
    def save_emprunts(self):
        with open(data_path,"w") as f:
            json.dump(self.liste_emprunts,f)
    
    def add_emprunt(self,emprunt):
        self.liste_emprunts.append(emprunt.to_dict())
        # with open(data_path,"w") as f:
        #     json.dump(self.liste_emprunts,f)  
        
    def remove_emprunt(self,emprunt):
        for i in range(len(self.liste_emprunts)):
            if self.liste_emprunts[i]["id_lecteur"]==emprunt["id_lecteur"]:
                self.liste_emprunts.remove(self.liste_emprunts[i])
                break      
        # with open(data_path,"w") as f:
        #     json.dump(self.liste_emprunts,f)

    def update_emprunt(self,emprunt):
        for i in range(len(self.liste_emprunts)):   
            if self.liste_emprunts[i]["id_lecteur"]==str(emprunt.id_lecteur):
                self.liste_emprunts[i]=emprunt.to_dict()
                break
        

    
    def verif_emprunt(self,id_lecteur):
        """
        cette fonction verifie si un emprunt est enregistré dans la liste des emprunts
        la fonction cherche par id de lecteur ou id de livre 
        """
        exist=False
        for i in range(len(self.liste_emprunts)):
            if self.liste_emprunts[i]["id_lecteur"]==str(id_lecteur):
                exist=True
        return exist
    
    def afficher_emprunt_lecteur(self, id_lecteur):
        """
        cette fonction affiche la liste des livres empruntés par un lecteur
        """
        for i in range(len(self.liste_emprunts)):
            if self.liste_emprunts[i]["id_lecteur"] == str(id_lecteur):
                print(f"\n Livres empruntés par le lecteur ID {id_lecteur} :")
                print(f"{'N°':<4} {'ID Livre':<10}")
                print("-" * 20)
                for k, x in enumerate(self.liste_emprunts[i]["livres"]):
                    print(f"{k+1:<4} {x:<10}")
                break

    def verif_emprunt_lecteur(self,id_lecteur):
        """
        cette fonction retourne le pointeur de l'emprunt d'un lecteur dans la liste des emprunts
        """
        
        for i in range(len(self.liste_emprunts)):
            if self.liste_emprunts[i]["id_lecteur"]==str(id_lecteur):
                self.afficher_emprunt_lecteur(id_lecteur)
                return i
        return None

    def demande_emprunt(self):
        id_lecteur=input("entrer le numero d'identification du lecteur")
        # self.afficher_emprunt_lecteur(id_lecteur)
        if lecteurs.verif_lecteur(id_lecteur):     
            reponse=input("entrer la liste des livres désirés, séparés par des virgules")
            try:
                liste_id_livre=set([str(s) for s in reponse.split(",")])
            except:
                print("Erreur de saisie, veuillez entrer des identifiants valides")
                return None


            ls=[str(x) for x in liste_id_livre if livres.verifier_disponibilite(x)]
            if len(ls)==0:
                print("Aucun livre disponible")
            else:
                print("Les livres suivants sont disponibles: ",ls,"tapez entrer yes pour valider l'emprunt")
                reponse=input()
                if reponse=="yes":
                    new_emprunt=emprunt(id_lecteur,ls)
                    self.add_emprunt(new_emprunt)
                    for i in range(len(livres.liste_livres)):                
                        if str(livres.liste_livres[i]['id'])  in ls:
                            print("le livre est disponible")
                            livres.liste_livres[i]["disponibilite"]="Indisponible"
                            livres.save_livres()
                    self.save_emprunts()
                    print("Emprunt validé")
                else:
                    print("Emprunt annulé")
                
        else:
            print("Lecteur non enregistré, veuillez vous enregistrer avant de faire un empvrunt")

    def rendre_emprunt(self):
        id_lecteur=input("entrer le numero d'identification du lecteur")
        if lecteurs.verif_lecteur(id_lecteur):
            for i in range(len(self.liste_emprunts)):
                if self.liste_emprunts[i]["id_lecteur"]==str(id_lecteur):
                    print("la liste des livres empruntés est: ")
                    self.afficher_emprunt_lecteur(id_lecteur)
                    # for k,x in enumerate(self.liste_emprunts[i]["livres"]):
                    #     print("- livre",k+1," , identifiant livre :",x)
                    print("tapez les identifiants des livres que vous voulez rendre séparer par une virgule")
                    reponse=input()
                    try:
                        liste_id_livre=[str(s) for s in reponse.split(",")]
                    except:
                        print("Erreur de saisie, veuillez entrer des identifiants valides")
                        return None
                    
                    for x in liste_id_livre:
                        if x in self.liste_emprunts[i]["livres"]:
                            self.liste_emprunts[i]["livres"].remove(x)
                            for j in range(len(livres.liste_livres)):
                                if livres.liste_livres[j]["id"]==x:
                                    livres.liste_livres[j]["disponibilite"]="Disponible"
                                    break

                    if len(self.liste_emprunts[i]["livres"])==0:
                        self.remove_emprunt(self.liste_emprunts[i])
                        print("Tous les livres ont été rendus, l'emprunt a été supprimé")

                        
                    break
            self.save_emprunts()
            livres.save_livres()
            print("Emprunt rendu")       
        else:
            print("Lecteur non enregistré, veuillez vous enregistrer avant de rendre un livre")


    def afficher_emprunts(self,instance_lecteurs,instance_livres):
        """
        Affiche la liste des emprunts en cours avec les détails des lecteurs et des livres.
        """
        if not self.liste_emprunts:
            print("Aucun emprunt en cours.")
            return

        print(f"{'N°':<4} {'ID Lecteur':<12} {'Nom Lecteur':<15} {'ID Livre':<10} {'Titre Livre'}")
        print("-" * 70)
        compteur = 1

        # Création de dictionnaires pour lookup rapide
        lecteurs_dict = {lecteur["id"]: lecteur["nom"] for lecteur in instance_lecteurs.liste_lecteurs}
        livres_dict = {livre["id"]: livre["titre"] for livre in instance_livres.liste_livres}

        for emprunt in self.liste_emprunts:
            id_lecteur = emprunt["id_lecteur"]
            nom_lecteur = lecteurs_dict.get(id_lecteur, "Inconnu")

            for id_livre in emprunt["livres"]:
                titre_livre = livres_dict.get(id_livre, "Inconnu")
                print(f"{compteur:<4} {id_lecteur:<12} {nom_lecteur:<15} {id_livre:<10} {titre_livre}")
                compteur += 1


    def menu(self,choix,instance_lecteurs,instance_livres): 
        while True:
            
            match choix:
                case "1":self.demande_emprunt()
                case "2":self.rendre_emprunt()
                case "3":self.afficher_emprunts(instance_lecteurs,instance_livres)
                case "4": break
                case _:
                    print("Choix invalide, veuillez réessayer.")
            print("----------------------------Menu des emprunts------------------------------ :")
            print("1. Demander un emprunt   ||  2. Rendre un emprunt  ||  3. Liste emprunts en cours  ||  4. Quitter")
            choix = input("Entrez votre choix : ")