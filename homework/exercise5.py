def main():
    print("Wprowadz tablice do sprawdzenia(przykład: 10 50 60 20), czy liczby mieszcza sie w zakresie <10; 50>")
    table = list(map(int, input().strip().split()))
    for i in table:
        if not i <= 50 or not i >= 10:
            print("Nie wszystkie elementy mieszcza sie w zakresie <10; 50>")
            return
    print("Wszystkie elementy mieszcza sie w zakresie <10; 50>")


main()