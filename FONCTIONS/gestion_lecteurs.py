import json
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../DATA/lecteurs.json")

class lecteur (object):
    def __init__(self,id,nom):
        self.id=id
        self.nom=nom

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom
        }

class gestion_lecteurs:
    def __init__(self):
        with open(data_path,"r") as f:
            self.liste_lecteurs=json.load(f)

    def save_lecteurs(self):
        with open(data_path,"w") as f:
            json.dump(self.liste_lecteurs,f)

    def add_lecteur(self,lecteur):
        self.liste_lecteurs.append(lecteur.to_dict())
        
    
    def remove_lecteur(self,id):
        for i in range(len(self.liste_lecteurs)):
            if self.liste_lecteurs[i]["id"]==str(id):
                self.liste_lecteurs.remove(self.liste_lecteurs[i])
                break
        

    def update_lecteur(self,lecteur):
        for i in range(len(self.liste_lecteurs)):
            if self.liste_lecteurs[i]["id"]==str(lecteur.id):
                self.liste_lecteurs[i]=lecteur.to_dict()
                break
        

    def verif_lecteur(self,input):
        """
        cette fonction verifie si un lecteur est enregistré dans la liste des lecteurs
        la fonction cherche par id de lecteur ou nom 
        """
        exist=False
        for i in range(len(self.liste_lecteurs)):
            if self.liste_lecteurs[i]["id"]==str(input) or self.liste_lecteurs[i]["nom"]==str(input):
                exist=True
        return exist

    def afficher_lecteurs(self): 
        for i,x in enumerate(self.liste_lecteurs):
            print( i+1, "- " , x["id"], " nom : ", x["nom"])

    def generer_nouvel_id(self):
        if not self.liste_lecteurs:  
            return 1
        else:
            ids = [int(livre["id"]) for livre in self.liste_lecteurs]
            return str(max(ids) + 1) 
        
    def ajouter_lecteur(self):
        id=self.generer_nouvel_id()
        nom=input("Entrez le nom du lecteur : ")
        if self.verif_lecteur(id):
            print("Lecteur existe deja")
        else:
            lecteur1=lecteur(id,nom)
            self.add_lecteur(lecteur1)
            self.save_lecteurs()
            print("Lecteur ajouté avec succès")

    def modifier_lecteur(self):
        id=input("Entrez l'id du lecteur à modifier : ")
        if self.verif_lecteur(id):
            nom=input("Entrez le nouveau nom du lecteur : ")
            lecteur1=lecteur(id,nom)
            self.update_lecteur(lecteur1)
            self.save_lecteurs()
            print("Lecteur modifié avec succès")
        else:
            print("Lecteur n'existe pas")
    
    def supprimer_lecteur(self):    
        id=input("Entrez l'id du lecteur à supprimer : ")
        if self.verif_lecteur(id):
            self.remove_lecteur(id)
            self.save_lecteurs()
            print("Lecteur supprimé avec succès")
        else:
            print("Lecteur n'existe pas")

    def menu(self,choix):         
        while True:
            
            match choix:
                case "1":self.ajouter_lecteur()
                case "2":self.modifier_lecteur()
                case "3":self.supprimer_lecteur()
                case "4":self.afficher_lecteurs()
                case "5": break
                case _:
                    print("Choix invalide, veuillez réessayer.")
            
            print("----------------------------Menu du gestion des lecteurs------------------------------ :")
            print("1. Ajouter un lecteur  ||  2. Modifier Lecteur  ||  3. supprimer Lecteur  ||  4. Liste des Lecteurs  ||  5. Quitter")
            choix = input("Entrez votre choix : ")


