x: int = 1
if __name__ == "__main__":
    n = int(input("ingrese un numero para hallar su factorial:  "))
    for num in range (1, n+1, 1):
        x=x*num
        print(f"{num}! = {x}")