def main():
    print("Wprowadź liczby(format: 12351246) do obliczenia sredniej")
    table = list(input())
    average = 0
    for i in table:
        average += int(i)
    average = average / len(table)
    print(f"Średnia liczb: {round(average, 2)}")

if __name__ == '__main__':
    main()