# Programación 1

Programas y ejercicios hechos en la materia de **Programación 1**, en Python.
Cada programa está en su propia carpeta.

## Contenido

- [Programas](#programas)
- [Requisitos](#requisitos)
- [Cómo ejecutar](#cómo-ejecutar)

## Programas

| Programa | Tema | Archivo |
|---|---|---|
| [blackjack](#blackjack) | Juegos | `BLACKJACK.py` |
| [butacas_cine](#butacas_cine) | Reservas | `butacasCine.py` |
| [cifrado_cesar](#cifrado_cesar) | Texto | `cifrado_cesar.py` |
| [contraseña_segura](#contraseña_segura) | Texto | `contraseña_segura.py` |
| [determinar_numero_dias_mes_1900_2026](#determinar_numero_dias_mes_1900_2026) | Fechas | `determinarNumeroDiasMes1900_2026.py` |
| [figuras_asteriscos](#figuras_asteriscos) | Matrices | 4 archivos |
| [juego_de_luces](#juego_de_luces) | Juegos | `juego_de_luces.py` |
| [matrices](#matrices) | Matrices | 2 archivos |
| [memorama_en_1d](#memorama_en_1d) | Juegos | `memorama_en_1d.py` |

### blackjack
Juego de Blackjack contra el crupier, que empieza con **$100** de capital.
Puedes apostar, pedir carta o plantarte, y el As vale 11 o 1 según convenga.

### butacas_cine
Sistema de reservas para una sala de **10 filas por 20 butacas**.
Permite reservar (con propuesta automática de lugares juntos), cancelar y ver la disponibilidad.

### cifrado_cesar
Pide un texto y un número de pasos, y desplaza cada letra esa cantidad de posiciones.
Respeta mayúsculas y minúsculas, y deja intactos los símbolos.

### contraseña_segura
Evalúa una contraseña: mínimo **10 caracteres**, mayúscula, minúscula, dígito y carácter especial.
Si falla, muestra qué requisitos le faltan.

### determinar_numero_dias_mes_1900_2026
Recibe año (mayor a 1582), mes y día, y dice qué **día de la semana** fue.
Usa una fórmula matemática para calcularlo.

### figuras_asteriscos
Dibuja figuras con asteriscos: una casa, un triángulo rectángulo y triángulos centrados.
Algunas usan matrices de numpy y la altura se pide al usuario.

### juego_de_luces
Hay **10 luces** en fila y elegir una cambia su estado y el de sus vecinas.
El objetivo es apagarlas todas en el menor número de movimientos.

### matrices
Dibuja un **reloj de arena** hueco de asteriscos a partir de una altura dada.
También calcula cuántos vecinos con valor 1 tiene cada celda de una matriz de 0 y 1.

### memorama_en_1d
Memorama con **5 parejas** de números boca abajo en una fila.
Eliges dos posiciones por turno hasta encontrar todas. Al final incluye ejemplos de operaciones de conjuntos (unión, intersección, complemento y diferencias).

## Requisitos

| Requisito | Uso |
|---|---|
| Python 3 | Lenguaje |
| `numpy` | Matrices y arreglos |
| `emoji` | Luces del juego de luces |
| `IPython` | Mostrar títulos en las figuras |

```bash
pip install numpy emoji ipython
```

## Cómo ejecutar

Entra a la carpeta del programa y ejecútalo:

```bash
cd blackjack
python BLACKJACK.py
```

Cada programa pide los datos por teclado, así que solo sigue las instrucciones en pantalla.
