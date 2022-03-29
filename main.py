# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from finance import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')

    compte = initCompte()
    print(compte)
    compte = creerSousCompte(compte)
    #print(trouverCompte(compte, 2))
    crediter(compte,5,1000)
    print(compte)
    debiter(compte,5,1500)
    print(compte)
