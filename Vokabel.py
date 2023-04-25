import random

Deutschl = []
Englischl = []


def SprachenAbFrage():
    pass


def Hinzufügen():
    print("Möchtest du erst Deutsch oder Englisch hinzufügen? (D/E)")
    DoE = input("> ")
    y = True
    z = True
    d = True
    while y:
        if DoE == "D" or DoE == "d":
            print("Gib die Deutsche Bedeutung an.")
            Deutsch = input("> ")
            y = not True
            f = 0
            while d:
                x = Deutsch.isalpha()
                if x:
                    d = not True
                    while f == 0:
                        if x:
                            print("Ist " + Deutsch +" das Wort was du Hinzufügen willst?")
                            Sicher = input("(Y/N) ")
                            f = f + 1
                            while z:
                                if Sicher == "y" or Sicher == "Y":
                                    print("Das word wurde zur Deutschen Liste hinzugefügt.")
                                    z = not True
                                    Deutschl.append(Deutsch)
                                    print(Deutschl)
                                    global De
                                    De = True

                                elif Sicher == "n" or Sicher == "N":
                                    Hinzufügen()
                                    z = not True
                                else:
                                    Sicher = input("Du musst Y oder N eingeben. ")

                else:
                    print("Du must ein Wort eingeben.")
                    Deutsch = input("> ")

        elif DoE == "E" or DoE == "e":
            print("Gib die Englisch Bedeutung an.")
            Englisch = input("> ")
            y = not True
            f = 0
            while d:
                x = Englisch.isalpha()
                if x:
                    d = not True
                    while f == 0:
                        if x:
                            print("Ist " + Englisch +" das Wort was du Hinzufügen willst?")
                            Sicher = input("(Y/N) ")
                            f = f + 1
                            while z:
                                if Sicher == "y" or Sicher == "Y":
                                    print("Das word wurde zur Englisch Liste hinzugefügt.")
                                    z = not True
                                    Englischl.append(Englisch)
                                    print(Englisch)
                                    global En
                                    En = True

                                elif Sicher == "n" or Sicher == "N":
                                    Hinzufügen()
                                    z = not True
                                else:
                                    Sicher = input("Du musst Y oder N eingeben. ")

                else:
                    print("Du must ein Wort eingeben.")
                    Englisch = input("> ")


        else:
            print("Du musst Deutsch oder Englisch wählen.")
            DoE = input("(D/E) > ")

    if En:
        print("Gib die Englisch Bedeutung an.")
        f = 0
        while d:
            x = Deutsch.isalpha()
            if x:
                d = not True
                while f == 0:
                    if x:
                        print("Ist " + Deutsch +" das Wort was du Hinzufügen willst?")
                        Sicher = input("(Y/N) ")
                        f = f + 1
                        while z:
                            if Sicher == "y" or Sicher == "Y":
                                print("Das word wurde zur Deutschen Liste hinzugefügt.")
                                z = not True
                                Deutschl.append(Deutsch)
                                print(Deutschl)

                            elif Sicher == "n" or Sicher == "N":
                                Hinzufügen()
                                z = not True
                            else:
                                Sicher = input("Du musst Y oder N eingeben. ")

            else:
                print("Du must ein Wort eingeben.")
                Deutsch = input("> ")
        




def Trainieren():
    pass


def eingabe():
    print("Das ist der Vokabeltrainer.")
    x = input("Gib ein ob du etwas hinzufügen oder Trainieren willst. (H/T) ")
    y = True
    while y:
        if x == "H" or x == "h":
            print("Du hast hinzufügen gewählt")
            Hinzufügen()
            y = not True
        elif x == "T" or x == "t":
            print("Du hast Trainieren gewählt")
            Trainieren()
            y = not True
        else:
            print("Du musst H oder T eingeben")
            x = input("(H/T) > ")
            print(x)


eingabe()
