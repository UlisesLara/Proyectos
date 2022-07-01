import random

class participantes:        # Registro
    def __init__(self, nom, con, ran, pun, pos):
        self.nombre = nom
        self.continente = con
        self.ranking = ran
        self.puntaje = pun
        self.posicion = pos


def carga(v):       # Cargamos todos los datos necesarios aleatoriamente
    america = ("Abigail", "Abril", "Agustina", "Alaia", "Alana", "Adrián", "Agustín", "Alberto", "Alejandro",
               "Alexander", "Noah", "Emma", "Jacob", "Sophia", "Mason", "Olivia", "Liam", "Isabella", "William", "Ava")
    europa = ("Antonio", "Jose", "Manuel", "Francisco", "David", "Juan", "Carlos", "Jesus", "Alejandro", "Miguel",
              "Maria", "Carmen", "Josefa", "Ana", "Isabel", "Laura", "Cristina", "Francisca", "Antonia", "Lucia")
    asia = ("Sakura", "Mizuki", "Mei", "Misuki", "Kokoro", "Cho", "Eiko", "Kumiko", "Mana", "Yoko", "Hikari", "Ryu",
            "Akira", "Kai", "Yuki", "Nozomi", "Aoi", "Kaoru", "Tsubasa", "Tora")
    africa = ("Achebe", "Aidah", "Alika", "Ashanti", "Finnley", "Gasira", "Jetta", "Johari", "Latoya", "Leiza",
              "Mbwana", "Nala", "Sade", "Siara", "Aba", "Abu", "Abdul", "Amiri", "Badou", "Bakari")
    oceania = ("William", "Isabella", "Jack", "Ruby", "Oliver", "Chloe", "Joshua", "Olivia", "Thomas", "Charlotte",
               "Lachlan", "Mia", "Cooper", "Lily", "Noah", "Emily", "Ethan", "Ella", "Lucas", "Sienna")
    for i in range(len(v)):
        con = random.randint(0, 4)
        if con == 0:
            nom = random.choice(america)
        elif con == 1:
            nom = random.choice(europa)
        elif con == 2:
            nom = random.choice(asia)
        elif con == 3:
            nom = random.choice(africa)
        elif con == 4:
            nom = random.choice(oceania)
        ran = random.randint(1, 100)
        pun = 0
        pos = None
        v[i] = participantes(nom, con, ran, pun, pos)


def contador(v):        # Contador de participantes por continente
    cont_am = cont_eu = cont_as = cont_af = cont_oc = 0

    for i in range(len(v)):
        if v[i].continente == 0:
            cont_am += 1
        elif v[i].continente == 1:
            cont_eu += 1
        elif v[i].continente == 2:
            cont_as += 1
        elif v[i].continente == 3:
            cont_af += 1
        elif v[i].continente == 4:
            cont_oc += 1
    print("America :", cont_am)
    print("Europa :", cont_eu)
    print("Asia :", cont_as)
    print("Africa :", cont_af)
    print("Oceania :", cont_oc)


def contar_continentes(v, c):
    n = len(v)
    m = len(c)
    for i in range(n):
        for j in range(m):
            if v[i].continente == j:
                c[j] += 1


def ordenxranking(v):           # Ordenamos los participantes segun su ranking
    for i in range(len(v)-1):
        for j in range(i+1, len(v)):
            if v[i].ranking > v[j].ranking:
                v[i], v[j] = v[j], v[i]


def simulacion(n, l, x, y):   # Funcion utilizada para simular las rondas de eliminacion
    for i in range(x):
        if i == y:
            break
        n[i].puntaje = random.randint(100, 1000)
        n[-i-1].puntaje = random.randint(100, 1000)
        if n[i].puntaje > n[-i-1].puntaje:
            l[i] = n[i]
        elif n[i].puntaje < n[-i-1].puntaje:
            l[i] = n[-i-1]
        print("-" * 60)
        print("Participante 1:\t  Participante 2:")
        print("Nombre :", n[i].nombre, "\t Nombre :", n[-i-1].nombre)
        print("Puntaje :", n[i].puntaje, "\t Puntaje :", n[-i-1].puntaje)
        print("Ranking :", n[i].ranking, "\t Ranking :", n[-i-1].ranking)
        print("Continente :", n[i].continente, "\t Continente :", n[-i-1].continente)
        print("-" * 60)
        if n[i].puntaje > n[-i - 1].puntaje:
            print("PASA :", n[i].nombre)
        elif n[i].puntaje < n[-i - 1].puntaje:
            print("PASA :", n[-i-1].nombre)


