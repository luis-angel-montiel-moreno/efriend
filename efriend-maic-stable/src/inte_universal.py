

# inte.py
# Interprete de dialogos simples
# Supone dos archivos dquasie entrada
# El primero: code.int
# Tiene el programa del script del dialogo.
# El segundo: emo.dic
# Es un diccionario de cosas como estados de animo, paises, etc.

# Se ejecuta como: python inte.py 
#
# Los programas "code.int" tienen instrucciones con 3 componentes enteros
# El primero es # de etiqueta (o 0), el segunto tipo de instruccion
# (abajo esta la lista) y el tercero es el argumentos del tipo de instruccion.

# 0 -> Fin fisico del programa, nunca lleva etiqueta.
# 1 -> pregunta profe
#    El argumento es un apuntador al texto que se despliega
#    El texto puede incluir variables @0, ..., @3.
# 2 -> alumno contesta
#    La respuesta queda registrada en la variable "vari"
# 3 -> alumno contesta si/no. No implica salto (# de linea es el tercer argumento)
# 4 -> Define variable
#    El tercer argumento es # de variable. El contenido de "vari" se copia a
#    variables[i], donde i es el # de variable (tercer argumento).    
# 5 -> alumno contesta si/no. Si implica salto (similar a 3)
# 6 -> Salto incondicional. Argumentos es # de linea.
# 7 -> Busca en diccionario. Argumentos indica el # de linea del diiccionario.
# 8 -> Salto si no esta en diccionario (ultimo uso de 7).
#    Argumento indica # linea del salto.  
# 9 -> nop. Ahora es fin logico del programa. Redirecciona a 0.
#10 -> registra edo de animo global {0,1,2,3,4,5}
#    La escala realmente la define el programador de Tokens. Pero se supone
#    -1 como indefinido.
#11 -> registra persepcion alumno escuela  {0,1,2,3,4,5}. Similar a 10.
#12 -> Define random. El argumento define el limite entero superior del random
#    Queda registrado en variable rr. Limite inferior es 1.
#13 -> Salto multiple segun variable aleatoria
#    Salto curioso. Por documentar ...
#14 -> Salta si edo_animo NO es 0 o 1. Salta  a argumento.
#15 -> Escribe directamente al archivo
#    El argumento es un apuntador al texto que se despliega
#    El texto puede incluir variables @0, ..., @3.
#16 -> Busca en diccionario. Argumentos indica el # de linea del diiccionario
# Similar a 7, la diferencia es que la longitud de la palabra buscada y la
# del diccionario deben coincidir.
#17 -> Si No loop salta.
#18 -> recupera informacion personal
# Argumento es etiqueta (tipo #1) pro con formato incluyendo posiblemente
# placeholders *. Se realiza match contra info. Personal del usuario
# resultado queda en variables @0, ...
# 19 -> no se usa aqui. EXIT GLOBAL. SE traduce a #6 etc
#20 -> Salta si perpecion alumno NO es 0 o 1. Salta  a argumento.
# 21 -> entra opcion FAQ  ????? LUIS
# 22  -> lectura digito
# 23  -> reset rr (rr=0)
# 24  -> vari=str(rr)
# 25  -> if rr > 0 salta tercer argumento

# Inicio de Funciones

# obten entero al inicio de una cadena
def obten_digitos_inicio(cadena):
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


# elimina blancos
# Por lo pronto uso exclusivo en find_almost_in1
# quita los blancos del patron para formatear hechos.
def remove_bl(cadena):
  if " " in  cadena: cade1= ajusta_bl(cadena.replace(" ", ""))
  else: cade1=cadena
  return cade1



# elimina control r
# Por lo pronto uso exclusivo en ???
# 
def el_contr_l(cadena):
  if "\r" in  cadena: cade1= el_contr_l(cadena.replace("\r", ""))
  else: cade1=cadena
  return cade1

# Filtrito 1
# Por lo pronto uso exclusivo en opcion # 15 (escribe archivo)
# Cambia los blancos x giones bajos (_)del patron para formatear a hechos.
def trblTogb(cadena):
  if " " in  cadena: cade1= ajusta_bl(cadena.replace(" ", "_"))
  else: cade1=cadena
  return cade1



