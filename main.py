# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from finance import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')

    compte = initCompte()
    # print(compte)
    # compte = creerSousCompte(compte)
    # #print(trouverCompte(compte, 2))
    # crediter(compte,5,1000)
    # print(compte)
    # debiter(compte,5,1500)
    # print(compte)

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
            lister(compte)
            execution = int(input("Appuyez sur un chiffre pour afficher les listes : "))
            print("\n")
        else:
            if (execution == 2):
                numero = int(input("Entrer le numero de compte : "))
                montant = int(input("Entrer le montant : "))
                crediter(compte, numero, montant)

                print(compte)
                # print(compte , "\n")
                execution = int(input("Appuyez sur un chiffre pour afficher les listes : "))
                print("\n")
            else:
                if (execution == 3):
                    print('')
                    numero = int(input("Entrer le numero de compte : "))
                    montant = int(input("Entrer le montant : "))

                    debiter(compte, numero, montant)
                    print(compte, "\n")
                    execution = int(input("Appuyez sur un chiffre pour afficher les listes : "))
                    print("\n")

                elif(execution == 4):
                    compte = creerSousCompte(compte)
                    execution = int(input("Appuyez sur un chiffre pour afficher les listes : "))
                    print("\n")

    print("fin \n")
