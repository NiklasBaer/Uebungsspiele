import random
global Nummern
Nummern = [1, 2, 3, 4, 5, 6, 7, 8, 0]
x = 1000
c = 1000
y = 8999
winis = True
Geheimzahl = 0


def Zahlcreate(Nummern):
    global Ziffer1
    global Ziffer2
    global Ziffer3
    global Ziffer4
    Zahlkorekt = True
    while Zahlkorekt == True:

        Ziffer1 = random.choice(Nummern)
        Nummern.remove(Ziffer1)
        Ziffer2 = random.choice(Nummern)
        Nummern.remove(Ziffer2)
        Ziffer3 = random.choice(Nummern)
        Nummern.remove(Ziffer3)
        Ziffer4 = random.choice(Nummern)
        global Zahl
        Zahl = []
        Zahl.append(Ziffer1)
        Zahl.append(Ziffer2)
        Zahl.append(Ziffer3)
        Zahl.append(Ziffer4)

        Ziffer1 = str(Ziffer1)
        Ziffer2 = str(Ziffer2)
        Ziffer3 = str(Ziffer3)
        Ziffer4 = str(Ziffer4)

        Number = Ziffer1 + Ziffer2 + Ziffer3 + Ziffer4
        Number = int(Number)

        if Number >= 1000 and Number <= 8999:
            Zahlkorekt = not True



def Raten(x, c):

    global Guess

    Guess = input(
        "Der Computer hat sich eine Zahl ausgedacht du bist drann mit Raten : ")

    while 1000 == c:

        if (Guess >= '0' and Guess <= '9'):

            c = c - 1

        else:

            Guess = input("Bitte gebe eine Zahl ein : ")

    Guess = int(Guess)
    while 1000 == x:

        if Guess < x:

            Guess = input("Bitte gib eine Zahl zwischen 1000 und 8999 ein : ")

            Guess = int(Guess)

        elif Guess > y:

            Guess = input("Bitte gib eine Zahl zwischen 1000 und 8999 ein : ")

            Guess = int(Guess)

            return Guess

        else:

            x = x - 1

    global Versuche

    Versuche = 0

    Versuche = Versuche + 1


def PrüfenWieVieleRichtig(Guess, Zahl):

    Guess = str(Guess)
    Zahl = str(Zahl)
    global set1
    global set2
    set1 = set(Guess)
    set2 = set(Zahl)
    set3 = set1.intersection(set2)
    global list3
    list3 = list(set3)
    global Richtig
    Richtig = 0
    Richtig = len(list3)


def PrüfenWelcheRichtig(Guess):
    global Platz1
    Platz1 = 0
    global Platz2
    Platz2 = 0
    global Platz3
    Platz3 = 0
    global Platz4
    Platz4 = 0
    x = [int(a) for a in str(Guess)]
    Raten1 = x.pop(0)
    Raten2 = x.pop(0)
    Raten3 = x.pop(0)
    Raten4 = x.pop(0)

    if Raten1 == Ziffer1:
        Platz1 = Platz1 + 1
    if Raten2 == Ziffer2:
        Platz2 = Platz2 + 1
    if Raten3 == Ziffer3:
        Platz3 == Platz3 + 1
    if Raten4 == Ziffer4:
        Platz4 == Platz4 + 1
    global Hinweis
    Hinweis = Platz1 + Platz2 + Platz3 + Platz4


def Win(Ziffer1, Ziffer2, Ziffer3, Ziffer4, Guess):
    Ziffer1 = str(Ziffer1)
    Ziffer2 = str(Ziffer2)
    Ziffer3 = str(Ziffer3)
    Ziffer4 = str(Ziffer4)
    global Geheimzahl
    global winis
    winis = True
    Geheimzahl = Ziffer1 + Ziffer2 + Ziffer3 + Ziffer4
    Guess = int(Guess)
    Geheimzahl = int(Geheimzahl)
    if Guess == Geheimzahl:
        print("Das spiel ist voreib")

        winis = not True


def HinweisSpieler(Hinweis, Versuche):
    # Richtig  für wie viele
    # Hinweis wie viele ander richtigen stelle sind
    if Richtig == 1:
        print("Es ist eins Richtig.")
        if Hinweis == 1:
            print("Eins ist an der Richtigen Stelle.")
        if Hinweis == 2:
            print("Zwei sind an der Richtigen Stelle.")
        if Hinweis == 3:
            print("Drei sind an der Richtigen Stelle.")
        if Hinweis == 0:
            print("Keins ist an der Richtgen Stelle.")
    if Richtig == 2:
        print("Es sind zwei Richtig.")
        if Hinweis == 1:
            print("Eins ist an der Richtigen Stelle.")
        if Hinweis == 2:
            print("Zwei sind an der Richtigen Stelle.")
        if Hinweis == 3:
            print("Drei sind an der Richtigen Stelle.")
        if Hinweis == 0:
            print("Keins ist an der Richtgen Stelle.")
    if Richtig == 3:
        print("Es sind drei Richtig.")
        if Hinweis == 1:
            print("Eins ist an der Richtigen Stelle.")
        if Hinweis == 2:
            print("Zwei sind an der Richtigen Stelle.")
        if Hinweis == 3:
            print("Drei sind an der Richtigen Stelle.")
        if Hinweis == 0:
            print("Keins ist an der Richtgen Stelle.")
    if Richtig == 4:
        print("Du hast Gewonnen.")
        global winis
        winis = not False
        Versuche = str(Versuche)
        print("Du hast " + Versuche + " Versuch/e Gebraucht.")
        if winis:
            Spielerneut()
    if Richtig == 0:
        print("Es ist keins Richtig.")
        print("Es ist keins an der Richtigen Stelle.")
    
Versuche = 0

Zahlcreate(Nummern)
def Spiel(Versuche):
    while winis == True:
        Raten(x, c)
        print(Guess)
        print(Zahl)
        PrüfenWieVieleRichtig(Guess, Zahl)
        PrüfenWelcheRichtig(Guess)
        HinweisSpieler(Hinweis, Versuche)
        Versuche = Versuche + 1
    

Spiel(Versuche)

def Spielerneut():
    global Erneut
    Erneut = input("Möchtest du erneut Spielen? Gebe y/n ein : ")
    print(Erneut)
    if Erneut == "Y" or Erneut == "y":
        Spiel(Versuche)
        global winis
        winis = True
    else:
        input("Drücke eine beliebige taste um das Programm zu beenden.")