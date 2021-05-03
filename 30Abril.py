#y =input("ingrese una cualidad de sergio: ")
#print ("sergio es",y)
# #EJ#1

#numero = int(input("ingrese un numero "))
#print("la potencia al cuadrado del numero es:",numero**2)
# #EJ2

#num1 = int(input("ingrese el 1er numero"))
#num2= int(input("ingrese el 2do numero"))
#print("la resta de ambos numeros es =:",num1-num2)
#print("la division de ambos numeros es=:",num1/num2)
#print("la multiplicacion de ambos numeros es =:",num1*num2)
#print("el residuo o mmodulo de ambos numeros es=:",num1%num2)
# #EJ3

#import math#se importa la libreria para poder accerder a la funcion modf que separa la parte decimal de la entera de un numero
#num =float(input("ingrese un numero decimal: "))
#parteDecimal,parteEntera = math.modf(num)#siempre se debe poner la parte decimal como primera variable. sino queda mal.
#print("la parte entera del numero es= ",parteEntera,"la parte decimal del numero es= ",parteDecimal)
# #EJ4

#nota1=int(input("1ra nota"))
#nota2=int(input("2da nota"))
#nota3=int(input("3ra nota"))
#nota4=int(input("4ta nota"))
#nota5=int(input("5ta nota"))
#nota1=nota1*0.15
#nota2=nota2*0.20
#3nota3=nota3*0.15
#3nota4=nota4*0.30
#3nota5=nota5*0.20
#print("la nota final es= ",nota1+nota2+nota3+nota4+nota5)
# #EJ5

#sumaProductos=0
#cantidadProductos=0
#precioProducto= int(input("ingrese el precio de su producto"))
#while precioProducto!=0:
#    sumaProductos=sumaProductos+precioProducto
#    cantidadProductos=cantidadProductos+1
#    precioProducto = int(input("ingrese el precio de su producto"))
#    if precioProducto==0:
#        break
#print("el precio sin iva es:",sumaProductos,"COP")
#print("la cantidad de productos fue:",cantidadProductos)
#print("el precio de la compra con iva es:",sumaProductos+sumaProductos*19/100,"COP")
# #EJ6


#numero1= int(input("ingrese el primer nro:"))
#numero2= int(input("ingrese el primer nro:"))
#numero3= int(input("ingrese el primer nro:"))

#print("el promedio de los tres numero es:", (numero3+numero2+numero1)/3)
# EJ#7

#A=1#intercambie el valor de dos variables e imprima los valores antes y después del intercambio. Por ejemplo, si a = 1 y b = 3,
# al intercambiar sus valores serán a = 3 y b = 1
#B=3
#def valoresIniciales(a,b):
#    return " El valor inicial de a=:",a," El valor inicial de b=:",b
#print (valoresIniciales(A,B))

#def cambioValores( a,b):
#    return "el valor posterior al intercambio de a=:",a,"el valor posterior al intercambio de a=:",b
#print(cambioValores(B,A))
# #EJ8

#velocidad= int(input("ingrese la velocidad a la que cae el objeto"))
#print("la velocidad fue de ",velocidad,"km/h")
#altura = int(input("ingrese la altura a la que se solto el objeto"))
#print("la altura a la que se solto el objeto fue de ",altura,"metros")

#tiempoCaida= velocidad/altura
#print("el tiempo de caida fue de ",tiempoCaida,"segundos")
# EJ9

#tiempo=int (input("ingrese el tiempo"))
#aceleracion=int (input("ingrese la aceleracion"))
#velocidad=int (input("ingrese la velocidad inicial"))
#distancia= (velocidad*tiempo)+1/2*aceleracion*tiempo**2
#print(distancia)
# EJ10


#segundos = int(input("ingrese cierta cantidad de segundos " ))
#segundosHoras= segundos*1/60*(1/60)
#print("la cantidad de segundos es =:",segundosHoras,"horas")
# #EJ11

#segundos = int(input("ingrese cierta cantidad de segundos " ))
#segundosMinutos= segundos*1/60
#print("la cantidad de segundos es =:",segundosMinutos,"minutos")
# EJ12

