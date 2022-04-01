from finance.Compte import Compte


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
        # print("5 : Consulter compte \n")
        # print("6 : Consulter compte \n")
        # print("4 : Sortir \n")
        execution = int(input("quelle action voulez-vous exécuter : "))
        print("\n")

        if (execution == 1):
            #print(compte, "\n")
            print(compte.__str__())

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
















