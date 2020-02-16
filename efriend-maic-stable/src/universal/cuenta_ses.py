# cuenta_ses.py
 
# obten entero al inicio de una cadena
def obten_digitos_inicio(cadena):
  j=0
  n=""
  while(cadena[j].isdigit() ):
    n= n + cadena[j]
    j=j+1
  return n 
# Programa principal

#import sys

file_name2= "agents_knowledge/MAIC_KR/universal/questions_made.clasp"
iden2 =open(file_name2,"r")
for renglon in iden2:

 if "h_animo_i(" in renglon:
   n = obten_digitos_inicio(renglon[10: ])
 if "p(q10)" in renglon:
   break

print("HAY " +str(int(n)+1)+" SESIONES\n")

iden2.close()







