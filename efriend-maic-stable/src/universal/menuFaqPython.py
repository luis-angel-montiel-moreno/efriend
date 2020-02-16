#! programa faq

from xml.dom.minidom import parse
import xml.dom.minidom



def imprimeMenuSeccion():
   str = "Elige una seccion de preguntas:" + "\n"
   str = str + " 1." + "Mindfulness" + "\n"
   str = str + " 2." + "Coaching" + "\n"
   print(str)	


def obtenSeccion(numero):
   str = ""
   if numero==1:
      str = "mindfulness"
   elif numero==2:
      str = "coaching"
   return str

"""
Elige un tipo de pregunta:
 1.que
 2.como
 3.cual
 4.porque
 5.tiene
 6.tiene que ver
 7.es
 8.interesa pero
 9.cuanto
 10.hay
 11.donde
 12.para que
"""
def imprimeMenuTipo():
   str = "Elige un tipo de pregunta:" + "\n"
   str = str + " 1." + "que" + "\n"
   str = str + " 2." + "como" + "\n"
   str = str + " 3." + "cual" + "\n"
   str = str + " 4." + "porque" + "\n"
   str = str + " 5." + "tiene" + "\n"
   str = str + " 6." + "tiene que ver" + "\n"
   str = str + " 7." + "es" + "\n"
   str = str + " 8." + "interesa pero" + "\n"
   str = str + " 9." + "cuanto" + "\n"
   str = str + " 10." + "hay" + "\n"
   str = str + " 11." + "donde" + "\n"
   str = str + " 12." + "para que" + "\n"
   print(str)	


def obtenTipo(numero):
   str = ""
   if numero==1:
      str = "que"
   elif numero==2:
      str = "como"
   elif numero==3:
      str = "cual"
   elif numero==4:
      str = "porque"
   elif numero==5:
      str = "tiene"
   elif numero==6:
      str = "tieneQueVer"
   elif numero==7:
      str = "es"
   elif numero==8:
      str = "interesaPero"
   elif numero==9:
      str = "cuanto"
   elif numero==10:
      str = "hay"
   elif numero==11:
      str = "donde"
   elif numero==12:
      str = "paraQue"
   return str



def getPreguntasByTipo(seccion, tipoPregunta):
   # Open XML document using minidom parser

   doc = xml.dom.minidom.parse("agents_knowledge/SLAVES_TASKS/faq_task/preguntasMindfulness.xml")
   FAQ = doc.getElementsByTagName("FAQ")[0]
   if FAQ.hasAttribute("tipo"):
      print("FAQ:"+FAQ.getAttribute("tipo"))
   # Get all the movies in the collection
   preguntas = doc.getElementsByTagName("preguntas")[0]
   if preguntas.hasAttribute("tipo"):
      print("preguntas:"+preguntas.getAttribute("tipo"))

   listasPFaq = preguntas.getElementsByTagName("listaPreguntasFAQ")

   nPreg = 0
   for listaPreguntasFaq in listasPFaq:
      if listaPreguntasFaq.getAttribute("seccion")==seccion:
         if listaPreguntasFaq.hasAttribute("seccion"):
            print("listaPreguntasFAQ:"+listaPreguntasFaq.getAttribute("seccion"))

         preguntasFaq = listaPreguntasFaq.getElementsByTagName("preguntaFAQ")

         for p in preguntasFaq:
            if p.getAttribute("tipoPregunta")==tipoPregunta: 
               print("**********")
               if p.hasAttribute("numero"):
                  print("Numero: "+p.getAttribute("numero"))
               pregunta = p.getElementsByTagName('pregunta')[0]
               print("\nPregunta:\n"+pregunta.childNodes[0].data)
               respuesta = p.getElementsByTagName('respuesta')[0]
               print("\nRespuesta:\n"+respuesta.childNodes[0].data)
               nPreg = nPreg + 1
               if nPreg%3==0: raw_input("\npresiona <<Enter>> para continuar viendo resultados. ")


def preparaFuncion(tipoPregunta):
	getPreguntasByTipo("mindfulness",tipoPregunta)

def lecturaNumero(lowerb,upperb):
   numero = 0
   while True:
      try:
         numeroStr = raw_input("Selecciona opcion numerica>>")
         if numeroStr.isdigit():
            numero = int(numeroStr)
            if(numero>=lowerb and numero <=upperb): break
            else: 
               print ("numero incorrecto, por favor intente de nuevo")
         else:
            print("numero requerido, por favor intente de nuevo")
      except ValueError:
         print("Oops! vuelve a intentar")
      print("\n>>>")
   return numero


def browserFAQ():
   while True:
      imprimeMenuSeccion()
      nseccion= lecturaNumero(1,2)
      imprimeMenuTipo()
      ntipo = lecturaNumero(1,12)
      getPreguntasByTipo(obtenSeccion(nseccion),obtenTipo(ntipo))
      print("\ndesea volver a navegar en FAQ?, seleccione: 1. si, 2. no.")
      nopcion = lecturaNumero(1,12)
      if nopcion==2: break


#browserFAQ()

"""
i = 0
while i<11:
   print(obtenTipo(i))
   i = i + 1
"""
#getPreguntasByTipo(obtenSeccion(2),obtenTipo(1))
#getPreguntasByTipo("mindfulness","que")
#gtPreguntasByTipo("coaching","que")