# Elimina blancos despues de cada cambio de linea
# Recursivo x 2 razones: just for fun e ignorancia.
# O sea no se si iterativo funcionaria
# x esto de la inmutabilidad de las cadenas
def ajusta_bl(cadena):
  if "\n " in  cadena: cade1= ajusta_bl(cadena.replace("\n ", "\n"))
  else: cade1=cadena
  return cade1

# Quita c_ del argumento de un hecho
def ajusta_hecho(cadena):
  if "c_" in  cadena: cade1= ajusta_hecho(cadena.replace("c_", ""))
  else: cade1=cadena
  return cade1

# Sustituye & por "cambio de linea"
def incerta_cl(cadena):
  if "&" in  cadena: cade1= incerta_cl(cadena.replace("&", "\n"))
  else: cade1=cadena
  return cade1

# Encuentra el # de linea asociado a una etiqueta
# Arreglo con l elementos
# eti es la etiqueta a buscar
def no_etiqueta(l,arreglo,eti):
 for k in range(0,l):
  if arreglo[k][0]==eti:
    return arreglo[k][1]

# checa si c3 (diccionario) es subcadena de c4 desde el inicio
# admitiendo permutacion de 2 caracteres
# Precondicion: hay discrepancia exactamente en 2 caracteres
def sinpermutacion(c3,c4):
 k=0
 for i in range(0, len(c3)):
   if c3[i] != c4[i]:
     if k==0:
        p1=i
        k=1
     else: p2=i
 if p2 != p1+1: return True
 if  c3[p1] != c4[p2]: return True
 if  c3[p2] != c4[p1]: return True
 return False

 

## TEma central checar cadena contra diccionario

# Compara (sin) comodines
# caso :) no considerado (bien) todavia
# c1 cade de diccionario, c2 cadena de entrada
# checa si cadena c1 es subcadena de c2, iniciando en algun lado de c2.
# Requisito es que un caracter anterior de c2 donde hay coincidencia
# sea un blanco. O sea la coincidencia debe ocurrir al inicio de una palabra,
# nunca en medio
# Acepta un error de caracter
# o permutacion de 2 caracteres
def almost_subc(c1,c2):
 if len(c2) < len(c1): return False
 if "*" in c1: return False
# print ("compara c1,c2 ", c1,c2)
# k cuenta errores en la comparacion
 k=0

# buscamos inicio de subcadena para coincidencia
 sw=0
 for j in range(0, len(c2)):
   if  c1[0] != c2[j]: continue
   sw=1
   break
 if sw==0: return False

# la coincidencia esta en c2[j] 
# o sea c1[0]= c2[j] precondicion para el resto del codigo.
# print("paso sw=0")
# En el resto de cadena de c1 debe  existir espacion para comparar con c2
# En otro caso es falso.
 if len(c2) -j < len(c1): return False
# print("paso prueba de longitud")
 
# Precondicion: Coincidencia en primer caracter y hay longitus apropida para 
# comparar, resta llevar a cabo la comparacion de cadenas.
# recordemos que k contara errores de coincidencia
 for i in range(0, len(c1)):
   if c1[i] != c2[i+j]: k=k+1
# print("k= ",k)
 if k == 0:
#   print("k=0, true")
# sin errores !!!
   if (j > 0 and c2[j-1] != " "):
     return almost_subc(c1,c2[j+1: ])

   return True

# Checamos si hay mas de 2 errores es inaceptable y hacemos recursion
# para checar mas adelante en la cadena c2.

 if k> 2:
    return almost_subc(c1,c2[j+1: ])
 elif k > 1:
    if sinpermutacion(c1,c2[j: ]):
      return almost_subc(c1,c2[j+1: ])
# if (j > 0 and c2[j-1] != " "): almost_subc(c1,c2[j+1: ])
# Porque la linea de abajo??? veo que k==0 y paso el test anterior
# empiricamente parece funcionar, pues de lo contrario reconoce nonsense
 if len(c1) < 4: return False
# print("True ?")
 return True


        

# C1 con  posibles comodines
# Efecto secundario. Placeholders (*) se almacenan en arreglo variables.
def almost2_subc(c1,c2):
 global variables
 ii=0
 c3 =c1 + " "
 c4 = c2 + " "
 lista_c3= c3.split(" ")
 lista_c4= c4.split(" ")
# print("lista_c3= ", lista_c3)
# print("lista_c4= ", lista_c4)
# print("len c3,c4 =", len(lista_c3), len(lista_c4))
# AGREGUE
 if len(lista_c3) != len(lista_c4): return False

 if len(lista_c4) < len(lista_c3): return False
