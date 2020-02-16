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


file_name1= 'tmp/Cine.int'

# Abre archivos e inicializa 
iden1 =open(file_name1,'r',encoding="latin-1")


file_name2= "agents_knowledge/MAIC_KR/universal/preguntasCine.clasp"
iden2 =open(file_name2,"w",encoding="latin-1")


# Leemos archivo para seleccionar el modelo
# el modelo queda en la lista Adial1
# Esta lista contiene los atomos en posicion par e ubicacion en el sript
# En la posicion non contiene el token
hay=0
for renglon in iden1:
  if "e" !=  renglon[0]: continue
  hay=1
  Adial1 = renglon.split(')')[0]+")."

  break
if hay==1:
  iden2.writelines("%%% Pregunta a realizar\n")
  iden2.writelines(Adial1)
else: iden2.writelines("%%% NO hay pregunta a realizar\n")
iden1.close()





iden2.close

#print;
#print("*** fin de sesion ***")
#print;






