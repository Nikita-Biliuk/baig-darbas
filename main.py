# Boulingo taškų skaičiuoklė
import sys


# Tikrinama, ar 1 metimas yra skaičius
def is_number(metimas1):
    try:
        int(metimas1)
    except ValueError:
        print("Neteisingai ivestas 1 metimas")
        sys.exit()

# Tikrinama, ar 2 metimas yra skaičius
def is_number2(metimas2):
    try:
        int(metimas2)
    except ValueError:
        print("Neteisingai ivestas 2 metimas")
        sys.exit()

# Tikrinama, ar papildomas metimas yra skaičius
def is_number3(pap_metimas):
    try:
        int(pap_metimas)
    except ValueError:
        print("Neteisingai ivestas papildomas metimas")
        sys.exit()






# Programa skaiciuojanti taskus
def boulingas():
    f = 0
    s = 0
    metimai = 0
    metimas = []

    while f < 10:

        # Taškų įvedimas už 1 metimą
        metimai += 1
        f += 1
        print(f"Freimas: {f}")
        metimas1 = input(f"Metimas 1: ")

        # Straiko patikrinimas
        if metimas1 == "x":
            metimas.append(metimas1)
            print("Straikas!")
            s += 10
            print(f"Jusu taskai: {s}")

            if f > 1:

                # Tasku pridejimas uz spara ar straika
                if f > 2:
                    if metimas[metimai-2] == "x" or metimas[metimai-2] == "/":
                        s += 10

                if metimas[metimai-3] == "x":
                    s += 10
                    print(f"Jusu taskai pridejus papildomus taskus uz straikus/sparus: {s}")

        # Prazangos patikrinimas(žengimas ant linijos)
        elif metimas1 == "F":
            metimas.append(metimas1)
            print("Folas!")
            if f > 1:
                if metimas[metimai - 2] == "x" or metimas[metimai - 2] == "/":
                    s += 0

                if metimas[metimai - 3] == "x":
                    s += 0

            # 2 Metimas jeigu per 1 metima padarita prazanga
            metimas2 = input(f"Metimas 2: ")
            metimas.append(metimas2)
            metimai += 1

            if metimas2 == "/":
                print("Sparas!")
                s += 10

                if metimas[metimai - 3] == "x":
                    s += 10 - int(metimas1)
                print(f"Jusu taskai: {s}")

            else:
                if int(metimas2) > 10:
                    print("Klaidingai ivestas tasku skaicius uz 2 metima!")
                    break

                else:
                    s += int(metimas2)

                    if metimas[metimai - 3] == "x":
                        s += int(metimas2)
                    print(f"Jusu taskai: {s}")

        else:

                is_number(metimas1)
                metimas.append(metimas1)

                # Tikrinama, ar teisingai įvestas taškų skaičius už 1 metimą
                if int(metimas1) > 9 or int(metimas1) < 0:
                    print("Klaidingai ivestas tasku skaicius uz 1 metima!")
                    break
                if int(metimas1) > 9 or int(metimas1) < 0:
                    print("Klaidingai ivestas tasku skaicius uz 1 metima!")
                    break

                # Taškai pelnomi iš 1 metimo už ankstesnius straikus
                if metimas[metimai-2] == "x" or metimas[metimai-2] == "/":
                    s += int(metimas1)
                    print(f"Jusu taskai pridejus papildomus taskus uz straikus/sparus: {s}")
                if f > 1:
                    if metimas[metimai-3] == "x":
                        s += int(metimas1)
                        print(f"Jusu taskai pridejus papildomus taskus uz straikus/sparus: {s}")

                #2 metimas
                metimas2 = input(f"Metimas 2: ")
                metimas.append(metimas2)
                metimai += 1

                if metimas2 == "/":
                    print("Sparas!")
                    s += 10

                    if metimas[metimai-3] == "x":
                        s += 10 - int(metimas1)
                    print(f"Jusu taskai pridejus papildomus taskus uz straikus/sparus: {s}")

                else:
                    is_number2(metimas2)
                    if int(metimas1) + int(metimas2) > 10:
                        print("Klaidingai ivestas tasku skaicius uz 2 metima!")
                        break

                    else:
                        s += int(metimas1) + int(metimas2)
                        print(f"Jusu taskai: {s}")
                        if metimas[metimai-3] == "x":
                            s += int(metimas2)
                        print(f"Jusu taskai pridejus papildomus taskus uz straikus/sparus: {s}")

        # Papildomi metimai
        if f == 10:
            a = metimas[metimai-2]
            b = metimas[metimai-1]
            if b == "x":
                pap_metimas = input(f"Papildomas metimas: ")

                if a == "x":
                    s += 10

                if pap_metimas == "x":
                    s += 10

                else:
                    is_number3(pap_metimas)
                    s += int(pap_metimas)
                pap_metimas = input(f"Papildomas metimas: ")

                if pap_metimas == "x":
                    s += 10
                else:
                    s += int(pap_metimas)

            if b == "/":
                pap_metimas = input(f"Papildomas metimas: ")

                if pap_metimas == "x":
                    s += 10

                else:
                    is_number3(pap_metimas)
                    s += int(pap_metimas)

    return f"Jus surinkote: {s} tasku"


print(boulingas())