# print("len(lista)", len(lista_c3))
# letra= input("inicia busqueda")
 for j in range(0, len(lista_c3)-1):
 #     print("j=", j)
 #     print(lista_c3[j], "---", lista_c4[j])
      if  lista_c3[j] == lista_c4[j]:
        if lista_c3[j] == "*":
            variables[ii]= lista_c4[j]
            ii= ii+1
 #       print("corresponden")
        continue
      if  lista_c3[j]=="*":
        variables[ii]= lista_c4[j]
        ii= ii+1
#        print("ii, variables ", ii, variables)
        continue
      else:
#       print("FALSO")
       return False
# print(variables)
 return True

# Funcion central sobre comparacion
# Determina si cadena "quasi" ocurre en lcadenas
# CAMBIOS RECIENTES
def find_quasi_in(flag, cadena, lista_dict):
  global variables
  global c1
  c2= str.lower(cadena)
#  for j in range(0, len(lista_dict)-1): #  AGUAS 22 nov
  for j in range(0, len(lista_dict)):
    cad= lista_dict[j].replace("\n","")
    c1= str.lower(cad)
    if (flag==1 and len(c1) != len(c2)): continue
#    print("c1,c2 =", c1, " # ", c2)
    if almost_subc(c1, c2):
#        print("ENCONTRADA almost_sub")
        return True     
#    print("No encontrada almost_sub")
#    if almost1_subc(c1, c2):
#        return True
    if almost2_subc(c1, c2):
#        print("ENCONTRADA almost2_sub")
#        print("c1,c2 =", c1, " ### ", c2)
        return True
  return False

 
# Funcion util sobre comparacion
# Determina si cadena "almost" ocurre en lcadenas
# CAMBIOS RECIENTES
def find_almost_in1(cadena, lcadenas):
  global variables
  global c1
#  print("llegue almost", lcadenas)
#  letra = raw_input()
  lista_dict= lcadenas.split(".") # antes ;
#  print("lista_dict ", lista_dict)
#  letra = raw_input()
  c2= str.lower(cadena.replace("\n",""))
#  print("c2 ", c2)
  for j in range(0, len(lista_dict)-1):
#    print("j=",j)
    cad= lista_dict[j].replace(")"," ).")
#    print("cad ", cad)
    c1= str.lower(cad) 
#    print("c1, c2 ", c1, "//", c2)
    if len(c2) > len(c1): continue
 #   print("c1, c2 ", c1, "//", c2)
    if remove_bl(c2)==remove_bl(c1):
        return True
#    print("checara almost2")
    if almost2_subc(c2, c1):
        return True

  return False

          
### Fin de tema central checar cadenas

####  LECTURAs 
 
# Lectura simple
# prompt es >
# Uso raw_input en mi otra version de python, la de Linux (NO olvidar)

def lect():
    while True:
      try:
          letra = input("Dime>>>")
          break
      except ValueError:
          print("Oops! Try again")
    iden1.write("\n>>>")
    return letra

# lectura Si o No
def lect1():
    while True:
          letra = str.lower(lect())
          if "no" in letra: break
          elif "si" in letra: break
          else: print ("Oops! No entiendo, intente de nuevo x fa")
    return letra

# lectura numeros 0 al 10
def lect2():
    while True:
          ddd= lect()
          if ddd.isdigit(): 
            num = int(ddd)
            if (num >= 0 and num <= 9): break
            else: print("numero incorrecto, intente de nuevo x fa")
          else: print("requiero numero x fa")
    return num

#### Fin de lecturas

# transforma lista a cadena y semi-formatea
def formato(lista): 
  cadena=[]
  for j in range(0,len(lista)):
   if lista[j][0]=="{":  cadena += [ lista[j][1: ].replace("}","") ]
   else:
     cade= lista[j].replace("\n","")
     cade1= cade.replace(".", ".\n")
     cade2= cade1.replace("?", "?\n")
     cade3= cade2.replace(":)", ":)\n")
     cade4= cade3.replace("!", ":\n")
     cadena += [ incerta_cl(ajusta_bl(cade4.lstrip()))]
  cad1=""
  cad1 = cad1.join(cadena)
  return cad1

