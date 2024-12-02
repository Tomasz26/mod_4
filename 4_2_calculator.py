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
    #Funkcja pobierania wartości od użytkownika dla odejmowania i dzielenia
    while True:
        try:
            value = float(input(user_input))
            return value
        except:
            logging.debug("Program przyjmuje tylko liczby, spróbuj ponownie:")

def getvalue13(user_input):
    #Funkcja pobierania wartości od użytkownika dla dodawania i mnożenia
    values = []
    while True:
        try:
            value = input(user_input)
            if value == 'N':
                break
            value = float(value)
            values.append(value)
        except:
            logging.debug("Program przyjmuje tylko liczby, spróbuj ponownie:")
    return values

if operation == 1 or operation == 3:
    xs = getvalue13("Wpisz kolejną wartość, jeśli chcesz zakończyć wpisz 'N':")        
else:
    x = getvalue("Podaj składnik 1: ")
    y = getvalue("Podaj składnik 2: ")

if operation == 1:
    logging.info(f"Dodaję wszystkie podane przez Ciebie wartości: {xs}.")
    wynik = sum(xs)
elif operation == 3:
    logging.info(f"Mnożę wszystkie podane przez Ciebie wartości: {xs}.")
    wynik = 1
    for v in xs:
        wynik *= v
elif operation == 2:
    logging.info(f"Od {x} odejmuję {y}.")
    wynik = x - y
elif operation == 4:
    logging.info(f"{x} dzielę przez {y}.")
    wynik = x / y

print(f"Wynik Twoich obliczeń to: {wynik}")





