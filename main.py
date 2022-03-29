# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def initCompte():
    compte ={
        "montant":10000,
        "code":0,
        "sousCompte":[]
    }
    s1 = {
        "code": 1,
        "pourcentage": 50,
        "montant": 5000,
        "compteParent": 0
    }
    s2 = {
        "code": 2,
        "pourcentage": 25,
        "montant": 2500,
        "compteParent": 0
    }
    s3 = {
        "code": 3,
        "pourcentage": 25,
        "montant": 1250,
        "compteParent": 1
    }
    compte['sousCompte'].append(s1)
    compte['sousCompte'].append(s2)
    compte['sousCompte'].append(s3)
    compte['sousCompte'].append({
        "code": 4,
        "pourcentage": 10,
        "montant": 125,
        "compteParent": 3
    })
    compte['sousCompte'].append({
        "code": 5,
        "pourcentage": 20,
        "montant": 250,
        "compteParent": 3
    })
    return compte;

def sousCompte(code,pourcentage,montant,parent):
    sousCompte={
        "code": code,
        "pourcentage": pourcentage,
        "montant": montant,
        "compteParent": parent
    }
    return sousCompte;

def creerSousCompte(compte):
    code =int(input('entrer le code : '))
    parent = int(input('entrer numero compte parent : '))
    #print(type(code))
    poucentage = int(input('entrer pourcentage : '))

    if(parent == 0):
        #print("entrer dans if")
        mont = int (int(compte['montant'])*poucentage/100)
    else:
        sCompte = trouverCompte(compte,int(parent))
        print(sCompte)
        mont = int(sCompte['montant']) * poucentage / 100
    compte['sousCompte'].append(sousCompte(code,poucentage,mont,parent))
    return compte


def trouverCompte(compte,code):
    liste = compte['sousCompte']
    for i in liste:
        if (i['code'] == code):
            #print(i)
            return {
                    "code": code,
                    "pourcentage": i['pourcentage'],
                    "montant": i['montant'],
                    "compteParent": i['compteParent']
                     }
    return None


def existSousCompte(compte,code):
    resp=False
    liste = compte['sousCompte']

    for i in liste:
        if(i['compteParent'] == code):
             return True
    return resp

def existCompte(compte,code):
    resp=False
    liste = compte['sousCompte']

    for i in liste:
        if(i['code'] == code):
             return True
    return resp

def existCompteParent(compte,code):
    resp=False
    liste = compte['sousCompte']

    for i in liste:
        if(i['compteParent'] == code):
             return True
    return resp


"""
def ajouter(compte,code,montant):
    liste = compte['sousCompte']
    m=0
    for i in liste:
        if (i['compteParent'] == code):
            m = montant*i['pourcentage']/100
            i['montant'] += m

            if(existCompteParent(compte,code)):
                ajouter(compte,i['compteParent'],m)
    return compte

"""

def crediter(compte,code,montant):

    if(code==0):
        compte['montant'] += montant
    else:
        compte['montant'] +=montant
        repartirCompteParent(compte,code,montant)

def debiter(compte,code,montant):
    liste = compte['sousCompte']

    if(code==0):
        print("impossible de debiter sur le compte principal")
    else:

        for i in liste:
            if (i['code'] == code):
                i['montant'] -= montant


def repartirCompteParent(compte,code,montant):
    liste = compte['sousCompte']
    m=0
    for i in liste:
        if (i['code'] == code):
            i['montant'] += montant
            #print(existCompteParent(compte,code))
            repartirCompteParent(compte,i['compteParent'],montant)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')

    compte = initCompte()
    print(compte)
    #compte = creerSousCompte(compte)
    #print(trouverCompte(compte, 2))
    crediter(compte,5,1000)
    print(compte)
    debiter(compte,1,1500)
    print(compte)
