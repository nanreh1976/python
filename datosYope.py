from math import sqrt #importar libreria de matetica tipo raiz cuadrado

#Tipos de Datos

cadenasString = "milepeletqay@gmail.com" # str string
num1 = 7 #int Entero
num2 = -7 #int Entero
num3= 12.5 #float Flotante(numero decimales)
bool1 = True #bool dato Logico Verdadero
bool2 =False #bool dato Logico Falso


# Operadores

# + suma 
# - resta 
# * multiplicador 
# **potencia 
# / division 
# // division entera 
# % resto de la division (no porcentaje)

numero1 =11
numero2 = 5
suma = numero1 + numero2

print("el resultado de la suma: ", suma )

resta = numero1 - numero2

print("el resultado de la resta: ", resta )

multi = numero1 * numero2

print("el resultado de la multiplicacion: ", multi )

potencia = numero1 ** numero2

print("el resultado de la potencia: ", potencia )

divisionSim = numero1 / numero2

print("el resultado de la division simple: ", divisionSim )


divisionEnt = numero1 // numero2

print("el resultado de la division entera: ", divisionEnt )

divisionRest = numero1 % numero2

print("el resultado de la resto division: ", divisionRest )

raiz = sqrt(numero1+numero2)

print(" la raiz cuadrada de la suma de las variables es ", raiz )

#operadores de asignacion

edad=18 #asignacion

edad = edad + 5 #reasignacion

edad += 20 #edad = edad + 20 seria 
edad -= 2
edad *= 3

print("mi edad dentro de 5 años va a ser ", edad)

#operadores relacionales

num1 = 6
num2 = 12
num3 = 6

# menor que <
# mayor que >
# igual que ==
# != distinto que
# <= menor o igual que
# >= mayor o igual que

print(f"lo que hay en numero1 es menor que lo que hay en numero2 , ( {num1} , {num2} ) ", num1< num2)
print(f"lo que hay en numero1 es mayor que lo que hay en numero2 , ( {num1} , {num2} ) ", num1> num2)
print(f"lo que hay en numero1 es igual que lo que hay en numero2 , ( {num1} , {num2} ) ", num1== num2)
print(f"lo que hay en numero1 es igual que lo que hay en numero3 , ( {num1} , {num3} ) ", num1== num3)
print(f"lo que hay en numero1 es distinto que lo que hay en numero3 , ( {num1} , {num3} ) ", num1!= num3)
print(f"lo que hay en numero1 es distinto que lo que hay en numero2 , ( {num1} , {num2} ) ", num1!= num2)
print(f"lo que hay en numero1 es mayor o igual que lo que hay en numero2 , ( {num1} , {num2} ) ", num1>= num2)
print(f"lo que hay en numero1 es menor o igual que lo que hay en numero3 , ( {num1} , {num3} ) ", num1<= num3)
print(f"lo que hay en numero1 es menor o igual que lo que hay en numero2 , ( {num1} , {num2} ) ", num1<= num2)
print(f"lo que hay en numero1 es menor o igual que lo que hay en numero3 , ( {num1} , {num3} ) ", num1<= num3)