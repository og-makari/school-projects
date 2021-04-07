def main():
    if isPalindrom("maciej") == True:
        print("Podane słowo jest palindromem")
    else:
        print("Podane słowo nie jest palindromem")

def isPalindrom(word):
    for i in range(len(word)):
        print(i)
        if word[i] != word[len(word)-i-1]:
            return False
    return True

main()