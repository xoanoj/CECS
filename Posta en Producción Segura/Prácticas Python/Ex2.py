'''
    Escribe un programa que simule un xogo onde se tira un dado. Simula que se fan dúas tiradas do dado, mostra por pantalla os valores obtidos e indica se o maior é o primeiro ou o segundo, ou se hai empate.
'''

import random as r

def throwDice():

    return [r.randrange(1,6),r.randrange(1,6)]

def checkDice():
    
    results = throwDice()
    
    if results[0] > results[1]:

        print(str(results[0])+'>'+str(+results[1]))

    elif results[0] == results[1]:

        print(str(results[0])+'='+str(results[1]))

    else:

        print(str(results[0])+'<'+str(results[1]))


if __name__ == '__main__':
    checkDice()