def simulacion_semis(semis, final, tercer):         # Simulamos semifinales y asignamos a los perdedores a las
    for i in range(4):                              # rondas de tercer-cuarto puesto y a la final
        if i == 2:
            break
        semis[i].puntaje = random.randint(100, 1000)
        semis[-i-1].puntaje = random.randint(100, 1000)
        if semis[i].puntaje > semis[-i-1].puntaje:
            final[i] = semis[i]
            tercer[i] = semis[-i-1]
        elif semis[i].puntaje < semis[-i-1].puntaje:
            final[i] = semis[-i-1]
            tercer[i] = semis[i]
        print("-" * 60)
        print("Participante 1:\t  Participante 2:")
        print("Nombre :", semis[i].nombre, "\t Nombre :", semis[-i-1].nombre)
        print("Puntaje :", semis[i].puntaje, "\t Puntaje :", semis[-i-1].puntaje)
        print("Ranking :", semis[i].ranking, "\t Ranking :", semis[-i-1].ranking)
        print("Continente :", semis[i].continente, "\t Continente :", semis[-i-1].continente)
        print("-" * 60)
        if semis[i].puntaje > semis[-i - 1].puntaje:
            print("PASA :", semis[i].nombre)
        elif semis[i].puntaje < semis[-i - 1].puntaje:
            print("PASA :", semis[-i-1].nombre)


def generar_podio(final, podio):        # Se genera el podio segun los ganadores para actualizar el ranking
    for i in range(2):
        if i == 1:
            break
        if final[i].puntaje > final[-i-1].puntaje:
            final[i].posicion = 1
            final[-i-1].posicion = 2
            podio[0].posicion = 3
            podio[1] = final[-i-1]
            podio[2] = final[i]
        elif final[i].puntaje < final[-i-1].puntaje:
            final[-i-1].posicion = 1
            final[i].posicion = 2
            podio[0].posicion = 3
            podio[1] = final[i]
            podio[2] = final[-i-1]


def mostrar_podio(final, podio):       # Mostramos el podio
    for i in range(2):
        if i == 1:
            break
        if final[i].puntaje > final[-i-1].puntaje:
            print("Campeon :", final[0].nombre, "\n\tPuntaje :", final[0].puntaje, "\n\tRanking :", final[0].ranking,
                  "\n\tContinente :", final[0].continente)
            print("Segundo Puesto :", final[1].nombre, "\n\tPuntaje :", final[1].puntaje, "\n\tRanking :",
                  final[1].ranking,
                  "\n\tContinente :", final[1].continente)
        elif final[i].puntaje < final[-i - 1].puntaje:
            print("Campeon :", final[1].nombre, "\n\tPuntaje :", final[1].puntaje, "\n\tRanking :", final[1].ranking,
                  "\n\tContinente :", final[1].continente)
            print("Segundo Puesto :", final[0].nombre, "\n\tPuntaje :", final[0].puntaje, "\n\tRanking :",
                  final[0].ranking,
                  "\n\tContinente :", final[0].continente)
    print("Tercer Puesto :", podio[0].nombre, "\n\tPuntaje :", podio[0].puntaje, "\n\tRanking :", podio[0].ranking,
          "\n\tContinente :", podio[0].continente)


def promedios(v, n, l):         # Funcion para promediar los puntajes de las rondas
    puntajes = 0
    for i in range(n):
        if i == l:
            break
        puntajes += v[i].puntaje + v[-i - 1].puntaje
    prom_puntuacion = puntajes / n
    prom_puntuacion = round(prom_puntuacion, 2)
    print("Promedio de puntuacion en la ronda seleccionada: ", prom_puntuacion)


def actualizar_ranking(num, x):        # Funcion para actualizar el ranking viejo
    n = len(num)
    f = len(x)
    for i in range(n):
        for j in range(f):
            if x[j].nombre == num[i].nombre and x[j].ranking == num[i].ranking and x[j].continente == num[i].continente:
                if x[j].posicion == 1:
                    num[i].ranking -= 25
                    if num[i].ranking < 1:
                        num[i].ranking = 1
                if x[j].posicion == 2:
                    num[i].ranking -= 15
                    if num[i].ranking < 1:
                        num[i].ranking = 1
                if x[j].posicion == 3:
                    num[i].ranking -= 5
                    if num[i].ranking < 1:
                        num[i].ranking = 1


def menu():         # Printeo del menu de inicio
    print("-" * 60)
    print("1- Cantidad de participantes por continente. ")
    print("2- Puntaje promedio por participante en octavos. ")
    print("3- Puntaje promedio por participante en cuartos. ")
    print("4- Puntaje promedio por participante en semifinal. ")
    print("5- Mostrar el podio.")
    print("6- Mostrar el vector de participantes ordenado por ranking.")
    print("7- Salir.")
    print("-" * 60)