# busca el nombre de la variable correspondiente (Solo de 0 a 3 x lo ponto)
# La invoca la opcion 1 del dialogo.
def encuentra_nombre_var(msj): 
  if "@0" in msj: msj0= msj.replace("@0", variables[0])
  else: msj0=msj
  if "@1" in msj0: msj1= msj0.replace("@1", variables[1])
  else: msj1=msj0
  if "@2" in msj1: msj2= msj1.replace("@2", variables[2])
  else: msj2=msj1
  if "@3" in msj2: msj3= msj2.replace("@3", variables[3])
  else: msj3=msj2
  return msj3

def quita_acentos(str):
  valores = "abcdefghijklmnopqrstuvwxyz0987654321 +=.,?¿{}/|@·#()<>:-\n\\"
  strR = ""
  for xx in str:
    xa=xx.lower()
    if (not xa in valores):
 #     print(ord(xx))
      yy= "*"
      if (ord(xx)== 227): continue
      if (ord(xx)== 194): continue
      if (ord(xx)== 195): continue
      if (ord(xx)== 226): continue
      if (ord(xx)== 161): yy= "á"
      if (ord(xx)== 169): yy= "é"
      if (ord(xx)== 131): yy= ""
      if (ord(xx)== 173): yy= "í"
      if (ord(xx)== 179): yy= "ó"
      if (ord(xx)== 186): yy= "ú"
      if (ord(xx)== 177): yy= "ñ"
      if (ord(xx)== 34): yy= "¿"
      strR = strR + yy 
    else:
      strR = strR + xx
  return strR
    
   
#  return str.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')

  return str.replace('\n','')

# LECTURAS de ARCHIVOS (Muy particular)

# Lectura de la inf personal del usuario
def getInfP():

 pp=[]  
 file_name2= "agents_knowledge/MAIC_KR/universal/questions_made.clasp"
 iden2 =open(file_name2,encoding="latin-1")
 for renglon in iden2:
  if renglon[0]=="%" : continue
#  print(renglon)
  if "\n" in renglon:
    pe= renglon.replace("\n","")
    pa=ajusta_hecho(pe)
  else:
    pa=ajusta_hecho(renglon)
#  print(pa)
  p1= pa.replace("(", "( ")
  p2= p1.replace(").\r", " ).").replace(","," , ")
#  print(p2)
  pp= pp + [p2]
 iden2.close

# print(pp)

 qq=[]
 file_name2= "agents_knowledge/MAIC_KR/universal/preguntasCine.clasp"
## iden2 =open(file_name2,"r")
 iden2 = open(file_name2,encoding="latin-1") 
 for renglon in iden2:
  if renglon[0]=="%" : continue
#  print(renglon)
  if "\n" in renglon:
    qa= renglon.replace("\n","")
  else:
    qa=renglon
  q1= qa.replace("(", "( ")
  q2= q1.replace(").", ").").replace(","," , ")
  qq= qq + [q2]
 iden2.close

 rr= "".join(pp+qq)
 # print(rr)

 return rr


# lectura archivo de instrucciones
def lect_instr(iden):
 global instr, label
# l es contador de etiquetas.
 l=0
# i es contador de # de instruccion
 i=0
 for renglon in iden2:
  if "#" in renglon:
     label += [[0 ,i]]
     l=l+1
# Se almacena el "token" que debe venir en renglon
     instr += [[0, 9, renglon]]
     i=i+1
     continue
  datos=renglon.split()
  n_instr = int(datos[0])
  t_instr = int(datos[1])
  ap_instr = datos[2]
  label += [[n_instr,i]]
  l=l+1
  instr += [[n_instr, t_instr,ap_instr]]
  i=i+1
  if (t_instr==0): break

 i=0
# CHECAR BIEN instr[i][1] !="#" ??????????????
 while (instr[i][1] !=0):
  if (instr[i][1] ==3 or instr[i][1]==5  
        or instr[i][1]==6  or instr[i][1]==8
        or instr[i][1]==13 or instr[i][1]==14 
        or instr[i][1]==20 or instr[i][1]==17 or instr[i][1]==25):
     instr[i][2]= no_etiqueta(l,label, int(instr[i][2]))
  i=i+1


# Lectura archivo de parejas, Id, texto
def lect_msj(iden,dict):
 for renglon in iden:
  if "#" in renglon[0]: continue
  if renglon[0].isdigit():
      dict+=[ [obten_digitos_inicio(renglon),[el_contr_l(elimina_digitos_inicio(renglon))]  ]  ]
  else:
      X=dict.pop()
      X2=X.pop()
      X1=X.pop()
      dict+=[ [X1, el_contr_l(agrega(X2, renglon )) ]  ]
 return dict

