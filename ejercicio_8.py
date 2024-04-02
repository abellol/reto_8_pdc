import math
def exponencial_aproximada(x : int, n : int) -> float:
    suma : float = 0
    for i in range (0,n+1):
        nume = (x**i)
        deno = 1
        for num in range (1, i+1):
            deno *= num
        termino = nume/deno
        suma += termino
    return suma
def margen_error(real : float, aprox : float) -> float:
    error : float = (abs(real - aprox)/real) *100
    return error
if __name__ == "__main__":
    x = int(input("Ingrese un numero para que sea el exponente de la función:  "))
    porcentaje_error = float(input("Ingrese el porcentaje de error al que desea aproximarse (sin el %):  "))
    real= math.exp(x)
    bandera = True
    while bandera: 
        for i in range (1, 100):
            aprox = exponencial_aproximada(x, i)
            error = margen_error(real, aprox)
            if error < porcentaje_error:
                print(f"el valor estimado de la funcion e ^ {x} = {aprox}")
                print(f"el valor real de la funcion e ^ {x} = {real}")
                print (f"al sumar {i} terminos de la serie, el error es del {error}% y es menor al {porcentaje_error}%")
                bandera = False
                break
            else:
                continue
            