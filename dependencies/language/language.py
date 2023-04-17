class Luanguage():
    def __init__(self, Ln):
        self.Ln = Ln
        #si Ln (qui veux dire languageNomber) est egale a 1 alors francais si c est egale a 2 alors anglais

    def Speak(self):
        if self.Ln == 1:
            print("le jeux est maintenant en Francais !")
            return self.Ln
        elif self.Ln == 2:
            print("Now the game is in English")
            return self.Ln
        else:
            print("probleme !")
            return self.Ln
            