##### FIN de lecturas

# Da formato a la segunda entrada de cada elemento de dict
def da_formato(dict):
 for k in range(0, len(dict)):
  X=dict[k]
  X2=X.pop()
  X1=X.pop()
  dict[k]= [X1, formato(X2)]
 return dict

# dialogo Super central del programa

def dialogo(dict2,dict3):
 global iden1, iden2, edo_animo, perc_esc, instr, variables
 global c1
 global num_ses
 infP= getInfP()
# print(infP)
 test= find_almost_in1("contador( * ).", infP)
 if test >0 :
   num_ses=variables[0]
 else :
   num_ses=0
# print(" sesion numero ", num_ses)
# print("\n")
# print(infP)
# variables =[None]*4
# print("hola\n")
 entiendo=0
 loop=0
 i=0
 j=0
 rr=0
 var_txt =[]
 while (instr[i][1] !=0):
  tipo_instr=instr[i][1]
#  print( tipo_instr)
  
  if (tipo_instr==0):
    print("opcion 0")
    break

  elif (tipo_instr==1):
   msj=no_etiqueta(len(dict2), dict2, int(instr[i][2]))
   msj3= encuentra_nombre_var(msj)
   print(quita_acentos(msj3)) #aqui funcion que quita los acentos
   iden1.write(msj3)
   i=i+1

  elif (tipo_instr==2):
 # alumno contesta
   letra=lect()
   vari=letra
   i=i+1
   iden1.write(letra)
   print("\n")
   iden1.write("\n")


  elif (tipo_instr==3):
    print("Responde (Si,No) x fa:")
    letra=lect1()
    vari=letra
    iden1.write(letra)
    print("\n")
    iden1.write("\n")
    if "no" in letra: i= int(instr[i][2])
    else:
     rr = rr + 1
     i=i+1

  elif (tipo_instr==4):
     variables[int(instr[i][2])]=vari
     i=i+1

  elif (tipo_instr==5):
    print("Responde (Si,No) x fa:")
    letra=lect1()
    vari=letra
    iden1.write(letra)
    print("\n")
    iden1.write("\n")
    if "si" in letra: i= int(instr[i][2])
    else:
       rr = rr + 1
       i=i+1

  elif (tipo_instr==6): i= int(instr[i][2])

  elif (tipo_instr==7):
    no_dict= int(instr[i][2])
#    if (no_dict==2086): print("checo dict ", no_dict)
    ett= no_etiqueta(len(dict3), dict3, no_dict)
#    if (no_dict==2086):
#      print("ett,vari=  ", ett,vari)
#      raw_input(">>>")
    entiendo= find_quasi_in(0, vari, ett)
    if entiendo: vari=c1
#   en c1 queda la cadena encontrada del dict
#    if (no_dict==2086):
#       raw_input(">>>")
#       print("Status Encontro en dict=", entiendo)
#       raw_input(">>>")
    i=i+1

#  variable "entiendo" booleana (Esta o no en diccionario)
  elif (tipo_instr==8):
    if entiendo:
       i= i+1
    else:
       i= int(instr[i][2])

  elif (tipo_instr==9): 
  #  NO me acuerdo porque?
     if "#" in instr[i][2]:
       iden1.write(instr[i][2])
       iden1.write("\n")
     i=i+1

#  variable "loop" booleana (Esta o no ciclado)
  
  elif (tipo_instr==10):
     edo_animo=int(instr[i][2])
     i=i+1
 
  elif (tipo_instr==11):
     perc_esc=int(instr[i][2])
     i=i+1
 
  elif (tipo_instr==12):
     lim_rand=int(instr[i][2])
     rr= random.randint(1, lim_rand)
     i=i+1

  elif (tipo_instr==13): i= int(instr[i][2]) + (rr-1)*2
 
  elif (tipo_instr==14):
    if (edo_animo > 0 and edo_animo < 2):
       i= i+1
    else:
       i= int(instr[i][2])

  elif (tipo_instr==15):
   msj=no_etiqueta(len(dict2), dict2, int(instr[i][2]))
   msj3= encuentra_nombre_var(msj)
   iden1.write(trblTogb(msj3))
   i=i+1

  elif (tipo_instr==16):
    no_dict= int(instr[i][2])
    ett= no_etiqueta(len(dict3), dict3, no_dict)
    entiendo= find_quasi_in(1, vari, ett)
