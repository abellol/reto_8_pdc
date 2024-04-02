# Reto 8: Bucles 2 (For)
### Soy Alejandro Bello y pertenezco al grupo de "Fenomenoides", adjunto nuestro logo: 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

### 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
if __name__  == "__main__":
  for num in range (1, 101, 1): # Genera la secuencia [1, 2, ..., 99, 100]
      x = num ** 2  # eleva cada numero de la secuencia al cuadrado
      print (f"{num}^2 = {x}") # imprime "num ^ 2 = x"
```
### 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python
def impar (n : int): # se define la funcion que imprime los valores impares de 1 hasta n
    print ("Impares")   
    for i in range(1, n+1):
        if i % 2 == 0: # evalua si es par
            continue # si es par, solo pasa al siguiente numero
        else: 
            print (i) #imprime los impares dentro de la secuencia [1, 2, ..., n-1, n]

def par (n : int): # se define la funcion que imprime los valores pares de 1 hasta n
    print ("Pares")       
    for i in range (1, n+1):
        if i % 2 != 0: # evalua si es impar
            continue # si es impar, solo pasa al siguiente numero
        else: 
            print (i) #imprime los pares dentro de la secuencia [1, 2, ..., n-1, n]
             
if __name__ == "__main__":
    n : int = 1000 # se declara e inicializa la variable n = 1000
    x = impar(n) # Mostrará los impares de 1 a 1000
    y = par(n) # Mostrará los pares de 1 a 1000
    print (x, y) # se imprimen ambas funciones
```
### 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
if __name__ == "__main__":
    n = int(input("Ingrese un numero mayor o igual que 2:  ")) # se ingresa un numero mayor que 2 
    while n <= 2:
        n = int(input("el numero ingresado es menor, ingrese un numero mayor o igual que 2:  ")) # Un bucle que verifica que el numero n siempre sea mayor que 2
    if n%2==0: # En caso de ser par, 
        for nums in range (n, 1, -2): # se descompone en pares restando 2
            print (nums) #se muestra cada valor que se obtiene
    else: # en caso de ser impar, 
        for nums in range (n-1, 1, -2): # Se le resta uno al número y empiza a descomponer restando 2
            print(nums) # Imprime cada valor que se obtiene
```
### 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

```python
x: int = 1 # Se establece una variable que cambia con cada paso, en este caso 1 ya que es coel módulo de la multiplicación
if __name__ == "__main__":
    n = int(input("ingrese un numero para hallar su factorial:  ")) #Se ingresa el numero n deseado para hallar sus factoriales desde 1
    for num in range (1, n+1, 1): # para cada numero de 1 hasta n,
        x=x*num # se halla cada factorial y se guarda para calcular el siguiente valor.
        print(f"{num}! = {x}") # imprime cada factorial de la forma "num! = x "
```
### 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```python
resultado : int = 1 # Se establece una variable que cambia con cada paso, en este caso 1 ya que es el módulo de la multiplicación
if __name__ == "__main__":
    exp = int(input("Ingrese un exponente para la base 2:  ")) # se ingresa el exponente (entero)
    if exp > 0: # si el exponente es mayor que 0,
        for i in range (1, exp+1, 1): # para cada numero de 1 hasta exponente
            resultado *=2 # actualiza la variable resultado al multiplicar el resultado inicial (1) por  2, i veces
        print(f"2 ^ {i} = {resultado}") # imprimir el resultado de la forma : "2 ^ i = resultado"
    elif exp < 0: # si el exponente es menor que 0,
        for i in range (1, (-exp+1), 1): # para cada numero de 1 hasta exponente
            resultado *= 2 # actualiza la variable resultado al multiplicar el resultado inicial (1) por  2, i veces
            pot_neg = 1 / resultado # al ser potencia negativa, es multiplicar hace el inverso que queda como 1/2^i y queda en la variable pot_neg
        print(f"2 ^ {-i} = {pot_neg}") # imprimir el resultado de la forma : "2 ^ -i = pot neg"
    else: # si el exponente es igual a 0, retorna:
        print ( "2 ^ 0 = 1")
