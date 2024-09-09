from math import sqrt

#### Fonction secondaire


def isprime(p):
    i = 2
    while i < p and p % i != 0:
        i = i + 1
    if i == p :
        print(p ,": True")
    

    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
