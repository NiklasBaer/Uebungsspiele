# Das ist das Hub wo man die spiele verwalten kann 

from Beginn import Spiel

Versuche = 0

def Abfrage():
    Eingabe = input("Gib die Zahl ein um das Spiel auszusuchen : ")
    Eingabe =  int(Eingabe)
    
    if Eingabe == 1:
        Spiel(Versuche)

Abfrage()
