import json
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../DATA/livres.json")

class livre (object):
    def __init__(self,id,titre,auteur,disponibilite="Disponible"):
        self.id=id
        self.titre=titre
        self.auteur=auteur
        self.disponibilite=disponibilite
    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "auteur": self.auteur,
            "disponibilite": self.disponibilite
        }   


class gestion_livres:
    def __init__(self):
        with open(data_path,"r") as f:
            self.liste_livres=json.load(f)
    
    def save_livres(self):
        with open(data_path,"w") as f:
            json.dump(self.liste_livres,f)



    def add_livre(self,livre):
        self.liste_livres.append(livre.to_dict())
            
    
    def remove_livre(self,livre):
        self.liste_livres.remove(livre)
        # with open(data_path,"w") as f:
        #     json.dump(self.liste_livres,f)  
    
    def update_livre(self,livre):   
        for i in range(len(self.liste_livres)):
            if self.liste_livres[i]["id"]==livre.id:
                self.liste_livres[i]=livre.to_dict()
                break
        # with open(data_path,"w") as f:
        #     json.dump(self.liste_livres,f)
        
    def verifier_disponibilite(self,input):
        for i in range(len(self.liste_livres)):
            if self.liste_livres[i]["id"]==str(input) or self.liste_livres[i]["titre"]==str(input):
                if self.liste_livres[i]["disponibilite"]=="Disponible":
                    return True
                else:
                    return False
                
    def afficher_livres(self):
        if not self.liste_livres:
            print("Aucun livre enregistré.")
            return

        print(f"{'N°':<4} {'ID':<5} {'Titre':<30} {'Auteur':<20} {'Disponibilité'}")
        print("-" * 80)

        for i, x in enumerate(self.liste_livres, start=1):
            dispo = x.get("disponibilite", "Inconnu")
            print(f"{i:<4} {x['id']:<5} {x['titre']:<30} {x['auteur']:<20} {dispo}")
      
    
                
    def generer_nouvel_id(self):
        if not self.liste_livres:  # vide
            return 1
        else:
            ids = [int(livre["id"]) for livre in self.liste_livres]
            return str(max(ids) + 1)      

    def ajouter_livre(self):
        id=self.generer_nouvel_id()
        if not self.verifier_disponibilite(id):
            titre=input("Entrez le titre du livre : ")
            auteur=input("Entrez l'auteur du livre : ")
            livre1=livre(id,titre,auteur)
            self.add_livre(livre1)
            self.save_livres()
            print("Livre ajouté avec succès")
        else:
            print("Livre existe déjà ou n'est pas disponible")

    def modifier_livre(self):
        id=input("Entrez l'id du livre à modifier : ")
        if self.verifier_disponibilite(id):
            titre=input("Entrez le nouveau titre du livre : ")
            auteur=input("Entrez le nouvel auteur du livre : ")
            livre1=livre(id,titre,auteur)
            self.update_livre(livre1)
            self.save_livres()
            print("Livre modifié avec succès")
        else:
            print("Livre n'existe pas ou n'est pas disponible")
    
    def supprimer_livre(self):    
        id=input("Entrez l'id du livre à supprimer : ")
        if self.verifier_disponibilite(id):
            for i in range(len(self.liste_livres)):
                if self.liste_livres[i]["id"]==str(id):
                    self.liste_livres.remove(self.liste_livres[i])
                    break
            self.save_livres()
            print("Livre supprimé avec succès")
        else:
            print("Livre n'existe pas ou n'est pas disponible")


    def menu(self,choix): #print("1. Ajouter un lecteur  ||  2. Modifier Lecteur  ||  3. supprimer Lecteur  ||  4. Liste des Lecteurs")             
        
        while True:
            
            match choix:
                case "1":self.ajouter_livre()
                case "2":self.modifier_livre()
                case "3":self.supprimer_livre()
                case "4":self.afficher_livres()
                case "5": break
                case _:
                    print("Choix invalide, veuillez réessayer.")
            print("--------------------------------Menu des livres---------------------------------- :")
            print("1. Ajouter livre   ||  2. modifier livre  ||  3. supprimer livre  ||  4. Liste des livres  ||  5. Quitter")
            choix = input("Entrez votre choix: ")
            
                
