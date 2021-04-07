def main():
    a = int(input("Podaj 1 bok: "))
    b = int(input("Podaj 2 bok: "))
    c = int(input("Podaj 3 bok: "))
    if a+b>=c and b+c>=a and c+a>=b:
        print("Można zbudować trójkąt")
    else:
        print("Nie można zbudować trójkąta")

main()