#EJERCICIO 1 (IF,ELIF,ELSE)
# # x = 'Usuario1'
# # y = 'usuario2'

# x = str(input('ingresa tu usuario '))
# y = str(input('ingresa tu usuario '))

# if x == 'Usuario1':
#     print('El usuario es correcto')
# elif y == 'Usuario2':
#     print('El usuario 2 es correcto')   
# else:
#     print('Usuario Incorrecto')
#_________________________________________________________________________

# # print('Hola Buenas noches')
# # hora = str(input('Por favor ingrese que hora es: '))
# # print(hora)

#______________________________________________________________________
#EJERCICIO 2 F'STRING

#Realizar un programa que pregunte yel area de un triangulo 

# base = float(input('Ingrese la base del triangulo: '))
# altura = float(input('Ingrese la altura del triangulo: '))
# resultado = base*altura//2

# print(f'El resultado es: {resultado}')

#______________________________________________________________________

#EJERCICIO 3
#mayor o menor de edad

# edad = int(input('Ingresa tu edad: '))

# if edad >= 18:
#     print('Usted es mayor de edad')
# else:
#     print('Tu no eres mayor de edad')    
#______________________________________________________________________

# EJERCICIO 4 .UPPER  - .LOWER 
#Preguntar al usuario que ingrese una palabra que se imprima en mayuscula

# palabra = str(input('Ingrese una palabra en MAYUSCULAS: '))
# print(palabra.lower())

# palabra = str(input('Ingrese una palabra en minusculas: '))
# print(palabra.upper())

#______________________________________________________________________

# Crear un pgrama de caracteres que almacene una contrasenas, str
#EJERCICIO #4 
# contrasena = str(input('Ingrese su contrasena '))

# if contrasena.upper() == 'BRYAN1996':
#     print('Su contrasena es correcta')
# else:
#     print('Su contrasena no es correcta')
#______________________________________________________________________
# EJERCICIO #5 TRANSFORMAR TEXTO

# texto = str(input('Ingresa tu rutina en miniscula para tranformarlo a mayuscula: '.upper()))
# print(texto.upper())

#______________________________________________________________________
#EJERCICIO #6 CON OPOERADORES LOGICOS AND 

# En una escuela se realiza un sondeo de edades a los cuales se le asignara una categoria a los estudiantes, dependiendo su edad ingresaran a un grupo
# los grupos son a,b,c, los grupos deben mostrarse en mayusculas al final del resultado. 

# edad = int(input('Ingresa tu edad: '))

# if edad >= 1 and edad <=9 : 
#     print('Usted es asignado al grupo a'.upper())
# elif edad >=10 and edad <=15:
#     print('Usted es asignado al grupo b'.upper())
# elif edad >=16 and edad <=19:
#     print('Usted es asignado al grupo c'.upper())
# else:
#     print('Usted no se encuentra en ninguna categoria'.upper())
#______________________________________________________________________    
#EJERCICIO #7 CON OPOERADORES LOGICOS OR 

# color = str(input('Ingresa un color: '))

# if color == 'rojo' or color == 'azul':
#     print('El color es correcto')
# else:
#     print('No es correcto el valor')
#______________________________________________________________________    

#EJERCICIO #8 CON OPOERADORES LOGICOS NOT

# articulo = [1,2,3,4,5,6,7,8,9]
# while True:
#     try:
#         numero = int(input('Ingrese un numero del 1 al 9: '))
#     except ValueError:
#         print('ingresa solo numeros')
#         break
#     if numero not in articulo:
#         print('No se encuenta en la lista')
#     else:
#         print('El numero se encuentra en la lista')



numero = int(input('Ingrese un numero: '))

while numero <= 99:
    numero+=1 
    print(numero)

    if numero ==85: 
       print('Numero es menor a 99') 
       break

    
    

    


    
    

    


