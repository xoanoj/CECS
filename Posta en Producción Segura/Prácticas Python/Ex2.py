'''
    Escribe un programa que simule un xogo onde se tira un dado. Simula que se fan dúas tiradas do dado, mostra por pantalla os valores obtidos e indica se o maior é o primeiro ou o segundo, ou se hai empate.
'''

import random as r

def throwDice():
    MIN_INT = 1
    MAX_INT = 20

    return [r.randrange(MIN_INT,MAX_INT),r.randrange(MIN_INT,MAX_INT)]

def checkDice():
    
    results = throwDice()
    
    if results[0] > results[1]:

        print(f"{str(results[0])}>{str(results[1])}")

    elif results[0] == results[1]:

        print(f"{str(results[0])}={str(results[1])}")

    else:

        print(f"{str(results[0])}<{str(results[1])}")


if __name__ == '__main__':
    checkDice()
