import math
def arctan_aproximada(x : float, n: int) -> float:
        suma : float = 0
        for i in range (0,n+1):
            termino = (-1)**i * ((x**(2 * i + 1)/(2 * i + 1)))
            suma += termino
        return suma
def margen_error(real : float, aprox : float) -> float:
    if real == 0:
        return 0
    numerador = (abs(real - aprox))
    denominador = real
    error : float = numerador / denominador * 100
    if denominador > 0:
        return error
    elif denominador < 0:
       return -error
     
if __name__ == "__main__":    

    x = float(input("Ingrese un numero para calcular la función:  "))
    while x < -1 or x > 1:
        x= float(input("el valor no está dentro del rango esperado, intente de nuevo:  "))
    porcentaje_error = float(input("Ingrese el porcentaje de error al que desea aproximarse (sin el %):  "))
    real= math.atan(x)
    bandera = True
    while bandera: 
        for i in range (1, 1000):
            aprox = arctan_aproximada(x, i)
            error = margen_error(real, aprox)
            if error < porcentaje_error:
                print(f"el valor estimado de la funcion arctan({x}) = {aprox}")
                print(f"el valor real de la funcion arctan({x}) = {real}")
                print (f"al sumar {i} terminos de la serie, el error es del {error}% y es menor al {porcentaje_error}%")
                bandera = False
                break
            else:
                continue