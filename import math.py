import math

print("Pole i obwód figur")

inp = input("Napisz \"start\" żeby zacząć: ").lower().strip()

if inp == "start":
    print("Płaskie - a Bryły - b Dodatkowe wzory - c")
    inp = input("Wybierz: ").lower().strip()

    if inp == "a":
        print("Płaskie figury:")
        print("a - kwadrat")
        print("b - prostokąt")
        print("c - równoległobok")
        print("d - trójkąt")
        print("e - trapez")
        print("f - romb")
        print("g - koło")
        print("h - trójkąt prostokątny")

        inp = input("Wybierz figurę: ").lower().strip()

        if inp == "a":
            print("Kwadrat")
            inp = input("Pole czy obwód?(p/o) ").lower().strip()

            if inp == "p":
                a = float(input("Podaj a = "))
                print("Pole kwadratu =", a * a)

            elif inp == "o":
                a = float(input("Podaj a = "))
                print("Obwód kwadratu =", 4 * a)

            else:
                print("Nie ma takiej komendy")

        elif inp == "b":
            print("Prostokąt")
            inp = input("Pole czy obwód?(p/o) ").lower().strip()

            if inp == "p":
                a = float(input("Podaj a = "))
                b = float(input("Podaj b = "))
                print("Pole prostokąta =", a * b)

            elif inp == "o":
                a = float(input("Podaj a = "))
                b = float(input("Podaj b = "))
                print("Obwód prostokąta =", 2 * a + 2 * b)

            else:
                print("Nie ma takiej komendy")

        elif inp == "c":
            print("Równoległobok")
            inp = input("Pole czy obwód?(p/o) ").lower().strip()

            if inp == "p":
                a = float(input("Podaj a = "))
                h = float(input("Podaj h = "))
                print("Pole równoległoboku =", a * h)

            elif inp == "o":
                a = float(input("Podaj a = "))
                b = float(input("Podaj b = "))
                print("Obwód równoległoboku =", 2 * a + 2 * b)

            else:
                print("Nie ma takiej komendy")

        elif inp == "d":
            print("Trójkąt")
            inp = input("Pole czy obwód?(p/o) ").lower().strip()

            if inp == "p":
                a = float(input("Podaj a = "))
                h = float(input("Podaj h = "))
                print("Pole trójkąta =", a * h / 2)

            elif inp == "o":
                a = float(input("Podaj a = "))
                b = float(input("Podaj b = "))
                c = float(input("Podaj c = "))
                print("Obwód trójkąta =", a + b + c)

            else:
                print("Nie ma takiej komendy")

        elif inp == "e":
            print("Trapez")
            inp = input("Pole czy obwód?(p/o) ").lower().strip()

            if inp == "p":
                a = float(input("Podaj a = "))
                b = float(input("Podaj b = "))
                h = float(input("Podaj h = "))
                print("Pole trapezu =", (a + b) * h / 2)

            elif inp == "o":
                a = float(input("Podaj a = "))
                b = float(input("Podaj b = "))
                c = float(input("Podaj c = "))
                d = float(input("Podaj d = "))
                print("Obwód trapezu =", a + b + c + d)

            else:
                print("Nie ma takiej komendy")

        elif inp == "f":
            print("Romb")
            inp = input("Pole czy obwód?(p/o) ").lower().strip()

            if inp == "p":
                e = float(input("Podaj e = "))
                f = float(input("Podaj f = "))
                print("Pole rombu =", e * f / 2)

            elif inp == "o":
                a = float(input("Podaj a = "))
                print("Obwód rombu =", 4 * a)

            else:
                print("Nie ma takiej komendy")

        elif inp == "g":
            print("Koło")
            inp = input("Pole czy obwód?(p/o) ").lower().strip()

            if inp == "p":
                r = float(input("Podaj r = "))
                print("Pole koła =", math.pi * r * r)

            elif inp == "o":
                r = float(input("Podaj r = "))
                print("Obwód koła =", 2 * math.pi * r)

            else:
                print("Nie ma takiej komendy")

        elif inp == "h":
            print("Trójkąt prostokątny")
            a = float(input("Podaj a = "))
            b = float(input("Podaj b = "))

            print("Pole trójkąta prostokątnego =", a * b / 2)

        else:
            print("Nie ma takiej figury")

    elif inp == "b":
        print("Bryły:")
        print("a - sześcian")
        print("b - prostopadłościan")
        print("c - graniastosłup")
        print("d - ostrosłup")
        print("e - walec")
        print("f - stożek")
        print("g - kula")

        inp = input("Wybierz bryłę: ").lower().strip()

        if inp == "a":
            print("Sześcian")
            inp = input("Pole czy objętość?(p/o) ").lower().strip()

            if inp == "p":
                a = float(input("Podaj a = "))
                print("Pole powierzchni sześcianu =", 6 * a * a)

            elif inp == "o":
                a = float(input("Podaj a = "))
                print("Objętość sześcianu =", a * a * a)

            else:
                print("Nie ma takiej komendy")

        elif inp == "b":
            print("Prostopadłościan")
            inp = input("Pole czy objętość?(p/o) ").lower().strip()

            if inp == "p":
                a = float(input("Podaj a = "))
                b = float(input("Podaj b = "))
                c = float(input("Podaj c = "))
                print("Pole powierzchni prostopadłościanu =",
                      2 * a * b + 2 * a * c + 2 * b * c)

            elif inp == "o":
                a = float(input("Podaj a = "))
                b = float(input("Podaj b = "))
                c = float(input("Podaj c = "))
                print("Objętość prostopadłościanu =", a * b * c)

            else:
                print("Nie ma takiej komendy")

        elif inp == "c":
            print("Graniastosłup")
            inp = input("Pole czy objętość?(p/o) ").lower().strip()

            if inp == "p":
                pp = float(input("Podaj pole podstawy = "))
                pb = float(input("Podaj pole boczne = "))
                print("Pole powierzchni graniastosłupa =", 2 * pp + pb)

            elif inp == "o":
                pp = float(input("Podaj pole podstawy = "))
                h = float(input("Podaj wysokość = "))
                print("Objętość graniastosłupa =", pp * h)

            else:
                print("Nie ma takiej komendy")

        elif inp == "d":
            print("Ostrosłup")
            inp = input("Pole czy objętość?(p/o) ").lower().strip()

            if inp == "p":
                pp = float(input("Podaj pole podstawy = "))
                pb = float(input("Podaj pole boczne = "))
                print("Pole powierzchni ostrosłupa =", pp + pb)

            elif inp == "o":
                pp = float(input("Podaj pole podstawy = "))
                h = float(input("Podaj wysokość = "))
                print("Objętość ostrosłupa =", pp * h / 3)

            else:
                print("Nie ma takiej komendy")

        elif inp == "e":
            print("Walec")
            inp = input("Pole czy objętość?(p/o) ").lower().strip()

            if inp == "p":
                r = float(input("Podaj r = "))
                h = float(input("Podaj h = "))
                print("Pole powierzchni walca =",
                      2 * math.pi * r * r + 2 * math.pi * r * h)

            elif inp == "o":
                r = float(input("Podaj r = "))
                h = float(input("Podaj h = "))
                print("Objętość walca =", math.pi * r * r * h)

            else:
                print("Nie ma takiej komendy")

        elif inp == "f":
            print("Stożek")
            inp = input("Pole czy objętość?(p/o) ").lower().strip()

            if inp == "p":
                r = float(input("Podaj r = "))
                l = float(input("Podaj l = "))
                print("Pole powierzchni stożka =",
                      math.pi * r * r + math.pi * r * l)

            elif inp == "o":
                r = float(input("Podaj r = "))
                h = float(input("Podaj h = "))
                print("Objętość stożka =", math.pi * r * r * h / 3)

            else:
                print("Nie ma takiej komendy")

        elif inp == "g":
            print("Kula")
            inp = input("Pole czy objętość?(p/o) ").lower().strip()

            if inp == "p":
                r = float(input("Podaj r = "))
                print("Pole powierzchni kuli =", 4 * math.pi * r * r)

            elif inp == "o":
                r = float(input("Podaj r = "))
                print("Objętość kuli =", 4 * math.pi * r * r * r / 3)

            else:
                print("Nie ma takiej komendy")

        else:
            print("Nie ma takiej bryły")

    elif inp == "c":
        print("Dodatkowe wzory:")
        print("a - Twierdzenie Pitagorasa")
        print("b - przekątna kwadratu")
        print("c - wysokość trójkąta równobocznego")

        inp = input("Wybierz wzór: ").lower().strip()

        if inp == "a":
            print("Twierdzenie Pitagorasa")

            a = float(input("Podaj a = "))
            b = float(input("Podaj b = "))

            c = (a * a + b * b) ** 0.5

            print("Przeciwprostokątna c =", c)

        elif inp == "b":
            print("Przekątna kwadratu")

            a = float(input("Podaj a = "))

            d = a * 2 ** 0.5

            print("Przekątna kwadratu =", d)

        elif inp == "c":
            print("Wysokość trójkąta równobocznego")

            a = float(input("Podaj a = "))

            h = a * 3 ** 0.5 / 2

            print("Wysokość trójkąta równobocznego =", h)

        else:
            print("Nie ma takiego wzoru")

    else:
        print("Nie ma takiej komendy")

else:
    print("Nie ma takiej komendy")