# AdialToCdial.py
# traductor de dialogos abstractos a concretos (simples)
# python AdialToCdial.py  <dialogo_file> 
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

def extrae_num(cadena):
 cad1= ""
 for k6 in range(0, len(cadena)):
  if cadena[k6].isdigit():
    cad1 += cadena[k6]
 return cad1


def escribe(cadena):
#  cad1=""
#  cad1 = cad1.join(cadena)

  for j17 in range(0, len(cadena)):
   iden1.writelines(cadena[j17])
#   iden1.write("\n")

def skip_atom(iden2):
  for renglon in iden2:
    if "}" in renglon: break


def find_in(l,arreglo,eti):
 for k in range(0,l):
  if arreglo[k] == extrae_alnum(eti):
    return k
 return -1



# elimina control r
# Por lo pronto uso exclusivo en ???
# 
def el_contr_l(cadena):
  if "\r" in  cadena: cade1= el_contr_l(cadena.replace("\r", ""))
  elif "\n" in  cadena: cade1= el_contr_l(cadena.replace("\n", "")) 
  else: cade1=cadena
  return cade1
         
    
# obten entero al inicio de una cadena
def obten_digitos_inicio(cadena):
  global step
  j=0
  n=0
  while(cadena[j].isdigit() ):
    n= n*10 + int(cadena[j])
    j=j+1
  return n 

#Agrega elemento en lista
def agrega(lista, elemento):
 lista += [elemento]
 return lista


# Elimina digitos al inicio de una cadena
def elimina_digitos_inicio(cadena):
  j=0
  while(cadena[j].isdigit() ): j=j+1
  return cadena[j: ]  

# Identifica ???
def arg_est(t_instr):
   if (t_instr == 4 or t_instr ==7 or t_instr ==11 or t_instr==9 or t_instr==10
        or t_instr==12 or t_instr==16):
     return True
   else: return False


# Identifica instruccion con salto
def arg_salto(t_instr):
  if (instr[i1][1] ==3 or instr[i1][1]==5 or instr[i1][1]==6 or instr[i1][1]==8
       or instr[i1][1]==13 or instr[i1][1]==14 or instr[i1][1]==20
       or instr[i1][1]==17 or instr[i1][1]==25):
     return True
  else: return False

 



############# FIN de FUNCIONES

# Programa principal

#import sys

step= 1000

#iden2= open(str(sys.argv[1]),"r")
#file_name=sys.argv[1]


file_name= "agents_knowledge/SLAVES_TASKS/tokens_all.cod"

###iden2= open(file_name,"r")  ANTES 

iden2 = open(file_name,"r",encoding="latin-1") 


file_name1= 'tmp/code.int'

# Abre archivos e inicializa 
iden1 =open(file_name1,'w',encoding="latin-1")


file_name4= "tmp/Adial1.int"
iden4 =open(file_name4,"r",encoding="latin-1")

apunt=[]
for renglon in iden4:
   Adial1=renglon

Adial = Adial1.split(',')
Adial.pop()




instr=[]

sw=0
count_token=0

variables =[None]*10
label=[]
l=0
i=0
last_i=0

# bandera de fin "END" del archivo de entrada.
# 0 no es fin, 1 encontramos END.
end=0

# Guardamos codigo de un token de Adial
output_i=[]

# Se guarda el codigo de todos los tokens de Adial
foutput_i=[None]*len(Adial)

# Se guardan los mensajes. Se escribiran al final, con etiquetas
# lifted de acuerdo al lugar del token
output_t=[]


while True:
 if end==1: break
 label=[]
 l=0

# Lectura de tokens

# Turno cabeza de token
 for renglon7 in iden2:
  renglon=el_contr_l(renglon7)
#  Si cambio de <2 a < 3   RARO
  if "#" in renglon7:continue
  if len(renglon7) < 2: continue
  if "END" in renglon:
   end=1
   break
#  print(renglon)
  if sw==0:
     token=renglon
#     print("token= ",token)
#     raw_input()
     KK=find_in(len(Adial),Adial,token)
     if KK== -1:
         skip_atom(iden2)
         continue
     else: 
#          print("token ENCONTRADO= ",token)
          sw=1
          continue
  if sw==1:
     if "{" in renglon:
#       print("encontre { paso a sw=2")
       sw=2
       break
     else: 
      print("error, esperaba { \n")
      break

# Turno de instrucciones del token
 if end==1: break
 for renglon7 in iden2:
  renglon=el_contr_l(renglon7) 
#  print(renglon)   
  datos=renglon.split()
