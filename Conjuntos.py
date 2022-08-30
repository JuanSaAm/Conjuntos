#Conjuntos
#Definicion del conjunto universal.
U = {1,2,3,4,5,6,7,8,9,10} #En este caso el universo son los numeros del 1 al 10.
print("El universo es: ", U)

#Definicion del conjunto vacio.
V = set() #Se escribe esta linea para que no se confunda con una biblioteca.
V = {}
print("conjunto vacio: ", V)

#Definicion del conjunto por extencion.
a = {1,2,3,4,5} #Todos los elementos estan en orden.
print("Conjunto a = ", a)

#Definicion del conjunto por comprencion.
b = {2,4,6,8,10} #Todos los elementos son pares.
print("Conjunto b = ", b)

#Union de conjuntos
print("La union de a y b es", a|b)

#Interseccion de conjuntos
print("La interseccion de a y b es", a&b)

#Diferencia de conjuntos
print("La diferencia de a y b es", a-b)
print("La diferencia de b y a es", b-a)

#Diferencia simetrica de conjuntos
print("La diferencia simetrica de a y b es", a^b)

#Complemento de conjunto
print("Complemento de a es: ", U-a)

#Subconjunto
print("b es un subconjunto de U: ", b.issubset(U)) 
print("b es un subconjunto de a: ", b.issubset(a)) 

#Superconjunto
print("U es el superconjunto de b: ", U.issuperset(b))
print("a es el superconjunto de b: ", a.issuperset(b))