#   en c1 queda la cadenna encontrda del dict
    if entiendo: vari=c1

    i=i+1

  elif (tipo_instr==17):
    if loop:
       i= i+1
    else:
       loop=1
       i= int(instr[i][2])

  elif (tipo_instr==18):
    msj1=no_etiqueta(len(dict2), dict2, int(instr[i][2]))
    msj=msj1.replace("\n", "")
#    print("msj ", msj)
#    print("infP ", infP)
    rr= find_almost_in1(msj, infP)
    entiendo =rr
    if entiendo: vari=c1
#    print("rr ", rr)
    i= i+1

  elif (tipo_instr==20):
    print("opocion 20: ",perc_esc)
    if (perc_esc > 0 and perc_esc < 2):
       i= i+1
    else:
       i= int(instr[i][2])

  elif (tipo_instr==21):
    print("entra opcion faq.")
    menuFaqPython.browserFAQ()
    i = i+1

  elif (tipo_instr==22):
   rr= lect2()
   letra=str(rr)
#  Se agrego 14 feb
   vari=letra
   i=i+1
   iden1.write(letra)
   iden1.write("\n")

  elif (tipo_instr==23):
   rr=0
   i=i+1

  elif (tipo_instr==24):
   vari=str(rr)
   i=i+1
  elif (tipo_instr==25):
    if rr >0: i= int(instr[i][2])
    else: i=i+1


  else: 
    print("ERROR (OPcion invalida)")
    letra = raw_input("?")
    iden1.write("\n")
  

def protocolo_final(iden):
 global edo_animo, perc_esc
 global datetime_object
 print("Es todo x hoy, gracias :)")
 iden.write("Es todo x hoy, gracias :)")
 iden.write("\n")
 iden.write("Animo inicial =")
 iden.write(str(edo_animo))
 iden.write("\n")
 iden.write("Perc. escuela =")
 iden.write(str(perc_esc))
 iden.write("\n")
 iden.write("FechaHora =")
 iden.write(datetime_object)
 iden.write("\n")
 print("Serias tan anable de evaluarme x fa?")
 iden.write("Serias tan amable de evaluarme x fa?\n")
 iden.write(">>>")
 print("Muy chafa=0, ... Super=9:")
 eval=lect2()
 iden.write(str(eval))
 iden.write("\n")
 print(" Grcs :)")
 print(" Que estes super!!!")

############# FIN de FUNCIONES

# Programa principal

global iden1, iden2, edo_animo, perc_esc, instr, variables, datetime_object

variables =[None]*4


import random
from universal import mydict

# import faq menu browser
from universal import menuFaqPython

import datetime
datetime_object = str(datetime.datetime.now())

# Inician indefinidas
edo_animo=0
perc_esc =0

#file_name=sys.argv[1]


file_name="tmp/code.int"
###iden2= open(str(file_name),"r")

iden2 = open(file_name,encoding="latin-1") 

# Quizas incluir fecha y (hora?) en el nombre del archivo del registro de la conversacion.
if ".int" in file_name: file_name1= file_name.replace(".int",".cnv")
else: file_name1= 'tmp/sesion.cnv'

# Abre archivos e inicializa 
iden1 =open(file_name1,'w',encoding="latin-1")

#iden3 =open("emo.dic","r")
#iden3 = open("emo.dic",encoding="latin-1") 

# Programa. Lista con entradas de 3 elementos
instr=[]
label=[]


# Lectura instrucciones del codigo dialogo
# Dos partes: Turno instrucciones y despues turno mensajes
# turno instrucciones
lect_instr(iden2)

# Turno del texto mensajes

# Esto esta muy muy chafa x mejorar
# Lee mensajes del archivo y dejalos en dict

dict3=[]
dict2=[]

# Lectura mensajes de e-friend para desplegar
dict2=lect_msj(iden2,dict2)


#lectura diccionario(emociones, etc
#dict3=lect_msj(iden3,dict3)

dict2=da_formato(dict2)

#lectura diccionario(emociones, etc
dict3=mydict.leeDict()

#### Inicio del dialogo

dialogo(dict2,dict3)

protocolo_final(iden1) 

iden1.close()
iden2.close
##iden3.close

print;
print("*** fin de sesion ***")
print;






