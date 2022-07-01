import random

print("-" * 50)
print("Generación \n\tde Estadísticas \n\t\tsobre COVID-19")
print("-" * 50)

def menu():                     #Printeo del menu
    print("-" * 100)
    print("1-Cantidad de casos confirmado y porcentaje sobre el total de casos.")
    print("2-Edad promedio de los pacientes que pertenecen a grupo de riesgo.")
    print("3-Cantidad y porcentaje que el personal de salud representa sobre el total de casos.")
    print("4-Edad promedio entre los casos confirmados.")
    print("5-Menor edad entre los casos autóctonos.")
    print("6-Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el total de casos")
    print("7-Cantidad de casos confirmados con viaje al exterior.")
    print("8-Cantidad de casos sospechosos en contacto con casos confirmados.")
    print("9-Las regiones sin casos confirmados.")
    print("10-Porcentaje de casos positivos autóctonos sobre el total de positivos.")
    print("11-Salir")
    print("-" * 100)

def validacion():                           #Funcion para validar la cuenta
    cant_arroba, cont_error, = 0, 0,
    while cont_error < 3:
        cuenta = input("-Ingrese su cuenta (nombre@dominio)\n- ")
        for letra in cuenta:
            if cuenta[0] == "@" or cuenta[0] == "." or cuenta[len(cuenta)-1] == "@" or cuenta[len(cuenta)-1] == "." :
                cont_error += 1
                print("La cuenta no puede empezar ni terminar con un (@) o (.) , reingrese una valida")
                break
            else:
                if not "@" in cuenta:
                    print("ERROR! ,la cuenta no contiene un (@) , reingrese una valida")
                    cont_error += 1
                    break
                else:
                    if letra == "@":
                        cant_arroba += 1
                        if cant_arroba > 1:
                            print("ERROR! , la cuenta contiene mas de un (@), reingrese una valida")
                            cont_error += 1
                            break
                        else:
                            if ".." in cuenta:
                                print("ERROR! , la cuenta contiene dos puntos seguidos, reingrese una  valida")
                                cont_error += 1
                                break
                            else:
                                return True


def valores(v):             #Generacion aleatoria de datos y procedimientos
    pacientes,confirmados,suma_edades,cant_pac_riesgo,cont_pers,edad_conf,total_auto,exterior,sospechoso,capital,gcba,norte,sur,menor_edad_autoc,porcentaje = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    autoctono = False
    for i in range(v):
      pacientes += 1
      edad = random.randint(1,100)
      resultado = random.choice(["Positivo" , "Negativo"])
      if resultado == "Positivo":
          confirmados += 1
          porcentaje = (confirmados * 100) / v
          edad_conf += edad
      region = random.choice(["Capital", "Gran Córdoba", "Norte", "Sur"])
      if resultado == "Positivo" and region == "Capital":
          capital += 1
      if resultado == "Positivo" and region == "Gran Córdoba":
          gcba += 1
      if resultado == "Positivo" and region == "Norte":
          norte += 1
      if resultado == "Positivo" and region == "Sur":
          sur += 1
      if edad > 21:
          if edad < 65:
            personal_salud = random.choice(["Si","No"])
            if personal_salud == "Si":
                cont_pers += 1
      if edad < 21 :
          personal_salud = ("No")
      if edad >= 60:
          suma_edades += edad
          cant_pac_riesgo += 1
      viaje = random.choice(["Si","No"])
      if resultado == "Positivo" and viaje == "Si":
          exterior += 1
      contacto = random.choice(["Si","No"])
      print("Paciente numero : ", pacientes)
      print("La edad del paciente es de : ", edad)
      print("El resultado del test es : ", resultado)
      print("La region donde reside el paciente es : ", region)
      print("El paciente es personal de salud : ", personal_salud)
      print("El paciente viajo al exterior : ", viaje)
      print("El paciente tuvo contacto con casos confirmados:", contacto)
      if resultado == "Negativo" and contacto == "Si":
          sospechoso += 1
      if viaje == ("No") and resultado == ("Positivo") and contacto == ("No")  and personal_salud == ("No"):
          autoctono = True
          total_auto += 1
          print("El paciente es un caso autoctono")
          if total_auto == 1:
              menor_edad_autoc = edad
          else:
              if edad < menor_edad_autoc:
                  menor_edad_autoc = edad

      else:
          print("El paciente no es un caso autoctono")
      print(40 * '-')

    opcion = 1               # Menu de inicio
    while opcion != 11:
        menu()
        opcion = int(input("Ingrese el numero de la opción elegida\n- "))
        if opcion == 1:
            print("Pacientes confirmados = ", confirmados, " Porcentaje :  ", round(porcentaje, 2), "%")
        if opcion == 2:
            promedio_edad = suma_edades / cant_pac_riesgo
            print("La edad promedio del grupo de riesgo es de : ", int(promedio_edad),"años")
        if opcion == 3:
            promedio_salud =  (cont_pers * 100) / v
            print("Promedio de cantidad de personal de salud : ", round(promedio_salud, 2), "%")
        if opcion == 4:
            promedio_edad_conf = edad_conf / confirmados
            print("La edad promedio de los casos confirmados es de : ", int(promedio_edad_conf), "años" )
        if opcion == 5:
            if autoctono == True:
                print("La menor edad de los casos autoctonos es de : ", int(menor_edad_autoc), "años" )
            else:
                print("No se registraron casos autoctonos")
        if opcion == 6:
            print("Cantidad de casos confirmados por region y porcentaje sobre el total de casos : ")
            print("Capital : ",capital,"casos" "\nPorcentaje",round((capital * 100 / v),2),"%","\n<--------------------------->")
            print("Gran Córdoba : ",gcba,"casos" "\nPorcentaje : ",round((gcba * 100 / v),2),"%","\n<--------------------------->")
            print("Norte : ",norte,"casos" "\nPorcentaje : ",round((norte * 100 / v),2),"%","\n<--------------------------->")
            print("Sur : ", sur,"casos" "\nPorcentaje : ",round((sur * 100 / v),2),"%","\n<--------------------------->")
        if opcion == 7:
            print("La cantidad de casos confirmados con viaje al exterior es : ", exterior, "personas")
        if opcion == 8:
            print("La cantidad de casos sospechosos por contacto con casos confirmados es : ", int(sospechoso), "personas")
        if opcion == 9:
            print("Las regiones sin casos confirmados son : ")
            if capital == 0:
                print("- Capital")
            if gcba == 0:
                print("- Gran Córdoba")
            if norte == 0:
                print("- Norte")
            if sur == 0:
                print("- Sur")
            if capital >= 1 and gcba >= 1 and norte >= 1 and sur >= 1:
                print("- Todas las regiones tienen casos confirmados - ")
        if opcion == 10:
            por_auto = (total_auto * 100) / confirmados
            print("El porcentaje de casos positivos autóctonos sobre el total de positivos es de : ", round (por_auto, 2), "%")

if validacion():        #Ejecucion del programa
    print("La cuenta ingresada es correcta")
    pacientes = int(input("Ingrese la cantidad de pacientes\n- "))
    valores(pacientes)
else:
    print("\n\tHa excedido los 3 intentos validos\n\t\t\tFin del programa")
