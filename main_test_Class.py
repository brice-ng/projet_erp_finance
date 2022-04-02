import pickle
import json
from finance.Compte import Compte
from finance.Compte import SousCompte


if __name__ == '__main__':

    compte = Compte(0, 15000)
    execution = 6
    while (execution != 0):

        print("Les différentes actions que vous pouvez exécuter sont : \n")
        print("0 : sortir  \n")

        print("1 : Lister tous les comptes \n")
        print("2 : Créditer compte \n")
        print("3 : Débiter Compte  \n")
        print("4 : Créer sous-compte \n")
        print("5 : Enregistrer dans un fichier \n")
        print("6 : Lire dans un fichier \n")
        # print("5 : Consulter compte \n")
        # print("6 : Consulter compte \n")
        # print("4 : Sortir \n")
        execution = int(input("quelle action voulez-vous exécuter : "))
        print("\n")

        if (execution == 1):
            #print(compte, "\n")
            print("compte principal:")
            print(compte.__str__())
            compte.listeSousCompte()

            execution = int(input("Appuyez sur un chiffre pour afficher les listes : "))
            print("\n")

        else:
            if (execution == 2):
                numero = int(input("Entrer le numero de compte : "))
                montant = int(input("Entrer le montant : "))

                compte.crediter(numero,montant)
                compte.listeSousCompte()
                #print(compte.__str__())
                # print(compte , "\n")
                execution = int(input("Appuyez sur un chiffre pour afficher les listes : "))
                print("\n")

            else:
                if (execution == 3):
                    print('')
                    numero = int(input("Entrer le numero de compte : "))
                    montant = int(input("Entrer le montant : "))

                    compte.debiterSousCompte(numero,montant)
                    #debiter sousCompte
                    print(compte, "\n")
                    execution = int(input("Appuyez sur un chiffre pour afficher les listes : "))
                    print("\n")

                else:
                    if(execution == 4):
                        #creer sous compte
                        codeParent = int(input("Entrer le code parent : "))
                        numero = int(input("Entrer le numero de compte : "))
                        pourcentage = int(input("Entrer le pourcentage : "))

                        montant = compte.montant *pourcentage/100

                        s = SousCompte(numero, montant, codeParent, pourcentage)
                        compte.ajouterSousCompte(s)

                        execution = int(input("Appuyez sur un chiffre pour afficher les listes : "))
                        print("\n")
                    else:
                        if(execution == 5):
                            # saves = compte.listeSousCompte()
                            # fichier = open("savesAccount.txt", 'w')
                            # pickle.dump(fichier,saves)
                            # tf = open("sauvegardeCompte.txt", "w")
                            # tf.write(compte.listeSousCompte())
                            # tf.close()
                            # s = SousCompte(numero, montant, codeParent, pourcentage)
                            #lste = compte.listSous
                            compte.save()
                            execution = int(input("Appuyez sur un chiffre pour afficher les listes : "))
                            print("\n")
                        else:
                            print(compte.lire())
                            execution = int(input("Appuyez sur un chiffre pour afficher les listes : "))
                            print("\n")


    print("fin \n")














