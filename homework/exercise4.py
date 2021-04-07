def main():
    num = int(input("Podaj liczbe: "))
    divisors = []
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)
    print(f"Dzielniki liczby {num} to {divisors}")

if __name__ == '__main__':
    main()