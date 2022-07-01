#Trabajo practico sobre diagnostico de covid-19

print("~~~DETECCIÓN COVID-19~~~")
edad = int(input("Ingrese su edad: "))
neu = int(input("¿Evidencia neumonía? \n1-Si\n0-No\n- "))

if neu == 1:
    print("\tADVERTENCIA !")
    print("CASO SOSPECHOSO: Llame al Centro de Salud más cercano")    #Neumonia (caso directamente sospechoso)
elif neu == 0:
    temp = float(input("Ingrese temperatura corporal: "))
    if temp <= 37:
        if edad >= 60:  #Grupo de riesgo por edad
            print("CASO NO SOSPECHOSO. Por su edad, pertenece al grupo de riesgo. Aconsejamos NO SALIR de su casa")
        elif edad < 60:
            print("CASO NO SOSPECHOSO. Respete las normas del Gobierno y quedese en su casa.")

    elif temp > 37:      #Si la temperatura es mayor a 37
        sintomas = 0
        tos = int(input("¿Presenta tos? \n1-Si\n0-No\n- "))
        if tos == 1:
            sintomas += 1
        odinofagia = int(input("¿Presenta odinofagia? \n1-Si\n0-No\n- "))
        if odinofagia == 1:
            sintomas += 1
        dif_res = int(input("¿Presenta dificultad respiratoria? \n1-Si\n0-No\n- "))
        if dif_res == 1:
            sintomas += 1
        if sintomas == 0:
            print("CASO NO SOSPECHOSO. Respete las normas del Gobierno y quedese en su casa.")

        elif sintomas >= 1:    #Si tiene un sintoma o mas
            personal_salud = int(input("¿Usted es personal de Salud?, \n1-Si\n0-No\n- "))
            if personal_salud == 1:
                print("\tADVERTENCIA !")
                print("CASO SOSPECHOSO: Llame al Centro de Salud más cercano")
            elif personal_salud == 0:
                contacto = int(input("¿En los últimos 14 días estuvo en contacto con casos confirmados?, \n1-Si\n0-No\n- "))
                if contacto == 1:
                    print("\tADVERTENCIA !")
                    print("CASO SOSPECHOSO: Llame al Centro de Salud más cercano")
                elif contacto == 0:
                    exterior = int(input("¿En los últimos 14 días viajó al exterior?, \n1-Si\n0-No\n- "))
                    if exterior == 1:
                        print("\tADVERTENCIA !")
                        print("CASO SOSPECHOSO: Llame al Centro de Salud más cercano")
                    elif exterior == 0:
                        zona_nac = int(input("¿En los últimos 14 días estuvo en zonas nacionales con casos confirmados?, \n1-Si\n0-No\n- "))
                        if zona_nac == 1:
                            print("\tADVERTENCIA !")
                            print("CASO AUTOCTONO SOSPECHOSO: Llame al Centro de Salud más cercano")   #Caso autoctono
                        elif zona_nac == 0:
                            print("Usted presenta fiebre y síntomas respiratorios, pero al no haber" \
                                                                             " estado en contacto con población de riesgo, recomendamos" \
                                                                             " quedarse en su casa e ir evaluando la situación." \
                                                                             "\n En caso de dudas, consulte a su médico.")
