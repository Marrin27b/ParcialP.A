## Proyecto: Simulador de Combate Pokémon – C++

##  Integrantes del equipo
- Martin Samuel Monsalve Sánchez  
- David Santiago Trujillo  

---

## Descripción General

Este proyecto simula una batalla por turnos entre Pokémon, inspirada en los combates clásicos del universo Pokémon. Los jugadores pueden elegir entre 18 Pokémon con habilidades únicas y usar ataques estratégicos para vencer a su oponente.

El combate se puede jugar en dos modos:
- Jugador vs. Bot
- Jugador vs. Jugador

---

##  Funcionalidades Implementadas

### 1. Selección de Pokémon

**¿Para qué se implementó?**  
Permite a los jugadores elegir su Pokémon favorito entre una variedad de 18 opciones, cada uno con tipos y ataques únicos.

**¿Cómo se llevó a cabo su implementación?**  
- Se creó la función `crearPokemones()` que genera un vector de objetos `Pokemon`.
- Se implementó `elegirPokemonJugador()` para mostrar la lista y registrar la selección del usuario.

---

### 2. ⚔️ Sistema de Ataques

**¿Para qué se implementó?**  
Simula las habilidades ofensivas de los Pokémon durante el combate.

**¿Por qué se consideró necesario?**  
Es fundamental para representar la mecánica del juego y tomar decisiones tácticas.

**¿Cómo se llevó a cabo su implementación?**  
- Cada Pokémon tiene cuatro ataques representados como objetos `Ataque`, con nombre y daño.
- El método `usarAtaque()` reduce la vida del oponente tras ejecutarse.

---

### 3.  Turnos de Combate

**¿Para qué se implementó?**  
Controla el orden de participación y mantiene el flujo del combate.

**¿Por qué se consideró necesario?**  
Es esencial para la dinámica de combate por turnos.

**¿Cómo se llevó a cabo su implementación?**  
- Se utiliza una variable booleana `turnoJugador1` para alternar entre jugadores.
- En modo bot, se usan valores aleatorios (`rand()`) para elegir ataques automáticamente.

---

### 4. Sistema de Vida y Estado del Combate

**¿Para qué se implementó?**  
Controla la salud de los Pokémon y determina cuándo termina el combate.

**¿Por qué se consideró necesario?**  
Permite identificar el momento en que un Pokémon es derrotado y declarar al ganador.

**¿Cómo se llevó a cabo su implementación?**  
- La función `recibirDaño()` reduce la vida del Pokémon atacado.
- La función `estaVivo()` verifica si un Pokémon sigue en combate.
- Al terminar el combate, se imprime el ganador en consola.

---

### 5.  Modos de Juego

**¿Para qué se implementó?**  
Ofrece flexibilidad al usuario para jugar solo o con otra persona.

**¿Por qué se consideró necesario?**  
Mejora la experiencia y rejugabilidad del sistema.

**¿Cómo se llevó a cabo su implementación?**  
- El menú principal permite elegir entre "1 jugador (vs bot)" o "2 jugadores".
- En el modo 1 jugador, el oponente se elige automáticamente y sus ataques son aleatorios.

---

##  Requisitos Mínimos Cubiertos
- [x] Lenguaje: C++
- [x] Sistema de combate por turnos
- [x] Menú textual de interacción
- [x] Mínimo dos ataques por Pokémon (cada uno tiene cuatro)
- [x] Finalización del combate al llegar a 0 puntos de vida
- [x] Anuncio de ganador


##  Posibles Mejoras Futuras
- Animaciones básicas en consola (ASCII Art).
- Tipos de Pokémon y sistema de efectividad.
- Guardado de estadísticas de combate.
- Modo torneo.

## Diagrama de flujo
![image](https://github.com/user-attachments/assets/22467719-2c4e-4de5-81df-9556cb6aa148)


