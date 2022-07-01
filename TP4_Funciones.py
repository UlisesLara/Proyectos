def buscar_campeon(v):
    n = len(v)
    may = 0
    m = []
    for i in range(n):
        if may < v[i].campeonatos:
            may = v[i].campeonatos
            m = [v[i]]
        elif may == v[i].campeonatos:
            m.append(v[i])
    return m


def mostrar_campeones_x_conf(v):
    conf = [0] * 6
    for i in range(len(v)):
        if v[i].campeonatos != 0:
            conf[v[i].confederacion] += 1
    return conf


def validate_range(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Se pidió entre", inf, "y", sup, ". Cargue otra vez: ")
    return n


def buscar_pais(v, mensaje):
    n = len(v)
    pais = input(mensaje)
    for i in range(n):
        if v[i].nombre == pais:
            return i
    return -1


def crear_vector_nuevo(v, cod):
    vn = []
    for i in range(len(v)):
        if v[i].confederacion == cod:
            nom = v[i].nombre
            pts = v[i].puntos
            camp = v[i].campeonatos
            nuevo = Competidores_nuevo(nom, pts, camp)
            vn.append(nuevo)
    return vn


def crear_archivo(v, fd):
    m = open(fd, 'wb')
    for reg in v:
        pickle.dump(reg, m)
    m.close


def leer_archivo(fd, op):
    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    c = 0
    print(50 * "-")
    print("Leyendo archivo ", fd, "...")
    print(50 * "-")
    while m.tell() < t:
        vec = pickle.load(m)
        if op == 4:
            c += 1
        elif op == 5:
            mostrar_archivo(vec)
    return c
    m.close


def mostrar_archivo(registro):
    r = ""
    r += "{:<40}".format("Nombre: " + str(registro.nombre))
    r += "{:<15}".format("| Puntos: " + str(registro.puntos))
    r += "{:<15}".format("| Campeonatos ganados: " + str(registro.campeonatos))
    print()
    print(r)


def validar_paises(matriz, a):
    esta = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if a == matriz[i][j]:
                esta = True
                return esta
    return esta


def crear_matriz():
    n = 4
    m = 8
    matriz =[[0] * m for filas in range(n)]
    return matriz


def cargar_matriz(v, matriz):
    n = 4
    m = 8
    pais = -1
    esta = True
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                while pais == -1:
                    pais = buscar_pais(v, "Ingresar anfitrion: ")
                matriz[i][j] = v[pais].nombre
            elif i == 0 and j != 0:
                while esta:
                    cs = random.randint(0, 7)
                    pais = v[cs].nombre
                    esta = validar_paises(matriz, pais)
                    matriz[i][j] = pais
                esta = True
            else:
                while esta:
                    cs = random.randint(0, 31)
                    pais = v[cs].nombre
                    esta = validar_paises(matriz, pais)
                    matriz[i][j] = pais
                esta = True


def mostrar_matriz(matriz):
    print("Fixture:")
    print("Grupo A".center(15, "-"), "Grupo B".center(15, "-"), "Grupo C".center(15, "-"), "Grupo D".center(15, "-"),
          "Grupo E".center(15, "-"), "Grupo F".center(15, "-"), "Grupo G".center(15, "-"), "Grupo H".center(15, "-"), )
    b = ""
    for i in range(4):
        for j in range(8):
            b += str(matriz[i][j]).center(15, " ")
        print(b)
        b = ""


def buscar_en_fixture(matriz):
    n = len(matriz)
    m = len(matriz[0])
    nom = input("Ingresar nombre de país a buscar: ")
    esta = False
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == nom:
                if j == 0:
                    print(matriz[i][j], "Pertenece al grupo A")
                    esta = True
                    break
                if j == 1:
                    print(matriz[i][j], "Pertenece al grupo B")
                    esta = True
                    break
                if j == 2:
                    print(matriz[i][j], "Pertenece al grupo C")
                    esta = True
                    break
                if j == 3:
                    print(matriz[i][j], "Pertenece al grupo D")
                    esta = True
                    break
                if j == 4:
                    print(matriz[i][j], "Pertenece al grupo E")
                    esta = True
                    break
                if j == 5:
                    print(matriz[i][j], "Pertenece al grupo F")
                    esta = True
                    break
                if j == 6:
                    print(matriz[i][j], "Pertenece al grupo G")
                    esta = True
                    break
                if j == 7:
                    print(matriz[i][j], "Pertenece al grupo H")
                    esta = True
                    break
    if not esta:
        print(nom, "No participa en la competicion(O no existe).")
