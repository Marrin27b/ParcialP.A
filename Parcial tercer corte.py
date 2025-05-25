# Variables globales
filas = 8
columnas = 8
mapa = [[' ' for _ in range(columnas)] for _ in range(filas)]
vehiculos = {}
ocupados = {}
tarifa_minuto = 100  # Puedes cambiar esta tarifa

def generar_mapa():
    # Marcar entrada y salida
    mapa[0][0] = 'E'  # Entrada
    mapa[filas - 1][columnas - 1] = 'S'  # Salida

    # Crear vías horizontales y verticales
    for i in range(filas):
        mapa[i][1] = 'V'  # Vía vertical cerca a la entrada

    for j in range(2, columnas - 1):
        mapa[2][j] = 'V'  # Vía horizontal en la tercera fila

    # Espacios de parqueo (accesibles desde la vía horizontal)
    for i in range(3, filas - 1):
        for j in range(2, columnas - 1):
            mapa[i][j] = 'P'

def mostrar_mapa():
    print("\nMapa del Parqueadero:")
    for fila in mapa:
        print(' '.join(fila))
    print()

def mostrar_disponibilidad():
    libres = sum(f.count('P') for f in mapa)
    ocupados_count = sum(f.count('X') for f in mapa)
    print(f"Espacios libres: {libres}")
    print(f"Espacios ocupados: {ocupados_count}")

def buscar_espacio_libre():
    for i in range(3, filas - 1):
        for j in range(2, columnas - 1):
            if mapa[i][j] == 'P':
                return (i, j)
    return None

def ingresar_vehiculo(placa):
    if placa in vehiculos:
        print("Este vehículo ya está registrado.")
        return
    posicion = buscar_espacio_libre()
    if posicion:
        i, j = posicion
        mapa[i][j] = 'X'
        vehiculos[placa] = 0  # Guardar un valor de entrada ficticio
        ocupados[placa] = (i, j)
        print(f"Vehículo con placa {placa} ingresó al parqueadero.")
    else:
        print("No hay espacios disponibles.")

def sacar_vehiculo(placa):
    if placa not in vehiculos:
        print("Vehículo no encontrado.")
        return
    # Aquí puedes calcular el tiempo de permanencia de otra manera si es necesario
    print("Funcionalidad de cálculo de tiempo no disponible sin datetime.")
    # Liberar espacio
    i, j = ocupados[placa]
    mapa[i][j] = 'P'
    del vehiculos[placa]
    del ocupados[placa]

# Menú interactivo
def menu():
    generar_mapa()
    while True:
        print("\n--- MENÚ PARQUEADERO ---")
        print("1. Ingresar vehículo")
        print("2. Sacar vehículo")
        print("3. Mostrar mapa")
        print("4. Mostrar disponibilidad")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            placa = input("Ingrese la placa del vehículo: ")
            ingresar_vehiculo(placa)
        elif opcion == '2':
            placa = input("Ingrese la placa del vehículo: ")
            sacar_vehiculo(placa)
        elif opcion == '3':
            mostrar_mapa()
        elif opcion == '4':
            mostrar_disponibilidad()
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:

            print("Opción inválida.")

# Ejecutar menú
if __name__ == "__main__":
    menu()
