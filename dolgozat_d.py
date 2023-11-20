def feladat_1():
    for i in range(120, 211):
        print(i, " ")


def feladat_2():
    tort = float(input("Kérek egy tört számot: "))
    while not ((tort < 0) and (0 > tort) and (tort > -10)):
        tort = float(input("Hibás! Kérek egy tört számot: "))
    print("Ügyes vagy!")


def feladat_3():
    szam = int(input("Kérek egy számot: "))
    if szam % 2 == 1:
        for i in range(szam, 7, -2):
            print(i, end=" ")
    else:
        szam += 1
        for i in range(7):
            print(i, end=" ")


def feladat_4():
    db = 0
    for i in range(7):
        szoveg = input("Kérek be szöveget: ")
        b = szoveg.rfind("b")
        print(b)
        db = db + b
    print(f"Ennyi db {db} b betű van a szövegbe.")