#segundos = int(input("ingrese cierta cantidad de segundos " ))
#segundosHoras= segundos*1/60*(1/60)
#segundosMinutos= segundos*1/60
#horasSegundos=segundos*3600/1
#print(segundosHoras,"horas",segundosMinutos,"minutos",horasSegundos,"segundos")
# EJ13

#nro = int (input("ingrese el nro"))
#if nro %2 == 0 and nro>0:
#    print("es par")
#elif nro%2!=0 and nro>0 :
#    print("es impar")
#elif nro==0:
#    print("el nro es cero, y es par")
#elif nro<0:
#    print(" el numero es negativo")
#else:
#    print("los datos ingresados nos son validos")
#EJ14

#nro = int (input("ingrese el nro"))
#if nro >0:
#    print("positivo")
#elif nro<0:
#    print("negativo")
#EJ15
#nro = int (input("ingrese el nro"))
#if nro %2 == 0 and nro>0:
#    print("es par positivo")
#elif nro %2==0 and nro<0:
#    print("es par negativo")
#elif nro%2!=0 and nro>0 :
#    print("es impar positivo")
#elif nro%2!=0 and nro<0:
#    print("es impar negativo")
#elif nro==0:
#    print("el nro es cero, y es par")
#elif nro<0:
#    print(" el numero es negativo")
#else:
#    print("los datos ingresados nos son validos")
#EJ16

#def invertir(numero):
#    invertido = ""
#    for n in numero:
#        invertido = n + invertido
#    return invertido

#num = str(input("Ingrese un número entero a invertir: "))
#print(invertir(num))
#EJ17
#numero = int(input("Ingrese un número: "))
#if numero >= 10:
#    print("La tercera parte del número es", numero * 3)
#else:
#    print("La cuarta parte del número es", numero * 4)
#EJ18
#n1 = int(input("Ingrese un número entero: "))
#n2 = int(input("Ingrese otro número: "))
#print("El número mayor es", max(n1, n2))
#eEJ19

#numero = int(input("Ingrese un número entero: "))
#print("El número ingresado equivale a", float(numero), "en decimal.")
# EJ20

n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número: "))
n3 = int(input("Ingrese otro número: "))
suma = n1 + n2
if suma > n3:
    print("La suma de los dos primeros números es mayor que el tercer número ingresado.")
else:
    print("La suma de los dos primeros números es menor que el tercer número ingresado.")
# EJ21
user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
if user.startswith("admin") and password.startswith("12345678"):
    print("Inicio de sesión completado")
else:
    print("Inicio de sesión fallido (usuario o contraseña incorrectos).")
# EJ22

print("Los diez primeros números naturales pares son:")
for x in range(0, 11):
    if x % 2 == 0:
        print(x, "", end="")
#EJ23
print("Los diez primeros números naturales impares son:")
for x in range(0, 11):
    if x % 3 == 0:
        print(x, "", end="")
#EJ24

lado = float(input("Ingrese la longitud de un lado del hexágono"))
print("El valor del área del hexágono es:", (6 * (lado**2)) / (4 * (math.tan(math.pi / 6))))
# EJ25
x1 = float(input("Digite la coordenada x1: "))
y1 = float(input("Digite la coordenada x2: "))
x2 = float(input("Digite la coordenada y1: "))
y2 = float(input("Digite la coordenada y2: "))
print("La distancia entre los puntos es de", math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
#EJ26
n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número: "))
n3 = int(input("Ingrese otro número: "))
print("El número mayor es", max(n1, n2, n3), "y el menor es", min(n1, n2, n3))
#EJ27
distancia = int(input("Ingrese la distancia a recorrer (en kilómetros): "))
dias = int(input("Ingrese los días de estancia: "))
pasaje = 5000 * distancia
if distancia > 1000 and dias > 7:
    print(pasaje - (pasaje * 0.15))
else:
    print("El precio del pasaje es", pasaje)
#EJ28
year = int(input("Ingrese un año: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
#EJ29
user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
if user.startswith("admin") and password.startswith("12345678"):
    print("Inicio de sesión completado")
else:
    print("Inicio de sesión fallido (usuario o contraseña incorrectos).")
#EJ3O


















