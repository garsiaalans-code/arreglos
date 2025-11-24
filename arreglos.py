
nombres = []
artistas = []
duraciones = []
popularidades = []

def agregar_canciones():
    print("\n--- AGREGAR CANCIONES ---")
    try:
        cantidad = int(input("¿Cuántas canciones deseas agregar? "))
    except ValueError:
        print("Debes ingresar un número entero.")
        return
    
    for i in range(cantidad):
        print(f"\nCanción {i+1}:")
        nombre = input("Nombre: ")
        artista = input("Artista: ")
        while True:
            try:
                dur = float(input("Duración (minutos): "))
                break
            except ValueError:
                print(" Ingresa un número válido (float).")


        while True:
            try:
                pop = int(input("Popularidad (1 a 100): "))
                if 1 <= pop <= 100:
                    break
                else:
                    print(" Debe ser un número entre 1 y 100.")
            except ValueError:
                print(" Ingresa un número entero válido.")

    
        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(dur)
        popularidades.append(pop)

    print("\nCanciones agregadas exitosamente.\n")


def ver_reportes():
    print("\n--- REPORTES ---")

    if len(nombres) == 0:
        print(" No hay canciones registradas.")
        return

    total = len(nombres)
    dur_total = sum(duraciones)
    max_pop = max(popularidades)
    idx_max = popularidades.index(max_pop)

    
    min_pop = min(popularidades)
    idx_min = popularidades.index(min_pop)
    promedio = sum(popularidades) / total

    print(f" Número total de canciones: {total}")
    print(f" Duración total de la playlist: {dur_total:.2f} minutos")
    print(f" Canción más popular: {nombres[idx_max]} ({max_pop})")
    print(f" Canción menos popular: {nombres[idx_min]} ({min_pop})")
    print(f" Popularidad promedio: {promedio:.2f}")
def buscar_canciones():
    print("\n--- BUSCAR CANCIONES ---")
    
    if len(nombres) == 0:
        print(" No hay canciones registradas.")
        return

    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print(" Opción inválida.")
        return

    if opcion == 1:
        artista_buscar = input("\nIngresa el nombre del artista: ")
        print("\n--- RESULTADOS ---")

        encontrados = False
        for i in range(len(nombres)):
            if artistas[i].lower() == artista_buscar.lower():
                print(f"{nombres[i]} - {artistas[i]} (Pop: {popularidades[i]})")
                encontrados = True
        
        if not encontrados:
            print(" No se encontraron canciones de ese artista.")

    elif opcion == 2:
        try:
            min_p = int(input("Popularidad mínima: "))
            max_p = int(input("Popularidad máxima: "))
        except ValueError:
            print("Ingresa números válidos.")
            return

        print("\n--- RESULTADOS ---")
        encontrados = False
        for i in range(len(nombres)):
            if min_p <= popularidades[i] <= max_p:
                print(f" {nombres[i]} - {artistas[i]} (Pop: {popularidades[i]})")
                encontrados = True
        
        if not encontrados:
            print(" No hay canciones en ese rango de popularidad.")

    else:
        print(" Opción no válida.")
def playlist_recomendada():
    print("\n--- PLAYLIST RECOMENDADA ---")

    if len(nombres) == 0:
        print(" No hay canciones registradas.")
        return

    promedio = sum(popularidades) / len(popularidades)
    print(f" Popularidad promedio: {promedio:.2f}\n")

    recomendadas = False
    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print(f" {nombres[i]} - {artistas[i]} (Pop: {popularidades[i]})")
            recomendadas = True

    if not recomendadas:
        print(" Ninguna canción supera el promedio.")

def menu():
    while True:
        print("\n")
        print("FESTIVAL PLAYLIST")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        try:
            opcion = int(input("\nElige una opción: "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if opcion == 1:
            agregar_canciones()
        elif opcion == 2:
            ver_reportes()
        elif opcion == 3:
            buscar_canciones()
        elif opcion == 4:
            playlist_recomendada()
        elif opcion == 5:
            print("\n Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

menu()
