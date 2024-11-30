def check_if_palindrom(x):
    # Checks if given word is a palindorme
    # Argument should be a single word
    
    x = x.lower() #making all letters lower
    y = 0
    z = len(x) - 1
    while y < z:

        if x[y] != x[z]:
            print(False)
            return
            
        y += 1
        z -= 1

    print(True)

check_if_palindrom('Kajak')
check_if_palindrom('ala')
check_if_palindrom('hello')