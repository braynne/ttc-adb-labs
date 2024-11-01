## Escenario 1: Gráfico de Barras 2D en Diferentes Planos en 3D

Este ejercicio tiene como objetivo crear un gráfico 3D que proyecte gráficos de barras 2D en diferentes planos del espacio tridimensional. En este caso, se proyectan barras en los planos y=0, y=1, y=2, y y=3, lo que crea la ilusión de varios gráficos de barras organizados a lo largo de diferentes capas o planos.

`np.random.seed(19680801)`

#### Tener en cuenta:

- Visualizar gráficos de barras 2D en diferentes posiciones dentro de un espacio
tridimensional.

- Distribuir los gráficos de barras en diferentes planos en el eje y del gráfico,
mostrando cómo se comportan los datos a lo largo de este eje.

- Usar colores diferentes para cada conjunto de barras proyectadas, facilitando la
diferenciación entre los distintos planos.

- Crear una visualización en 3D que permita explorar la variación de las barras a lo
largo de un eje adicional (en este caso, el eje y)

### Código

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]

for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)

    cs = [c] * len(xs)
    cs[0] = 'c'

    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)
```

[Código completo del escenario 1](lab23_1.py)

### Conclusión

Este ejercicio busca visualizar gráficos de barras en un espacio tridimensional al proyectarlos en varios planos (en este caso, *y=0*, *y=1*, *y=2*, y *y=3*). Esto crea la apariencia de múltiples gráficos de barras en capas, cada uno organizado en un plano distinto, permitiendo comparar fácilmente los datos en diferentes "niveles" dentro del mismo espacio 3D.

[Laboratorio 23](../../lab23)
