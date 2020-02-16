

MAX_V = 20
# Programa principal

#import sys



file_name1= 'tmp/vertices.out'

# Abre archivos e inicializa 
iden1 = open(file_name1,'r')

# Leemos archivo y contamos modelos en no_models
nV = 0 
for renglon in iden1:
  nV = nV + 1 

if nV > MAX_V:
   print("WARNING: MAX VERTICES OVER VALUE\n")    
else:
   print(nV)

iden1.close








