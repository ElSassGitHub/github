def lireFichier(name:str):
    ls = []
    with open(name, 'r') as f:
        for l in f:
            l = l.rstrip("\n\r")
            ls.append(l)
    return ls

def main():
    file = input("Entrez le nom d'un fichier : ")
    try:
        result = lireFichier(file)
    except PermissionError as err:
        print(f"ERREUR '{err}' : vous ne pouvez pas lire le fichier")
    except FileNotFoundError as err:
        print(f"ERREUR '{err}' : le fichier n'existe pas")
    except FileExistsError as err:
        print(f"ERREUR '{err}' : le fichier existe déjà")
    except IOError as err:
        print(f"ERREUR '{err}' : une erreur d'entrée/sortie est survenue")
    else:
        print("\n".join(result))
    finally:
        print("Le programme est terminé")

if __name__ == '__main__':
    main()