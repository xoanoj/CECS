'''
    Crea unha función que reciba como parámetro unha cadea é devolva true se se pode convertir a un número enteiro e false en caso contrario.
'''

user_inpt = input("Input string: \n")

try:

    user_input = int(user_inpt)
    print(f"Conversion: {str(user_inpt)}")

except Exception as error:
    print(f"Conversion failed [{error}]")