# outClaspToAdial.py
# Se ejecuta:
# python outDlVToAdial.py
# 
# La entrada es un archivo de texto con ( a lo mas) 500 modelos
# generados con Clasp
# El nombre del archivo es 'Adial.int' y suponemos que ya existe
# tiene un formato extricto x ser salida de otro programa
# No se hace validacion del formato
# Tambien suponemos (x lo pronto) que no es vacio, hay al menos un modelo.
# La salida es un script ya implicito en cada modelo de Adial.int.
# No es otra cosa que una lista de "tokens"
# Ejemplo:
# i21,i8,e7,i7,a3,
# La  lista esta ordenada de acuerdo al primer argumento de la lista de atomos
# del modelo seleccionado
# 


import random

# Funcion residuo o modulo
# Supongo que int trunca, x confirmar
def modulo(extrae,no_models):
 return extrae- ( no_models * (int(extrae/no_models)))


# Convierte lista a cadena y la escribe
# Seguro se puede escribir mejor
# print se puede activar

def extrae_alnum(cadena):
 cad1= ""
 for k6 in range(0, len(cadena)):
  if cadena[k6].isalnum():
    cad1 += cadena[k6]
 return cad1

# Similar a la anterior funcion
def extrae_num(cadena):
 cad1= ""
 for k6 in range(0, len(cadena)):
  if cadena[k6].isdigit():
    cad1 += cadena[k6]
 return cad1




############# FIN de FUNCIONES

# Programa principal

#import sys

extrae= random.randint(1, 500)

file_name1= 'tmp/Adial_cuantitative.int'

# Abre archivos e inicializa 
iden1 =open(file_name1,'r')

file_name2= "tmp/Adial1.int"
iden2 =open(file_name2,"w")

# Leemos archivo y contamos modelos en no_models
apunt=[]
lista_sol = []
for renglon in iden1:
 if ("camino1" in  renglon)== False:
   continue
 else:
##   print(renglon)
   lista_sol = renglon.split( )
iden1.close
##print(lista_sol)
no_solu=len(lista_sol)


if no_solu > 0:
# print(lista_sol)
# Usamos funcion residuo para seleccionar que modelo seleccionaremos
# obtenemos residuo y evitamos el 0
 counter= modulo(extrae,no_solu)
# print(counter)
 Adial1= lista_sol[counter]
 Adial2= (Adial1.replace(")", "")).replace("camino1(","")
 Adial= Adial2.split(",")
 if (Adial[0]=="u10"):
   Adial3 = ["q0"] + Adial[ :2] + ["x3"] + Adial[2: ]
 else:
   Adial3 = ["q3"] + Adial[ :2] + ["q1"] + ["x3"] + Adial[2: ]

else:
   print("WARNING: MAX VERTICES UNDER VALUE\n")
   Adial3=["q10", "x3", "a71", "e21"]

for i in range(0, len(Adial3)):
 iden2.writelines(Adial3[i])
 iden2.writelines(",")

iden2.close
print (Adial3)







