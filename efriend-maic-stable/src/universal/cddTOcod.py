# cdeTOcod.py
# traductor de ....
# python cddTOcod.py  <dialogo_file> 
#


# Convierte lista a cadena y la escribe
# Seguro se puede escribir mejor
# print se puede activar

def extrae1_alnum(cadena):
 cad1= ""
 for k6 in range(0, len(cadena)):
  if cadena[k6].isalnum():
    cad1 += cadena[k6]
  else:break
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
  cd= arreglo[k][0]
#  print("len ",len(eti),len(cd))
#  print("eti, arreglo[k] = ", eti, cd)
  if cd == eti:
#    print("encontro= ",arreglo[k][1])
#    input() 
    return arreglo[k][1]
# input()
 return -1

        
    
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

# Identifica ??? (AHORA YA NO incluye # 17???)
def arg_est(t_instr):
   if ( t_instr == 2 or t_instr == 4 or t_instr ==7 or t_instr ==11 or t_instr==9 or t_instr==10 
        or t_instr==12 or t_instr==16):
     return True
   else: return False


# Identifica instruccion con salto (INCLUYE # 17 a diferncia de ...
def arg_salto(t_instr):
  if (instr[i1][1] ==3 or instr[i1][1]==5 or instr[i1][1]==6 or instr[i1][1]==8
       or instr[i1][1]==13 or instr[i1][1]==14 
       or instr[i1][1]==20 or instr[i1][1]==17 or instr[i1][1]==25):
     return True
  else: return False

def filtra_exit(lista, eti):
 out=[]
 for k in range(0,len(lista)):
   entry=lista[k]
#   print("entry_in= ", entry)
   if entry[1]=="19 ":
     entry_out =  [entry[0],"6 ",eti, entry[3]]
   else:
     entry_out = entry
#   print("entry_out = ", entry_out)
#   input()
   out += [entry_out]
 
 return out
 



############# FIN de FUNCIONES

# Programa principal

import sys

step= 20

file_name2=str(sys.argv[1]) + ".cdd"
print(file_name2)

# Quizas incluir fecha y (hora?) en el nombre del 
# archivo del registro de la conversacion.
if ".cdd" in file_name2:
    file_name1= file_name2.replace(".cdd",".cod")


print(file_name1)

iden2= open( "TOKENS_CDD/" + file_name2,"r")
iden1 =open( "TOKENS_SET/" + file_name1,'w')

pp=[]
k=1

for renglon in iden2:
 if "END" in renglon: break
 if renglon[0]==".":
   l=len(renglon)
   eti = extrae1_alnum(renglon[1: l-1])
   if len(eti)==0:
     k=k+1
     continue
   else:
     pp += [[eti,k*step]]
     k=k+1
iden2.close
#print(pp)
#input()
#print("k= ",k)

iden2= open( "TOKENS_CDD/" + file_name2,"r")


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
foutput_i=[None]*99

# Se guardan los mensajes. Se escribiran al final, con etiquetas
# lifted de acuerdo al lugar del token
output_t=[]
Adial=[]

#print("inicia")
while True:
 if end==1: break
 label=[]
 l=0

# Lectura de tokens

# Turno cabeza de token
 for renglon in iden2:
#  print("renglon ", renglon)
  if len(renglon) < 2: continue
  if "END" in renglon:
   end=1
  if "#" in renglon:continue
#  print("sw,end = ", sw, end)
  if (sw==0 and end !=1):
#     print("token=",renglon)
     sw=1
     if "." in renglon:
       KK=KK+1
       token="."
       Adial+= [token]
       continue
     else: 
       KK=0
       token=renglon
       Adial=[token.replace("\n","")]
       continue
  if sw==1:
     if "{" in renglon:
       sw=2
       break
  else: 
#  ES NO ES ERROR??????????????????
#      print("error, esperaba { \n")
      break

# Turno de instrucciones del token
 if end==1: break
# print("Adial= ", Adial)
# print("turno instr token")
 for renglon in iden2:    
  datos=renglon.split()

