


class Compte:
    def __init__(self,code,montant):
        self.code=code
        self.montant=montant
        self.sousCompte=[]
        self.solde=montant
        self.restPercentage =100

    def ajouterSousCompte(self,souscompte):
        self.solde -= souscompte.montant
        self.restPercentage -= souscompte.pourcentage
        self.sousCompte.append(souscompte)

    def crediter(self,code,montant):
        if(self.code==code):
            for i in self.sousCompte:
                m=i.pourcentage*montant/100
                i.montant += m
        else:
            for s in self.sousCompte:
                if (s.code == code):
                    s.montant +=montant
            self.montant += montant

    def debiterSousCompte(self,code,montant):

        if (self.code == code):
            print("débit impossible sur ce compte!")
        else:
            for s in self.sousCompte:
                if (s.code == code):
                    s.debiter(montant)
            self.montant -= montant

    #def crediter(self,montant):

    def findByCode(self,code):
        if(self.code==code):
            return self
        else:
            for s in self.sousCompte:
                if(s.code == code):
                    return s
        return -1

    def __str__(self):
        return "code: {0}, montant: {1} ,solde: {2} ,restPercentage: {3}".format(self.code,self.montant,self.solde,self.restPercentage)

    def listeSousCompte(self):
        print(f"Sous compte de {0} :",self.code)
        for s in self.sousCompte:
            print(s)


    def listSousCompteByCode(self,code):

        print(self.findByCode(code))
        print("ses sous compte sont:")
        for s in self.sousCompte:
            if(s.code==code):
                print(s)



class SousCompte(Compte):
     def __init__(self,code,montant,codeParent,pourcentage):
        super().__init__(code,montant)
        self.codeParent = codeParent
        self.pourcentage=pourcentage


     def __str__(self):
        return "code: {0}, montant: {1} ,solde: {2} ,restPercentage: {3}, codeParent: {4}, pourcentage: {5}".format(self.code,self.montant,self.solde,self.restPercentage,self.codeParent,self.pourcentage)


     def debiter(self, montant):
        self.montant -= montant


if __name__ == '__main__':

    compte = Compte(0,15000)
    print(compte.__str__())
    print("")

    sous = SousCompte(1,1440,0,50)
    s1 = SousCompte(2,1500,0,40)
    so = SousCompte(3,500,1,30)

    compte.ajouterSousCompte(sous)
    compte.ajouterSousCompte(s1)

    compte.ajouterSousCompte(so)
    print(compte.__str__())
    print("")

    compte.listeSousCompte()
    print("")
    print("")
    #s1.listeSousCompte()

    print("find By Code:")

    #print(compte.findByCode(3))

    compte.listSousCompteByCode(1)



