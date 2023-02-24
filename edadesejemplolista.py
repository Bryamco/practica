
lista_edades_a =[33,42,45,1,22,11,133,4]
lista_edades_b =[4,7,1,16,12]

def algun_mayor_edad(
    x:list,
    y:list
)-> list:
    nueva_lista=0
    sumalsita = lista_edades_a + lista_edades_b  
    for i in sumalsita:
        if i >18:
            print(i)
            nueva_lista = nueva_lista + 1
    print(nueva_lista)
algun_mayor_edad(lista_edades_a,lista_edades_b)
