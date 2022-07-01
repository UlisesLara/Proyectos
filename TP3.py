__author__ = 'Agustin_Margaria,Lucas_Vallinotti,Ulises_Lara'
from TP3_modulos import*


def test():
    v, cuartos, semis, final, tercer, podio, primero, continentes = [0] * 16, [0] * 8, [0] * 4, [0] * 2, [0] * 2, \
                                                                    [0] * 3, [0] * 1, [0] * 5
    carga(v)
    opcion = -1
    ordenxranking(v)
    contar_continentes(v, continentes)

    print("-" * 60, "OCTAVOS", "-" * 60)
    simulacion(v, cuartos, 16, 8)
    print("-" * 60, "CUARTOS", "-" * 60)
    simulacion(cuartos, semis, 8, 4)
    print("-" * 60, "SEMIS", "-" * 60)
    simulacion_semis(semis, final, tercer)
    print("-" * 60, "TERCER PUESTO", "-" * 60)
    simulacion(tercer, podio, 2, 1)
    print("-" * 60, "FINAL", "-" * 60)
    simulacion(final, primero, 2, 1)
    generar_podio(final, podio)

    while opcion != 7:
        menu()
        opcion = int(input("Escriba una opcion: "))
        if opcion == 1:
            print("Participantes por Continentes :")
            print(continentes)
            contador(v)
        if opcion == 2:
            promedios(v, 16, 8)

        if opcion == 3:
            promedios(cuartos, 8, 4)

        if opcion == 4:
            promedios(semis, 4, 2)

        if opcion == 5:
            mostrar_podio(final, podio)

        if opcion == 6:         # Mostramos el vector original ordenado por ranking y el actualizado
            print("-" * 60)
            print("\n\t\t\t\t\tRANKING VIEJO\n")
            print("-" * 60)
            for i in range(len(v)):
                print("Nombre :", v[i].nombre)
                print("Ranking :", v[i].ranking)
                print("Continente :", v[i].continente)
                print("-" * 60)
            actualizar_ranking(v, podio)
            ordenxranking(v)
            print("\n\t\t\t\t\tRANKING NUEVO\n")
            print("-" * 60)
            for i in range(len(v)):
                print("Nombre :", v[i].nombre)
                print("Ranking :", v[i].ranking)
                print("Continente :", v[i].continente)
                print("-" * 60)


if __name__ == "__main__":
    test()
