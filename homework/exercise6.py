def main():
    print("Wprowadz tablice do sprawdzenia(przykład: 10 50 60 20), czy liczby mieszcza sie w zakresie <10; 50>")
    table = list(map(int, input().strip().split()))
    numbers = []
    for i in table:
        if not i <= 50 or not i >= 10:
            numbers.append(i)
    if not numbers:
        print("Wszystkie elementy mieszcza sie w zakresie <10; 50>")
    else:
        print(f"{numbers} nie należą do przedziału")


if __name__ == '__main__':
    main()