def main():
    height = int(input('Podaj wysokość piramidy: '))
    for i in range(1, height+1):
        print(" " * (height-i) + "# " * i)

main()