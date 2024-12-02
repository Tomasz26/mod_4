import sys
import logging
logging.basicConfig(level=logging.DEBUG)

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

def getvalue12(user_input):
    while True:
        try:
            value = float(input(user_input))
            return value
        except:
            logging.debug("Program przyjmuje tylko liczby, spróbuj ponownie:")

if operation == 1 or 2:
    x = getvalue12("Podaj składnik 1: ")
    y = getvalue12("Podaj składnik 1: ")
    z = getvalue12("Podaj składnik 3: ")
        
else:
    x = input("Podaj składnik 1: ")
    y = input("Podaj składnik 2: ")

