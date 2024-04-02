import math
def seno_aproximada(x : float, n : int) -> float:
    suma : float = 0
    for i in range (0,n+1):
        arg = 2 * i + 1
        num = (-1)**i *(x**(arg))
        deno = 1
        for j in range (1, arg + 1):
            deno *= j
        termino = num/ deno
        suma += termino
    return suma
def margen_error(real : float, aprox : float) -> float:
    if real == 0:
        return 0 
    numerador = (abs(real - aprox))
    denominador = real
    error : float = numerador/denominador * 100
    if denominador > 0:
        return error
    elif denominador < 0:
       return -error
if __name__ == "__main__":    
    x = float(input("Ingrese un numero para calcular la función:  "))
    porcentaje_error = float(input("Ingrese el porcentaje de error al que desea aproximarse (sin el %):  "))
    real= math.sin(x)
    bandera = True
    while bandera: 
        for i in range (1, 100):
            aprox = seno_aproximada(x, i)
            error = margen_error(real, aprox)
            if error < porcentaje_error:
                print(f"el valor estimado de la funcion sin({x}) = {aprox}")
                print(f"el valor real de la funcion sin({x}) = {real}")
                print (f"al sumar {i} terminos de la serie, el error es del {error}% y es menor al {porcentaje_error}%")
                bandera = False
                break
            else:
                continue