```
### 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

```python
resultado : int = 1 # Se establece una variable que cambia con cada paso, en este caso 1 ya que es el módulo de la multiplicación
if __name__ == "__main__":
    x = float (input("ingrese la base de la expresion:  ")) # se ingresa la base de la expresión (real)
    n = int(input("ingrese el exponente de la expresion:  ")) # Se ingresa el exponente de la expresión (entero)
    if n < 0: # si el exponente es menor que 0,
        for i in range (1, -n+1, 1): # para cada numero de 1 hasta exponente
            resultado *= x  # actualiza la variable resultado al multiplicar el resultado inicial (1) por  2, i veces
            pot_neg = 1 / resultado # al ser potencia negativa, es multiplicar hace el inverso que queda como 1/2^i y queda en la variable pot_neg
        print(f"{x} ^ {-i} = {pot_neg}") # imprimir el resultado de la forma : "2 ^ -i = pot neg"
    elif n > 0: # si el exponente es mayor que 0,
        for i in range (1, n+1, 1): # para cada numero de 1 hasta exponente
            resultado *= x # actualiza la variable resultado al multiplicar el resultado inicial (1) por  x, i veces
        print(f"{x} ^ {i} = {resultado}") # imprimir el resultado de la forma : "2 ^ i = resultado"
    else: # si el exponente es igual a 0, retorna:
        print(f"{x} ^ 0 = 1")
```
### 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

```python
if __name__ == "__main__":
    for i in range (1, 10, 1): #para cada elemento i de la secuencia de  1 a 9
        print (f"Tabla del {i}") # imprimir "tabla del "i""
        for j in range (1, 11, 1): # para cada elemento j dentro de la secuencia 1 a 10
            num = i  * j # la variable num = i * j y se actualiza en cada paso
            print(f"{i} * {j} = {num}")  # retorna "i * j = num"
```
### 8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

```python
import math # se importa la libreria math 
def exponencial_aproximada(x : int, n : int) -> float: # se define la función exponencial 
    suma : float = 0 # se establece la variable que guardará la suma de los términos, inicia en 0 porque es el módulo de la suma
    for i in range (0,n+1): # para cada numero en la secuencia de 0 a n,
        nume = (x**i) # se establece la variable numerador que es igual a x ** i
        deno = 1 # la variable denominador empieza en 1, que es el módulo de la multiplicación
        for num in range (1, i+1): # para cada numero dentro de la secuencia de 1 a i,
            deno *= num # el denominador es igual a denominador por cada numero de la secuencia 
        termino = nume/deno # el termino es igual al cociente entre numerador y denominador 
        suma += termino # la suma es igual al termino, y se va sumando con cada paso
    return suma # retorna el valor final de la suma 
def margen_error(real : float, aprox : float) -> float: # defina la función del margen de error
    error : float = (abs(real - aprox)/real) *100 # el error es igual a :
    return error # retorna el valor del error 

if __name__ == "__main__":
    x = int(input("Ingrese un numero para que sea el exponente de la función:  ")) # Se ingresa el valor de la función y se almacena en la variable x
    porcentaje_error = float(input("Ingrese el porcentaje de error al que desea aproximarse (sin el %):  ")) # Se ingresa el porcentaje de error que se desea calcular en la variable porcentaje_error
    real= math.exp(x) # se calcula el valor real de la función 
    bandera: float = True # Se define la variable bandera, inicializada en True
    while bandera: 
        for i in range (1, 101): # para cada valor de la secuencia de 1 a 100
            aprox = exponencial_aproximada(x, i) # se usa la función exponencial_aproximada, como argumento la variable x e i
            error = margen_error(real, aprox) # calcula el margen de error entre la funcion real y la aproximada
            if error < porcentaje_error: # si el error calculado es menor al esperado, 
                print(f"el valor estimado de la funcion e ^ {x} = {aprox}")  # imprime el valor estimado de la función
                print(f"el valor real de la funcion e ^ {x} = {real}")  # Imprime el valor real de la función
                print (f"al sumar {i} terminos de la serie, el error es del {error}% y es menor al {porcentaje_error}%") # imprime el numero de sumas de la serie que debe ejecutar para ser menor al porcentaje ingresado
                bandera = False #establece la bandera como false
                break #  rompe el ciclo
            else: 
                continue
```
### 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

```python
import math # se importa la libreria math
def seno_aproximada(x : float, n : int) -> float: # se define la función seno
    suma : float = 0 # se establece la variable que guardará la suma de los términos, inicia en 0 porque es el módulo de la suma
    for i in range (0,n+1): # para cada numero en la secuencia de 0 a n,
        arg = 2 * i + 1 # se define la variable arg, que es un termino de todo el polinomio que se debe resolver
        num = (-1)**i *(x**(arg)) # Se define la variable del numerador 
        deno = 1  # la variable denominador empieza en 1, que es el módulo de la multiplicación
        for j in range (1, arg + 1):  # para cada numero dentro de la secuencia de 1 a arg + 1,
            deno *= j #  el denominador es igual a denominador por cada numero de la secuencia 
        termino = num/ deno # el termino es igual al cociente entre numerador y denominador 
        suma += termino # la suma es igual al termino, y se va sumando con cada paso
    return suma   # retorna el valor final de la suma 
