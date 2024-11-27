'''
    Crea un programa co alfabeto NATO ou radiofónico tal que, dada unha palabra imprima por pantalla cada letra da misma no alfabeto NATO.
'''

NATO_ALPH = [
    'ALPHA', 'BRAVO', 'CHARLIE', 'DELTA', 'ECHO', 'FOXTROT', 
    'GOLF', 'HOTEL', 'INDIA', 'JULIET', 'KILO', 'LIMA', 
    'MIKE', 'NOVEMBER', 'OSCAR', 'PAPA', 'QUEBEC', 'ROMEO', 
    'SIERRA', 'TANGO', 'UNIFORM', 'VICTOR', 'WHISKEY', 
    'X-RAY', 'YANKEE', 'ZULU'
]

ENG_ALPH = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

user_input = input("Add text to change to NATO notation (enlgish alphabet only): ").upper()

for i in user_input:
   
   if (i!=" "):

    print(NATO_ALPH[ENG_ALPH.index(i)] + " ")

   else:
    
    print(" ")