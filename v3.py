#11.	Napiši program, ki omogoči vnos nekega znaka. Program naj ugotovi, ali je prebrani znak mala ali velika črka angleške abecede ali pa nek drug simbol. Ustrezno ugotovitev naj izpiše.
"""
def male_velike_crke(znak):
    if znak >= "A" and znak <= "Z" or znak in "ČŠŽ":
        print("Velika črka")
    if znak >= "a" and znak <= "z" or znak in "čšž":
        print("Mala črka")
    else: print("nek drug znak")
"""
#12.	Napiši program, ki predstavlja preprost kalkulator, ki zna seštevati, odštevati, množiti in deliti. Sestavi preprost meni v obliki:
#»Izberi s pritiskom na tipko:«
#»A – seštevanje«
#»B – odštevanje«
#»C – množenje«
#»D – deljenje«
#Vhodne podatke naj uporabnik vnese pred izbiro operacije, vsebina posamezne izbire naj bo izračun rezultata, izpis rezultata pa naj bo na koncu programa.
#Če uporabnik izbere tipko, ki ni na meniju, naj program javi napačen vnos.
"""
def kalkulator():
    st1 = int(input("Vnesite prvo število: "))
    st2 = int(input("Vnesite drugo število: "))
    c = str(input("Vnesite črko katro želite: "))

    if c == "A":
        print(st1+st2)
    elif c == "B":
        print(st1-st2)
    elif c == "C":
        print(st1*st2)
    elif c == "D":
        print(st1/st2)

    else :
        print("napačen vnos")
"""

def main():
    i = 0
    vnos=int(input("Vnesite neko število: "))
    print("1", end = " ")
    while i < 5:
        if vnos % 2 == 0:
            print("2", end= " ")
        i = i + 1
    if vnos % 2 == 0:
        print("2", end=" ")
    if vnos % 3 == 0:
        print("3", end=" ")
    if vnos % 4 == 0:
        print("4", end=" ")
    if vnos % 5 == 0:
        print("5", end=" ")
    if vnos % 6 == 0:
        print("6", end=" ")

    






      
if __name__== "__main__":
    main()