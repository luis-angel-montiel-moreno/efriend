# extrae_respuestas.py
# Se ejecuta:
# python extrae_respuestas.py
# 
# 

 
def find(c,cadena):
  j=0
  while(cadena[j] != c):
    j=j+1
  return j

# obten entero al inicio de una cadena
def obten_digitos_inicio(cadena):
  j=0
  n=0
  while(cadena[j].isdigit() ):
    n= n*10 + int(cadena[j])
    j=j+1
  return n 

# Programa principal

#import sys

pp=[]
file_name2= "agents_knowledge/MAIC_KR/universal/questions_made.clasp"
iden2 =open(file_name2,"r",encoding="latin-1" )
for renglon in iden2:
 if "contador(" in renglon:
#   print("contador")
   n = obten_digitos_inicio(renglon[9: ])

 else: pp += [renglon]

iden2.close

iden2 =open(file_name2,"w",encoding="latin-1" )

for k in range(0, len(pp)):
 iden2.write(pp[k])

file_name1= 'tmp/respuestas.cnv'

# Abre archivos e inicializa 
iden1 =open(file_name1,'r',encoding="latin-1" )


# Leemos archivo 
# Recoradmos
# Predicados e_  estaticos
# predicados h_ dinamicos

for renglon in iden1:

 if "#" in  renglon:
### PARCHE checar bien
    if renglon[0] == "#": iii=1
    else: iii=2

#    print("caso # = ", renglon[iii:len(renglon) -1])
    r= renglon[iii : len(renglon) -1]
    if ("a7" or "a71" or "e26") in r: 
        continue
    else:
        iden2.write("p(" + r + ").\n" )
        continue
 elif "Animo" in renglon: 
        a= obten_digitos_inicio(renglon[15: ])
        iden2.write("h_animo_i(" + str(n) + "," + str(a) + ").\n" )
 elif "Perc." in renglon: 
       e= obten_digitos_inicio(renglon[15: ])
       iden2.write("h_perc_esc(" + str(n) + "," + str(e) + ").\n" )
 elif "FechaHora =" in renglon:
       iden2.write("%" + renglon + "\n" )
 elif ("(" in renglon and ")." in renglon):
   if ("h_" in renglon):
      k1=find("(",renglon)
      k2=find(")",renglon)
#      print(renglon[0:k1] + "("+ "c_"+str(n)+","+ renglon[k1+1:k2] + ").")
      iden2.write(renglon[0:k1] + "("+ str(n)+","+ "c_"+ renglon[k1+1:k2] + ").\n")
   elif ("e_" in renglon):
      k1=find("(",renglon)
      k2=find(")",renglon)
#      print(renglon[0:k1] + "("+ "c_"+str(n)+","+ renglon[k1+1:k2] + ").")
      iden2.write(renglon[0:k1] + "("+ "c_"+ renglon[k1+1:k2] + ").\n")
   else:
       iden2.write(renglon)

iden2.write("contador(" + str(n+1) + ").\n" )
# Cerramos archivo


#### fin

iden1.close()
iden2.close

#print;
#print("*** fin de sesion ***")
#print;






