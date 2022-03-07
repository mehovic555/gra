# kasyno
import random

cash = input("ile pieniedzy masz ze sobą?"+"\n")
bank = 0
# blackjack

reka = []
reka_stół = []
bd = random.randint(2, 11)


def BlackJack_gracz():
    a = random.randint(2, 11)
    print(a)
    b = random.randint(2, 11)
    print(b)
    f = a + b
    asy(a, f)
    asy(b, f)
    reka.append(a)
    reka.append(b)
    f = a + b
    print("na ręce masz " + str(reka) + " wynki na ręce to " + str(f))
    dobieranie(f)
    return f


def Blackjack_dealer():
    a = random.randint(2, 11)
    fd = a + bd
    asy(a, fd)
    asy(bd, fd)
    reka_stół.append(a)
    reka_stół.append(bd)
    fd = a + bd
    dobieranie_dealer(fd)
    print("ręka kasyna to " + str(fd))
    return fd


def asy(b, f):
    if b == 11:

        if f > 21:
            b == 1
    return b


def dobieranie(f):
    print("widoczna karta wydającego to " + str(bd))
    print("------------------------------------------")
    if f < 21:
        m = input("czy chcesz dobrać kartę?(tak/nie)"+"\n")
        if m == "tak":
            c = random.randint(2, 11)
            za = f + c
            asy(c, za)
            za = f + c
            reka.append(c)
            print("na ręce masz " + str(reka) + " wynki na ręce to " + str(za))
            if za < 21:
                n = input("czy chcesz dobrać kartę?(tak/nie)"+"\n")
                if n =="tak":
                    d = random.randint(2, 11)
                    zb = za + d
                    asy(d, zb)
                    zb = za + d
                    reka.append(d)
                    print("na ręce masz " + str(reka) + " wynik na ręce to " + str(zb))
                    if zb < 21:
                        z = input("czy chcesz dobrać kartę?(tak/nie)"+"\n")
                        if z =="tak":
                            e = random.randint(2, 11)
                            zc = zb + e
                            asy(e, zc)
                            zc = zb + e
                            reka.append(e)
                            print("na ręce masz " + str(reka) + " wynik na ręce to " + str(zc))
                            if zc < 21:
                                x = input("czy chcesz dobrać kartę?(tak/nie)"+"\n")
                                if x=="tak":
                                    g=random.randint(2,11)
                                    zd=zc+g
                                    asy(g, zd)
                                    zd=zc+g
                                    print("na ręce masz " + str(reka) + " wynik na ręce to " + str(zd))
                                    if zd<21:
                                        y = input("czy chcesz dobrać kartę?(tak/nie)" + "\n")
                                        if y=="tak":
                                            f = 100                          #dodać więcej
                                        elif y == "nie":
                                            print()
                                        else:
                                            print("błędna wartość")
                                elif x == "nie":
                                    print()
                                else:
                                    print("błędna wartość")
                        elif z == "nie":
                            print()
                        else:
                            print("błędna wartość")
                elif n == "nie":
                    print()
                else:
                    print("błędna wartość")
        elif m == "nie":
            print()
        else:
            print("błędna wartość")
    return f


def dobieranie_dealer(f):
    if f < 21:
        c = random.randint(2, 11)
        f = f + c
        asy(c, f)
        f = f + c
        reka_stół.append(c)
        if f < 21:
            d = random.randint(2, 11)
            f = f + d
            asy(c, f)
            f = f + d
            reka_stół.append(d)
            if f < 21:
                e = random.randint(2, 11)
                f = f + e
                asy(e, f)
                reka_stół.append(e)
                if f < 21:
                    f == 100
    return f


def wyniki(f, fd):
    win=0
    if f == 21:
        win = 3
    elif f < 21 and fd > 21:
        win = 1
    elif f > 21:
        win = 0


    return win


def wygrana(win, bank, cash):
    if win == 1:
        print("wygrana")
        bank = int(cash) + int(bank)
    if win == 3:
        bank = int((int(bank) *3) / 2)+int(bank)
        print("BLACKJACk")
    if win >= 1:
        cash = int(cash) + int(bank)
        print("obecny stan konta"+ "\n" + str(cash))
    if win < 1:
        cash = int(cash)- int(bank)
        print("przegrana")
        print("obecny stan konta"+ "\n" + str(cash))
    return cash


def BlackJack(cash):
    print("-----------------------------------")
    bank = input("ile chcesz postawić"+"\n" )
    if bank > cash:
        print("zła watrość")
    else:
        print("grajmy zatem")
        print("--------------------------------------")
        f = BlackJack_gracz()
        fd=Blackjack_dealer()
        wyniki(f, fd)
        wygrana(wyniki(f, fd), bank, cash)


# Ruletka
def ruletka_los():
    r=random.randint(0,36)
    return r
def ruletka_obst():
    global zak2
    zak1=input("na co chcesz obstawić liczbę, kolor, zakład specjalny? ")
    if zak1 == "liczba":
        zak2=input("jaka to ma być liczba w zakresie od 0 do 36")
    if zak1 == "kolor":
        zak2=input("jaki to ma być kolor")
    if zak1 == "zakład specjalny":
        zakp=input("jaki to zakład?"+"\n"+"1., 2. lub 3. 12 wpisz 12, 2 numery wpisz 2,3 numery wpisz 3, 4 numery wpisz 4, 1. 5 numerów wpisz 5 "+"\n"+"kolumny, linie, parzyste, nieparzyste")
        zaklady_spec(zakp)
    return zak2

def zaklady_spec(zakp):
    if zakp == "12":
        zak2 = input("która to ma być 12")
    if zakp == "2":
        zak2 = input("które to mają byc liczby")
    if zakp == "3":
        zak2 = input("które to mają być liczby")
    if zakp == "4":
        zak2 = input("które to mają być liczby")
    if zakp == "5":
        zak2 = [0, 1, 2, 3, 4]
    if zakp == "kolumny":
        zak2 = input("która to ma być kolumna")
    if zakp == "linie":
        zak2 = input("która to ma byc linia")
    if zakp == "parzyste":
        zak2="parzyste"
    if zakp == "nieparzyste":
        zak2="nieparzyste"


    return zak2

def rsprawdzenie(zak2, r):
    if zak2==0:
        print()

def ruletka(cash):
    print("-----------------------------------")
    bank = input("ile chcesz postawić" + "\n")
    if bank > cash:
        print("zła watrość")


# kości
def dice(cash):
    random.randint()


# część główna
gra = input("w co chcesz grać blackjack ruletka kości"+"\n")
if gra == "blackjack":
    BlackJack(cash)
elif gra == "ruletka":
    ruletka(cash)
elif gra == "kości":
    dice(cash)
else:
    print("ERROR 404")
