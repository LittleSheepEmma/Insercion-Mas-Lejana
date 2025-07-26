# Inserción Más Lejana - Visualización de Rutas

Este proyecto implementa el algoritmo de Inserción Más Lejana para encontrar una ruta eficiente entre clientes (por ejemplo, para el problema del viajante de comercio) y visualiza tanto la ruta como los resultados computados en una interfaz gráfica con pestañas.

## Características

- Lee coordenadas de clientes desde un archivo `Datos.txt` (42 líneas, 21 clientes, cada cliente en dos líneas: X y Y).
- Calcula la matriz de distancias entre todos los clientes.
- Aplica el algoritmo de Inserción Más Lejana para construir la ruta (puedes adaptar la lógica en el script).
- Visualiza la ruta en un plano cartesiano (matplotlib) y la tabla de resultados (orden de visita, coordenadas y costo total) en una sola ventana con pestañas (Tkinter).

## Requisitos

- Python 3.x
- numpy
- matplotlib
- tkinter (incluido en la mayoría de instalaciones de Python)

Instala las dependencias con:

```
pip install numpy matplotlib
```

## Uso

1. Prepara un archivo `Datos.txt` en el mismo directorio, con 42 líneas: cada par de líneas representa las coordenadas X e Y de un cliente.
2. Ejecuta el script:

```
python InsercionMasLejana.py
```

3. Se abrirá una ventana con dos pestañas:
   - **Gráfica de Ruta**: muestra el recorrido óptimo entre los clientes.
   - **Tabla de Resultados**: muestra el orden de visita, las coordenadas de cada cliente y el costo total de la ruta.

## Notas

- No se imprime nada en consola; toda la información relevante se muestra en la interfaz gráfica.
- Puedes alternar entre la gráfica y la tabla usando las pestañas.
- El algoritmo y la visualización están pensados para 21 clientes, pero puedes adaptar el código para más.
- La lógica de la ruta puede ser modificada para implementar la inserción más lejana real.
