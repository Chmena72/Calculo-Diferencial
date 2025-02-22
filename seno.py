import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parámetros
a, b = 2, -3
x = np.linspace(-10, 10, 400)

# Función
def seno(x, a, b):
    return a * np.sin(b * x)

# Graficar función seno
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.125, bottom=0.25)
line, = ax.plot(x, seno(x, a, b), label='Función Seno', color='blue')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
ax.set_title("Función Seno")
ax.set_xlabel('x')
ax.set_ylabel('y')

#Ajustar límites de los ejes para centrar la gráfica
ax.set_xlim(-10, 10)
ax.set_ylim(min(seno(x, a, b)) - 10, max(seno(x, a, b)) + 10)

# Ajustar espacio para slider
axcolor = 'lightgoldenrodyellow'
axa = plt.axes([0.125, 0.15, 0.775, 0.03], facecolor=axcolor)
axb = plt.axes([0.125, 0.125, 0.775, 0.03], facecolor=axcolor)

a_slider = Slider(
    ax=axa,
    label='a',
    valmin=-10,
    valmax=10,
    valinit=a,
    facecolor='blue'
)

b_slider = Slider(
    ax=axb,
    label='b',
    valmin=-10,
    valmax=10,
    valinit=b,
    facecolor='blue',
    orientation='horizontal'
)   

# Función de actualización para sliders
def update(val):
    a = a_slider.val
    b = b_slider.val
    line.set_ydata(seno(x, a, b))
    fig.canvas.draw_idle()

a_slider.on_changed(update)
b_slider.on_changed(update)

plt.show()