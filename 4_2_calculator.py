import sys
import logging
logging.basicConfig(level=logging.DEBUG)

while True:
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    if operation in ['1', '2', '3', '4']:
        operation = int(operation)
        break
    else:
        logging.debug("Proszę wpisać liczbę 1, 2, 3 lub 4 zgodnie z instrukcją, spróbuj ponownie.")

def getvalue(user_input):
    #Funkcja pobierania wartości od użytkownika
    while True:
        try:
            value = float(input(user_input))
            return value
        except:
            logging.debug("Program przyjmuje tylko liczby, spróbuj ponownie:")

if operation == 1 or 2:
    x = getvalue("Podaj składnik 1: ")
    y = getvalue("Podaj składnik 2: ")
    z = getvalue("Podaj składnik 3: ")
        
else:
    x = getvalue("Podaj składnik 1: ")
    y = getvalue("Podaj składnik 2: ")



