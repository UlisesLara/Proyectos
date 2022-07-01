from TP4_Funciones import*


def principal():
    print("\tSistema de Gestión de una Competencia Mundial")
    op = -1
    v = generar_arreglo()
    matriz = 0
    while op != 8:
        mostrar_menu()
        op = int(input("\t\tIngrese una opcion: "))
        if op > 8 or op < 1:
            print("Opcion invalida.")
        elif op == 1:
            mostrar_registro(v)
        elif op == 2:
            may = buscar_campeon(v)
            mostrar_registro(may)
        elif op == 3:
            conf = mostrar_campeones_x_conf(v)
            print(conf)
            print("UEFA tiene", conf[0], "pais(es) campeon(es).")
            print("CONMEBOL tiene", conf[1], "pais(es) campeon(es).")
            print("CONCACAF tiene", conf[2], "pais(es) campeon(es).")
            print("CAF tiene", conf[3], "pais(es) campeon(es).")
            print("AFC tiene", conf[4], "pais(es) campeon(es).")
            print("OFC tiene", conf[5], "pais(es) campeon(es).")
        elif op == 4:
            print("0: UEFA, 1: CONMEBOL, 2: CONCACAF, 3: CAF, 4: AFC, 5: OFC")
            cod = validate_range(0, 5, "Ingrese codigo entre 0 y 5: ")
            vn = crear_vector_nuevo(v, cod)
            fd = "clasificacion" + str(cod) + ".dat"
            crear_archivo(vn, fd)
            cant = leer_archivo(fd, op)
            print("El archivo ", fd, "tiene cargados ", cant, "registros.")
        elif op == 5:
            print("0: UEFA, 1: CONMEBOL, 2: CONCACAF, 3: CAF, 4: AFC, 5: OFC")
            cod = validate_range(0, 5, "Ingrese codigo para buscar su archivo (entre 0 y 5): ")
            fd = "clasificacion" + str(cod) + ".dat"
            if not os.path.exists(fd):
                ar = input("El archivo solicitado no existe. Presione enter para crearlo :")
                vn = crear_vector_nuevo(v, cod)
                crear_archivo(vn, fd)
                print("Archivo creado con exito!")
                print("Seleccione nuevamente la opcion 5 para mostrarlo.")
            else:
                leer_archivo(fd, op)
        elif op == 6:
            matriz = crear_matriz()
            cargar_matriz(v, matriz)
            mostrar_matriz(matriz)
        elif op == 7:
            if matriz == 0:
                print("La matriz no existe. Elija la opcion 6 para crearla.")
            else:
                buscar_en_fixture(matriz)


if __name__ == "__main__":
    principal()
