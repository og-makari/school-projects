def main():
    print("Podaj dwie liczby\n")
    a = int(input("Podaj 1 liczbe: "))
    b = int(input("Podaj 2 liczbe: "))
    for i in range(a, b+1):
        print(i)

if __name__ == '__main__':
    main()