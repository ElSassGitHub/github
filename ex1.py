def divEntier(x:int, y:int) -> int:
    if (x < 0) or (x is not int) or (y < 0) or (y is not int):
        raise ValueError
    elif y == 0:
        raise RecursionError
    else:
        if x < y:
            return 0
        else:
            x -= y
            return divEntier(x,y) +1

def main():
    try:
        x = int(input("Entrez la valeur de x: "))
        y = int(input("Entrez la valeur de y: "))
        result = divEntier(x,y)
    except RecursionError as err:
        print(f"ERREUR : y est égale à 0")
    except ValueError as err:
        print(f"ERREUR : un des nombres n'est pas un int positif")
    else:
        print(result)

if __name__ == '__main__':
    main()