import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parámetros
a, b, c, e = 2, -3, 1, 0
x = np.linspace(-10, 10, 400)

# Función
def raiz(x, a, b, c, e):
    return a * np.sqrt(b * x - c) + e

# Graficar la función
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.125, bottom=0.25)
line, = ax.plot(x, raiz(x, a, b, c, e), label='Función Raíz', color='red')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
ax.set_title("Función Raíz")
ax.set_xlabel('x')
ax.set_ylabel('y')

# Ajustar límites de los ejes para centrar la gráfica
ax.set_xlim(-10, 10)
ax.set_ylim(min(raiz(x, a, b, c, e)) - 10, max(raiz(x, a, b, c, e)) + 10)

# Ajustar espacio para sliders
axcolor = 'lightgoldenrodyellow'
axa = plt.axes([0.125, 0.15, 0.775, 0.03], facecolor=axcolor)
axb = plt.axes([0.125, 0.125, 0.775, 0.03], facecolor=axcolor)
axc = plt.axes([0.125, 0.10, 0.775, 0.03], facecolor=axcolor)
axe = plt.axes([0.125, 0.075, 0.775, 0.03], facecolor=axcolor)

# Sliders para ajustar los coeficientes a, b, c y e
a_slider = Slider(
    ax=axa,
    label='a',
    valmin=-10,
    valmax=10,
    valinit=a,
    facecolor='red'
)

b_slider = Slider(
    ax=axb,
    label='b',
    valmin=-10,
    valmax=10,
    valinit=b,
    facecolor='red'
)

c_slider = Slider(
    ax=axc,
    label='c',
    valmin=-10,
    valmax=10,
    valinit=c,
    facecolor='red'
)

e_slider = Slider(
    ax=axe,
    label='e',
    valmin=-10,
    valmax=10,
    valinit=e,
    facecolor='red'
)

# Función que se ejecuta cuando se cambian los sliders
def update(val):
    a = a_slider.val
    b = b_slider.val
    c = c_slider.val
    e = e_slider.val
    line.set_ydata(raiz(x, a, b, c, e))
    ax.set_ylim(min(raiz(x, a, b, c, e)) - 10, max(raiz(x, a, b, c, e)) + 10)  # Ajusta los límites de y
    fig.canvas.draw_idle()

a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)
e_slider.on_changed(update)

plt.show()