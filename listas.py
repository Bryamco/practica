lista_estudiantes = ['Bryan','Omar','Isaac']
lista_profesores = ['Felipe']

def agregar(
    lista: list
) -> list :
    estudiante = input('Ingrese estudiante ')
    lista.append(estudiante)
    print(lista)
    
# agregar(lista_estudiantes)

def suprimir(
    lista: list
) -> list :
    estudiante = input('suprima un estudiante ')
    lista.remove(estudiante)
    print(lista_estudiantes)
    
# suprimir(lista_estudiantes) 

def agregarnuevo(
    agregar=list,
    suprimir=list,
    c='Esto es bien cabron de aprender para mi'
):
   #print(agregar+suprimir)
   agregarnueva = agregar+suprimir
   agregarnueva.append(c)
   print(agregarnueva)
   
    
agregarnuevo(lista_estudiantes,lista_profesores)
          
        