<img width="1440" alt="Captura de pantalla 2025-05-25 a la(s) 12 59 44 p m" src="https://github.com/user-attachments/assets/0ef9ea6c-24bb-4142-8b8f-051fbe67ff7c" /># ParcialP.A
# Proyecto de Sistema de Parqueadero
## Integrantes del equipo
- [Martin Samuel Monsalve Sánchez]
- [David Santiago Trujillo]

### Proyecto Parqueadero
# Proyecto: Parqueadero Inteligente

Este proyecto simula la gestión de un parqueadero mediante una representación en consola de un mapa, registro de vehículos y disponibilidad de espacios.

### 1. Mapa Interactivo del Parqueadero

**¿Para qué se implementó?**
Para ofrecer una visualización clara y estructurada del parqueadero, indicando entrada, salida, vías y espacios disponibles u ocupados.

**¿Cómo se llevó a cabo su implementación?**
Se utilizó una matriz de 8x8 donde:
- `'E'` indica la entrada.
- `'S'` indica la salida.
- `'V'` representa las vías.
- `'P'` los espacios disponibles.
- `'X'` los espacios ocupados.

### 2. Registro de vehículos y ocupación de espacios

**¿Para qué se implementó?**
Para controlar la entrada y salida de vehículos, registrando su presencia en el parqueadero.

**¿Por qué se consideró necesario?**
Permite la trazabilidad de los vehículos y asegura que no se duplique el ingreso ni queden espacios mal gestionados.

**¿Cómo se llevó a cabo su implementación?**
Mediante el uso de un diccionario `vehiculos` para registrar las placas y `ocupados` para asociar cada vehículo con su ubicación en el mapa.

### 3. Disponibilidad en tiempo real

**¿Para qué se implementó?**
Para que los usuarios puedan consultar en cualquier momento cuántos espacios hay libres u ocupados.

**¿Por qué se consideró necesario?**
Facilita la toma de decisiones al momento de ingresar un vehículo.

**¿Cómo se llevó a cabo su implementación?**
Con una función que recorre el mapa y cuenta cuántas posiciones están marcadas como `'P'` o `'X'`.

**Diagrama de flujo**
Inicio
  │
  ▼
Generar mapa inicial
  │
  ▼
+----------------------+
| Mostrar menú         |
| 1. Ingresar vehículo |
| 2. Sacar vehículo    |
| 3. Mostrar mapa      |
| 4. Mostrar disp.     |
| 5. Salir             |
+----------------------+
  │
  ▼
Leer opción del usuario
  │
  ├───► Opción 1? ─► Pedir placa
  │                 │
  │                 ▼
  │         ¿Vehículo ya registrado?
  │                 │
  │           ├── Sí ─► Mostrar mensaje
  │           │
  │           └── No ─► Buscar espacio libre
  │                         │
  │                 ├── Hay espacio ─► Marcar como ocupado
  │                 │                   Guardar datos vehículo
  │                 │                   Mostrar mensaje
  │                 └── No hay ─► Mostrar mensaje
  │
  ├───► Opción 2? ─► Pedir placa
  │                 │
  │         ¿Vehículo está registrado?
  │                 │
  │           ├── No ─► Mostrar error
  │           └── Sí ─► Liberar espacio
  │                       Eliminar del registro
  │                       Mostrar mensaje
  │
  ├───► Opción 3? ─► Mostrar mapa
  │
  ├───► Opción 4? ─► Calcular espacios
  │                 Mostrar disponibilidad
  │
  ├───► Opción 5? ─► Mostrar mensaje de salida
  │                 Terminar programa
  │
  └───► Otra opción ─► Mostrar error
  │
  ▼
Repetir menú




