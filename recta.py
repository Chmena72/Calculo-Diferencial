import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parámetros iniciales
a, b, c = 2, -3, 1
x = np.linspace(-10, 10, 400)

# Función lineal
def lineal(x, pendiente, b):
    return pendiente * x + b

# Graficar función lineal
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.125, bottom=0.25)
line, = ax.plot(x, lineal(x, b, c), label='Función Lineal', color='indigo')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
ax.set_title("Función Lineal")
ax.set_xlabel('x')
ax.set_ylabel('y')

#Ajustar límites de los ejes para centrar la gráfica
ax.set_xlim(-10, 10)
ax.set_ylim(min(lineal(x, b, c)) - 10, max(lineal(x, b, c)) + 10)

# Ajustar espacio para sliders
axcolor = 'lightgoldenrodyellow'
axpendiente = plt.axes([0.125, 0.15, 0.775, 0.03], facecolor=axcolor)
axb = plt.axes([0.125, 0.125, 0.775, 0.03], facecolor=axcolor)

# Sliders para ajustar la pendiente y el intercepto
pendiente_slider = Slider(
    ax=axpendiente,
    label='Pendiente',
    valmin=-10,
    valmax=10,
    valinit=b,
    facecolor='indigo'
)

b_slider = Slider(
    ax=axb,
    label='B',
    valmin=-10,
    valmax=10,
    valinit=c,
    facecolor='indigo'
)

# Función que se ejecuta cuando se cambian los sliders
def update(val):
    pendiente = pendiente_slider.val
    b = b_slider.val
    line.set_ydata(lineal(x, pendiente, b))
    fig.canvas.draw_idle()

pendiente_slider.on_changed(update)
b_slider.on_changed(update)

plt.show()