#  print(len(datos),"@",renglon)
# instruccion con etiqueta
  if len(datos)>3:
   if "+" in datos[2]:
    n_instr = 0
    t_instr = int(datos[0])
    if arg_est(t_instr):
       ap_instr= str(int(datos[1]))   
    else:
       ap_instr= str(int(datos[1]) + (step * KK))
   else:
    n_instr = int(datos[0]) + (step * KK)
    t_instr = int(datos[1])
    if arg_est(t_instr):
       ap_instr= str(int(datos[2]))   
    else:
       ap_instr= str(int(datos[2]) + (step * KK)) 
  elif len(datos)==2:
# instruccion sin etiqueta
    n_instr = 0
    t_instr = int(datos[0])
    if arg_est(t_instr):
       ap_instr= str(int(datos[1]))   
    else:
       ap_instr= str(int(datos[1]) + (step * KK))

# hay 2 casos
  elif "+" in datos[2]:
   n_instr = 0
   t_instr = int(datos[0])
   if arg_est(t_instr):
       ap_instr= str(int(datos[1]))   
   else:
       ap_instr= str(int(datos[1]) + (step * KK))
  else:
    n_instr = int(datos[0]) + (step * KK)
    t_instr = int(datos[1])
    if arg_est(t_instr):
       ap_instr= str(int(datos[2]))   
    else:
       ap_instr= str(int(datos[2]) + (step * KK))

# termimos los casos
  if (n_instr >0):
    label += [[n_instr,i]]
    l=l+1
# guardamos la instruccion
#  print([n_instr, t_instr,ap_instr])
#  raw_input("chck point 0")
  instr += [[n_instr, t_instr,ap_instr]]
  i=i+1
  if (t_instr==0): break

# fin del ciclo que  proceso un token (codigo)
# tenemos que actualizar etiquetas del token.
 i1=last_i
 instr[i1][0]= step * KK  
 while (instr[i1][1] !=0 and instr[i1][1] !="#"):
#  print("antes", instr[i1])  
  if arg_salto(instr[i1][1]):
     l2= instr[i1][2]  
     l1 = ( step * KK ) + int(l2)
     instr[i1][2]= str(l2)
#  print("despues", instr[i1])
  i1=i1+1

# Genera salida de la instruccion en output_i
 output_i=[]
 if end==1: break
 i1=last_i
 while (instr[i1][1] !=0 and instr[i1][1] !="#"): 
  output_i += [[str(instr[i1][0]) + " ", str(instr[i1][1]) + " ", instr[i1][2], "\n"]]
  i1=i1+1

#  output_i += ["\n"]
# checK_point= raw_input("check point 1")
 last_i=i

# ya a la lista final asociada al token correspondiente indizado por KK
 foutput_i[KK] = output_i
 
#####

# Turno del texto mensajes del token

# Esto esta muy muy chafa x mejorar
# Lee mensajes del archivo y dejalos en dict
 if end==1: break
 dict=[]
 for renglon in iden2:
  if "#" in renglon[0]: continue
  if "}" in renglon[0]:
    sw=0
    break
  if renglon[0].isdigit():
# entrada de la etiqueta del mensaje, incluye # y primera oracion mensaje
      dict+=[ [obten_digitos_inicio(renglon),[elimina_digitos_inicio(renglon)]  ]  ]
# Agrega resto del texto del mensaje
  else:
      X=dict.pop()
      X2=X.pop()
      X1=X.pop()
      dict+=[ [X1, agrega(X2, renglon ) ]  ]

 if end==1: break

# guardamos # etiqueta lifted segun token junto con su texto
 for k3 in range(0, len(dict)):
  output_t += [[str(  dict[k3][0] + (step * KK)) + " "] + dict[k3][1]]
# count_token = count_token +1


# Da formato a la segunda entrada de cada elemento de dict
 if end==1: break
 for k in range(0, len(dict)):
  X=dict[k]
  X2=X.pop()
  X1=X.pop()
#  dict[k]= [X1, formato(X2)]

# guardamos diccionario sin dar formato.
  dict[k]= [X1, X2]

#print("fin de tokens")
#raw_input()
# Finalmente escribimos a archivo
gg= step * len(Adial)
for k in range(0, len(Adial)):
 escribe([ [ "#"], Adial[k], ["\n"]])

### ???? PROBLEMAS 
# Si archivo TOKENS tiene lineas vacias (entre } y token TRUENA
# print("k= ",k)
 escribe(foutput_i[k] )
# print("? ",foutput_i[k] )
escribe([ [str(gg)," 9 ","0","\n"], [ "0 ","0 ","0","\n"],["#","\n"]  ])
 

for k in range(0, len(output_t)):
 escribe(output_t[k]) 

#### fin

iden1.close()
iden2.close


#print;
#print("*** fin de sesion ***")
#print;