# instruccion con etiqueta
#  print("\n ")
#  print("renglon= ",renglon)
  
  if (len(datos)>3):
# longitud 4,5, etc
   if "+" in datos[3]:
#    print("len>3 ",datos[3])
    n_instr = int(datos[0]) + (step * KK)
    t_instr = int(datos[1])
    if arg_est(t_instr):
       ap_instr= str(int(datos[2]))   
    else:
      if datos[2][0].isdigit():
        ap_instr= str(int(datos[2]) + (step * KK))
      else:
        ap_instr=str(find_in(len(pp),pp,datos[2]))

   else:
    n_instr = 0
    t_instr = int(datos[0])
    if arg_est(t_instr):
       ap_instr= str(int(datos[1]))   
    else:
      if datos[1][0].isdigit():
        ap_instr= str(int(datos[1]) + (step * KK))
      else:
        ap_instr=str(find_in(len(pp),pp,datos[1]))

  elif len(datos)==2:
# instruccion sin etiqueta
#    print("sin etiqueta")
    n_instr = 0
    t_instr = int(datos[0])
    if arg_est(t_instr):
       ap_instr= str(int(datos[1]))   
    else:
      if datos[1][0].isdigit():
        ap_instr= str(int(datos[1]) + (step * KK))
      else:
        ap_instr=str(find_in(len(pp),pp,datos[1]))

  else:
# longitud =3
#  print("len datos= ", len(datos))
#   print(renglon)
#   print("len==3 ", datos[2])
   if "+" in datos[2]:
    n_instr = 0
    t_instr = int(datos[0])
    if arg_est(t_instr):
       ap_instr= str(int(datos[1]))   
    else:
      if datos[1][0].isdigit():
        ap_instr= str(int(datos[1]) + (step * KK))
      else:
        ap_instr=str(find_in(len(pp),pp,datos[1]))

   else:

    n_instr = int(datos[0]) + (step * KK)
    t_instr = int(datos[1])
    if arg_est(t_instr):
       ap_instr= str(int(datos[2]))   
    else:
      if datos[2][0].isdigit():
        ap_instr= str(int(datos[2]) + (step * KK))
      else:
        ap_instr=str(find_in(len(pp),pp,datos[2]))

  if (n_instr >0):
    label += [[n_instr,i]]
    l=l+1

# guardamos la instruccion
  instr += [[n_instr, t_instr,ap_instr]]
  i=i+1
  if (t_instr==0): break

# fin del ciclo que  proceso un token (codigo)
# tenemos que actualizar etiquetas del token.

 i1=last_i
 instr[i1][0]= step * KK  
 while (instr[i1][1] !=0 and instr[i1][1] !="#"):
  if arg_salto(instr[i1][1]):
     l2= instr[i1][2]  
     l1 = ( step * KK ) + int(l2)
     instr[i1][2]= str(l2)
  i1=i1+1

# Genera salida de la instruccion en output_i
 output_i=[]
 if end==1: break
 i1=last_i
 while (instr[i1][1] !=0 and instr[i1][1] !="#"):
  output_i += [[str(instr[i1][0]) + " ", str(instr[i1][1]) + " ", instr[i1][2], "\n"]]
  i1=i1+1
#  output_i += ["\n"]
# checK_point= input("check point 1")
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


# Finalmente escribimos a archivo
gg= step * len(Adial)
# print("Final Adial= ",Adial)
for k in range(0, len(Adial)):
 if Adial[k]!= ".":
   escribe([ Adial[k], ["\n"], ["{"], ["\n"]  ])
# print(foutput_i[k] )
 escribe(filtra_exit(foutput_i[k],str(gg)) )
escribe([ [str(gg)," 9 ","0","\n"], [ "0 ","0 ","0","\n"]  ])
 

for k in range(0, len(output_t)):
 escribe(output_t[k])
escribe([ ["}"], ["\n"] ]) 

#### fin

iden1.close()
iden2.close


print;
print("*** fin de sesion ***")
print;






