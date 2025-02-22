import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parámetros
a, b, c = 2, -3, 1
x = np.linspace(-10, 10, 400)

# Funciones
def logaritmica(x, a, b, c):
    return a * np.log(b * x + c)

# Graficar función logarítmica
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.125, bottom=0.25)
line, = ax.plot(x, logaritmica(x, a, b, c), label='Función Logarítmica', color='purple')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
ax.set_title("Función Logarítmica")
ax.set_xlabel('x')
ax.set_ylabel('y')

# Ajustar límites de los ejes para centrar la gráfica
ax.set_xlim(-10, 10)
ax.set_ylim(min(logaritmica(x, a, b, c)) - 10, max(logaritmica(x, a, b, c)) + 10)

# Ajustar espacio para slider
axcolor = 'lightgoldenrodyellow'
axa = plt.axes([0.125, 0.15, 0.775, 0.03], facecolor=axcolor)
axb = plt.axes([0.125, 0.125, 0.775, 0.03], facecolor=axcolor)
axc = plt.axes([0.125, 0.10, 0.775, 0.03], facecolor=axcolor)

a_slider = Slider(
    ax=axa,
    label='a',
    valmin=-10,
    valmax=10,
    valinit=a,
    facecolor='purple'
)

b_slider = Slider(
    ax=axb,
    label='b',
    valmin=-10,
    valmax=10,
    valinit=b,
    facecolor='purple'
)

c_slider = Slider(
    ax=axc,
    label='c',
    valmin=-10,
    valmax=10,
    valinit=c,
    facecolor='purple'
)

# Función de actualización para sliders
def update(val):
    a = a_slider.val
    b = b_slider.val
    c = c_slider.val
    line.set_ydata(logaritmica(x, a, b, c))
    fig.canvas.draw_idle()

a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)

plt.show()