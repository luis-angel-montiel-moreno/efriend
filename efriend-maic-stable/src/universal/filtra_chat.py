# extrae_respuestas.py
# Se ejecuta:
# python extrae_respuestas.py
# 
# 

# elimina control r
# Por lo pronto uso exclusivo en ???
# 
def el_contr_l(cadena):
  if "\r" in  cadena: cade1= el_contr_l(cadena.replace("\r", ""))
  else: cade1=cadena
  return cade1

# Programa principal

#import sys


file_name1= 'tmp/code.cnv'

# Abre archivos e inicializa 
iden1 =open(file_name1,'r',encoding="latin-1" )

file_name2= "tmp/respuestas.cnv"
iden2 =open(file_name2,"w",encoding="latin-1")

# Leemos archivo 
# Recoradmos
# Predicados e_  estaticos
# predicados h_ dinamicos


for renglon1 in iden1:
 renglon= el_contr_l(renglon1)
 if (">" ==  renglon[0] and len(renglon) > 4): 
    iden2.write(renglon)
    continue
 if "?" in  renglon:
    iden2.write(renglon)
    continue
 if "trata de" in  renglon:
    iden2.write(renglon)
    continue
 if "que intentes" in  renglon:
    iden2.write(renglon)
    continue
 if "nimo inicial =" in  renglon:
    iden2.write(renglon)
    continue
 if "FechaHora =" in  renglon:
    iden2.write(renglon)
    continue
 if "escuela =" in  renglon:
    iden2.write(renglon)
    continue
 if "nombre" in  renglon:
    iden2.write(renglon)
    continue
 if "Noto un" in  renglon:
    iden2.write(renglon)
    continue
 if ":)" in  renglon:
    iden2.write(renglon)
    continue
 if "#" in  renglon:
    iden2.write(renglon)
    continue

# casos error (salta)
 if ("(," in renglon or ",," in  renglon or ",)" in  renglon):
    continue

# Casos para ASSERT
 if ("e_" in renglon and "(" in  renglon and ")." in  renglon):
    iden2.write(renglon)
    continue

 if ("h_" in renglon and "(" in  renglon and ")." in  renglon):
    iden2.write(renglon)

 continue
# Cerramos archivo


#### fin

iden1.close()
iden2.close

#print;
#print("*** fin de sesion ***")
#print;






