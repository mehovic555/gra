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
parzyste=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
nieparzyste=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
czarne=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
czerwone=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
t5=[0,1,2,3,4]
k1=[1,4,7,10,13,16,19,22,25,28,31,34]
k2=[2,5,8,11,14,17,20,23,26,29,32,35]
k3=[3,6,9,12,15,18,21,24,27,30,33,36]
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
l4=[10,11,12]
l5=[13,14,15]
l6=[16,17,18]
l7=[19,20,21]
l8=[22,23,24]
l9=[25,26,27]
l10=[28,29,30]
l11=[31,32,33]
l12=[34,35,36]
p12=[1,2,3,4,5,6,7,8,9,10,11,12]
d12=[13,14,15,16,17,18,19,20,21,22,23,24]
t12=[25,26,27,28,29,30,31,32,33,34,35,36]
p18=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
d18=[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

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
        zakp=input("jaki to zakład?"+"\n"+"1., 2. lub 3. 12 wpisz 12, 2 numery wpisz 2,3 numery wpisz 3, 4 numery wpisz 4, 1. 5 numerów wpisz 5 "+"\n"+"kolumny, linie, parzyste, nieparzyste, 1. lub 2. 18")
        zaklady_spec(zakp)
    return zak2

def zaklady_spec(zakp):
    global zak2
    if zakp==12:
        zak2=input("która to 12 wpisz 12 i swoją liczbę")
    if zakp == 18:
        zak2 = input("która to 18 wpisz 18 i swoją liczbę")
    if zakp == 2:
        zakp2 = input("które to liczvy wpisz 22 i swoją liczbę")
        for i in range(2):
            zak2.append(zakp2)
    if zakp == 3:
        zakp2 = input("które to liczvy wpisz 33 i swoją liczbę")
        for i in range(3):
            zak2.append(zakp2)
    if zakp == 4:
        zakp2 = input("które to liczvy wpisz 44 i swoją liczbę")
        for i in range(4):
            zak2.append(zakp2)
    if zakp == 5:
        zak2=5
    if zakp == "kolumny":
        zak2 = input("która to ma być kolumna napisz 13 i swoją liczbę ")
    if zakp == "linie":
        zak2 = input("która to ma byc linia napisz 144 i do tego dodaj swoją linię")
    if zakp == "parzyste":
        zak2="parzyste"
    if zakp == "nieparzyste":
        zak2="nieparzyste"


    return zak2

def rsprawdzenie(zak2, r):
    global win
    z=0
    if zak2>=0 and zak2<=36:
        if zak2==r:
            win=35
    if zak2==str:
        if zak2=="parzyste":
            for i in range(36):
               if parzyste==r:
                   z+=1
            if z==1:
                win=1
        elif zak2 =="nieparzyste":
            for i in range(36):
                if nieparzyste==r:
                    z+=1
            if z==1:
                win=1
        elif zak2=="czerwone":
            for i in range(18):
                if czerwone==r:
                    z+=1
            if z==1:
                win=1
        elif zak2=="czarne":
            for i in range(18):
                if czarne==r:
                    z+=1
            if z==1:
                win=1
    if zak2>130 and zak2<140:#kolumna 2:1
        a=130-int(zak2)
        if a==1:
            for i in range(12):
                if k1==r:
                    z+=1
            if z==1:
                win=2
        if a==2:
            for i in range(12):
                if k2==r:
                    z+=1
            if z==1:
                win=2
        if a==3:
            for i in range(12):
                if k3==r:
                    z+=1
            if z==1:
                win=2

    if zak2>1440 and zak2<1460:#linia 5:1
        a=1440-int(zak2)
        if a==1:
            for i in range(3):
                if l1==r:
                    z+=1
            if z==1:
                win=5
        if a==2:
            for i in range(3):
                if l2==r:
                    z+=1
            if z==1:
                win=5
        if a==3:
            for i in range(3):
                if l3==r:
                    z+=1
            if z==1:
                win=5
        if a==4:
            for i in range(3):
                if l4==r:
                    z+=1
            if z==1:
                win=5
        if a==5:
            for i in range(3):
                if l5==r:
                    z+=1
            if z==1:
                win=5
        if a==6:
            for i in range(3):
                if l6==r:
                    z+=1
            if z==1:
                win=5
        if a==7:
            for i in range(3):
                if l7==r:
                    z+=1
            if z==1:
                win=5
        if a==8:
            for i in range(3):
                if l8==r:
                    z+=1
            if z==1:
                win=5
        if a==9:
            for i in range(3):
                if l9==r:
                    z+=1
            if z==1:
                win=5
        if a==10:
            for i in range(3):
                if l10==r:
                    z+=1
            if z==1:
                win=5
        if a==11:
            for i in range(3):
                if l11==r:
                    z+=1
            if z==1:
                win=5
        if a==12:
            for i in range(3):
                if l12==r:
                    z+=1
            if z==1:
                win=5

    if zak2>120 and zak2<130:#2:1
        a=120-int(zak2)
        if a==1:
            for i in range(12):
                if p12==r:
                    z+=1
            if z==1:
                win=2
        if a==2:
            for i in range(12):
                if d12==r:
                    z+=1
            if z==1:
                win=2
        if a==3:
            for i in range(12):
                if t12==r:
                    z+=1
            if z==1:
                win=2

    if zak2>180 and zak2<190:#1:1
        a=180-int(zak2)
        if a==1:
            for i in range(18):
                if p18==r:
                    z+=1
            if z==1:
                win=1
        if a==2:
            for i in range(18):
                if d18==r:
                    z+=1
            if z==1:
                win=1

    if zak2>220 and zak2<230:#17:1
        a=220-int(zak2)
    if zak2>330 and zak2<340:#11:1
        a=330-int(zak2)
    if zak2>440 and zak2<450:#8:1
        a=440-int(zak2)
    if zak2==5:
        for i in range(5):
            if t5 == r:
                z += 1
        if z == 1:
            win = 1
    if z==0:
        win=0
    return win

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
