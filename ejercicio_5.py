resultado : int = 1
if __name__ == "__main__":
    exp = int(input("Ingrese un exponente para la base 2:  "))
    if exp > 0:
        for i in range (1, exp+1, 1):
            resultado *=2
        print(f"2 ^ {i} = {resultado}")
    elif exp < 0:
        for i in range (1, (-exp+1), 1):
            resultado *= 2
            pot_neg = 1 / resultado
        print(f"2 ^ {-i} = {pot_neg}")
    else:
        print ( "2 ^ 0 = 1")