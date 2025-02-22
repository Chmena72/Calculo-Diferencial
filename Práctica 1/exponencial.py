import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parámetros iniciales
a, b, c = 2, -3, 1
x = np.linspace(-10, 10, 400)

# Función exponencial
def exponencial(x, a, b, c):
    return a * np.exp(b * x) + c

# Graficar la función exponencial
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.15, bottom=0.3)
line, = ax.plot(x, exponencial(x, a, b, c), label='Función Exponencial', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(loc='upper left')
ax.set_title("Función Exponencial")
ax.set_xlabel('x')
ax.set_ylabel('y')

# Ajustar límites de los ejes para centrar la gráfica
ax.set_xlim(-10, 10)
ax.set_ylim(min(exponencial(x, a, b, c)) - 10, max(exponencial(x, a, b, c)) + 10)

# Ajustar espacio para sliders
axcolor = 'lightgoldenrodyellow'
axa = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)
axb = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
axc = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)

# Creación de sliders
a_slider = Slider(axa, 'a', -10, 10, valinit=a, facecolor='blue')
b_slider = Slider(axb, 'b', -10, 10, valinit=b, facecolor='blue')
c_slider = Slider(axc, 'c', -10, 10, valinit=c, facecolor='blue')

# Función de actualización para sliders
def update(val):
    a = a_slider.val
    b = b_slider.val
    c = c_slider.val
    line.set_ydata(exponencial(x, a, b, c))
    ax.set_ylim(min(exponencial(x, a, b, c)) - 10, max(exponencial(x, a, b, c)) + 10)
    fig.canvas.draw_idle()

a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)

plt.show()