def margen_error(real : float, aprox : float) -> float:  # defina la función del margen de error
    if real == 0: # si real es igual a 0
        return 0 # retorna 0
    numerador = (abs(real - aprox)) # define la variable numerador, siendo la difernecia entre real y aproximado
    denominador = real # define la variable denominador con el valor de la función real
    error : float = numerador/denominador * 100 # la variable error es el valor del cociente entre las dos variables anteriores, multiplicado por 100
    if denominador > 0: # Si el denominador es mayor que 0,
        return error # retorna el valor original del error
    elif denominador < 0: # si el denominador es menor que 0,
       return -error # retorna el error multiplicado por -1 (cambio de signo)
if __name__ == "__main__":    
    x = float(input("Ingrese un numero para calcular la función:  ")) #  Se ingresa el valor de la función y se almacena en la variable x
    porcentaje_error = float(input("Ingrese el porcentaje de error al que desea aproximarse (sin el %):  ")) # Se ingresa el porcentaje de error que se desea calcular en la variable porcentaje_error
    real= math.sin(x) # se calcula el valor real de la función 
    bandera = True  # Se define la variable bandera, inicializada en True
    while bandera: 
        for i in range (1, 101): # para cada valor de la secuencia de 1 a 100
            aprox = seno_aproximada(x, i)  # se usa la función exponencial_aproximada, como argumento la variable x e i
            error = margen_error(real, aprox) # calcula el margen de error entre la funcion real y la aproximada
            if error < porcentaje_error: # si el error calculado es menor al esperado, 
                print(f"el valor estimado de la funcion sin({x}) = {aprox}") # imprime el valor estimado de la función
                print(f"el valor real de la funcion sin({x}) = {real}")  # Imprime el valor real de la función
                print (f"al sumar {i} terminos de la serie, el error es del {error}% y es menor al {porcentaje_error}%") # imprime el numero de sumas de la serie que debe ejecutar para ser menor al porcentaje ingresado
                bandera = False #establece la bandera como false
                break  # rompe el ciclo
            else:
                continue
```
### 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

```python
import math # se importa la libreria math
def arctan_aproximada(x : float, n: int) -> float: # se define la función arctan
        suma : float = 0 # se establece la variable que guardará la suma de los términos, inicia en 0 porque es el módulo de la suma
        for i in range (0,n+1):  # para cada numero en la secuencia de 0 a n,
            termino = (-1)**i * ((x**(2 * i + 1)/(2 * i + 1)))  #el termino es igual a :
            suma += termino # el valor del termino se va sumando en la variable suma
        return suma # retorna el valor final de suma
def margen_error(real : float, aprox : float) -> float:   # defina la función del margen de error
    if real == 0: # si real es igual a 0, 
        return 0 # retorna 0
    numerador = (abs(real - aprox))  # el numerador es igual al valor absoluto de la dferencia entre el valor real y aproximado de la función
    denominador = real # variable denominador toma el valor de la variable del valor de la funcion real 
    error : float = numerador / denominador * 100 # la variable error es igual al cociente entre numerador y denominador
    if denominador > 0: # si el denominador es mayor que 0,
        return error # retorna el valor de error 
    elif denominador < 0: # Si el denominador es menor que 0, 
       return -error # retorna el error multiplicado por -1 (cambio de signo)
  
if __name__ == "__main__":    
    x = float(input("Ingrese un numero para calcular la función:  ")) #  Se ingresa el valor de la función y se almacena en la variable x
    while x < -1 or x > 1: # un bucle verifica que el valor esté dentro del rango
        x= float(input("el valor no está dentro del rango esperado, intente de nuevo:  "))
    porcentaje_error = float(input("Ingrese el porcentaje de error al que desea aproximarse (sin el %):  ")) # Se ingresa el porcentaje de error que se desea calcular en la variable porcentaje_error
    real= math.atan(x)  # se calcula el valor real de la función
    bandera = True   # Se define la variable bandera, inicializada en True
    while bandera: 
        for i in range (1, 10001):  # para cada valor de la secuencia de 1 a 10000
            aprox = arctan_aproximada(x, i) # se usa la función exponencial_aproximada, como argumento las variables x e i
            error = margen_error(real, aprox) #  calcula el margen de error entre la funcion real y la aproximada
            if error < porcentaje_error:  # si el error calculado es menor al esperado,
                print(f"el valor estimado de la funcion arctan({x}) = {aprox}") # imprime el valor estimado de la función
                print(f"el valor real de la funcion arctan({x}) = {real}") # Imprime el valor real de la función
                print (f"al sumar {i} terminos de la serie, el error es del {error}% y es menor al {porcentaje_error}%") # imprime el numero de sumas de la serie que debe ejecutar para ser menor al porcentaje ingresado
                bandera = False   #establece la bandera como false
                break # rompe el ciclo
            else:
                continue
```
