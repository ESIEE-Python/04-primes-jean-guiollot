'''
cette fonction sert a conaitre les nombre premier
'''
from math import sqrt



def isprime(p):
    '''
    retoourne un boléin qui indique et indique si ce nombre est premier ou non

    arg p valeur entière positive

    return boléin objectif true false
    '''
    for k in range(2,int(sqrt(p)+1)) :
        if p%k == 0 :
            return False
    return True


#### Fonction principale


def main():
    '''
    test de la fonction jusqu'a 99

    arg :
        None
    
    return :
        None
    '''
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
