def main():
    a = float(input("Podaj dlugość 1 boku: "))
    b = float(input("Podaj dlugość 2 boku: "))
    if a > 0 and b > 0:
        result = (a ** 2 + b ** 2) ** (0.5)
        print(f"Długość przeciwprostokątnej: {result}")

main()