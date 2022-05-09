from helpers import move_sympy_plot_to_axes
from sympy import pi, fourier_series, plot, Symbol
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = Symbol('x')
s = fourier_series(x, (x, -pi, pi))

fig, ax = plt.subplots(figsize=(10, 10))

fig.suptitle('Fourier series of $f(x) = x$\nFirst $n$ nonzero terms',
             fontsize=16)


def init_plot():
    ax.clear()
    p_x = plot(x, (x, -3, 3), show=False, label=r'$f(x) = x$')
    move_sympy_plot_to_axes(p_x, ax)
    return ax


def animate(n):
    ax.autoscale_view()
    fig.canvas.draw()

    if len(ax.lines) > 1:
        ax.lines.pop(-1)

    fourier = s.truncate(n)
    p_fourier = plot(fourier, (x, -3, 3), show=False,
                     label=f"Fourier - n = {n}")
    move_sympy_plot_to_axes(p_fourier, ax)
    ax.legend()

    return ax


def animation_fourier(frames=range(1, 16, 2), interval=150, save=False,
                      filename='animation.gif', fps=1/2):

    ani = animation.FuncAnimation(fig, animate, frames=frames,
                                  interval=interval,
                                  repeat_delay=150,
                                  init_func=init_plot,
                                  )

    if save:
        ani.save(filename, 'imagemagick', fps=fps)

    return ani


ani = animation_fourier()
# ani = animation_fourier(save=True)
plt.show()
