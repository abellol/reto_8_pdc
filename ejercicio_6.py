resultado : int = 1
if __name__ == "__main__":
    x = float (input("ingrese la base de la expresion:  "))
    n = int(input("ingrese el exponente de la expresion:  "))
    if n < 0:
        for i in range (1, -n+1, 1):
            resultado *= x
            pot_neg = 1 / resultado
        print(f"{x} ^ {-i} = {pot_neg}")
    elif n > 0:
        for i in range (1, n+1, 1):
            resultado *= x
        print(f"{x} ^ {i} = {resultado}")
    else:
        print(f"{x} ^ 0 = 1")