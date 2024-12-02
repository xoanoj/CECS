'''
 Hai varias APIs dispoñibles que permite obter a ratio de conversión entre dous tipos de moedas. 
 Por exemplo, pode facerse unha petición á URL 
 [http://freecurrencyrates.com/api/action.php?do=cvals\&iso=usd\&f=eur\&v=1\&s=cbr](http://freecurrencyrates.com/api/action.php?do=cvals&iso=usd&f=eur&v=1&s=cbr) 
 para obter a ratio de conversión de USD a EUR.
'''

import requests,json

def fetch_rate():

    return json.loads(
        requests.get("http://freecurrencyrates.com/api/action.php?do=cvals&iso=usd&f=eur&v=1&s=cbr").text
        )['USD']

def get_euros():

    return int(input("Enter EUR to convert to USD: "))

def convert_euros_to_usd():

    return get_euros()*fetch_rate()

if __name__ == "__main__":
    
    print(f"{str(convert_euros_to_usd())} USD")