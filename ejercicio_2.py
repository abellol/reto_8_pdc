def impar (n : int): # se define la funcion que imprime los valores impares de 1 hasta 1000
    print ("Impares")   
    for i in range(1, n+1):
        if i % 2 == 0:
            continue
        else: 
            print (i)
def par (n : int): # se define la funcion que imprime los valores pares de 1 hasta 1000
    print ("Pares")       
    for i in range (1, n+1):
        if i % 2 != 0:
            continue
        else: 
            print (i)
             
if __name__ == "__main__":
    n : int = 1000
    x = impar(n)
    y = par(n)
    print (x, y)