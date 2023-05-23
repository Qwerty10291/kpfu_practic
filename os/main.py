from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import scipy.integrate as integr
import math
import numpy as np
import tkinter as tk

def erf_tailor(x, e):
    n = 0
    res = 0
    term = x
    while abs(term) >= e:
        res += term
        n += 1
        term = (-1) ** n * ( (x ** (2 * n + 1)) / (math.factorial(n) * (2 * n + 1)) )
    return 2 / math.sqrt(math.pi) * res

def erf_dt(t):
    return 2 / math.sqrt(math.pi) * math.exp(-t ** 2)

def create_graph(row, col):
    fig = Figure(figsize=(5,4), dpi=100)
    ax = fig.add_subplot(111)
    chart_type = FigureCanvasTkAgg(fig, root)
    chart_type.get_tk_widget().grid(row=row, column=col, columnspan=2, sticky='n', padx=10)
    return ax, chart_type

def plot_all():
    try:
        a = float(inp_a.get())
        b = float(inp_b.get())
        h = float(inp_h.get())
        eps = float(inp_eps.get())
    except:
        return
    if a > b:
        return
    if h > ((b - a) / 2):
        return

    interval = np.arange(a, b, h)
    fx_tail = np.array([erf_tailor(x, eps) for x in interval])
    fx_int = np.array([integr.quad(erf_dt, a, x, epsabs=eps)[0] for x in interval])
    sub = np.abs(fx_int - fx_tail)
    
    plt_tail.clear()
    plt_tail.set_title("Тейлор")
    plt_tail.plot(interval, fx_tail)
    wid_tail.draw()

    plt_int.clear()
    plt_int.set_title("Интеграл")
    plt_int.plot(interval, fx_int)
    wid_int.draw()
    
    plt_sub.clear()
    plt_sub.set_title("Разность")
    plt_sub.plot(interval, sub)
    wid_sub.draw()



root = tk.Tk()


tk.Label(text="a").grid(row=0, column=0)
inp_a = tk.Entry()
inp_a.grid(row=1, column=0)
tk.Label(text="b").grid(row=0, column=1)
inp_b = tk.Entry()
inp_b.grid(row=1, column=1)
tk.Label(text="h").grid(row=0, column=2)
inp_h = tk.Entry()
inp_h.grid(row=1, column=2)
tk.Label(text="eps").grid(row=0, column=3)
inp_eps = tk.Entry()
inp_eps.grid(row=1, column=3)
tk.Button(text="plot", command=plot_all).grid(row=2, column=0, columnspan=4, pady=6, ipadx=100)

plt_tail, wid_tail = create_graph(3, 0)
plt_tail.set_title("Тейлор")
plt_int, wid_int = create_graph(3, 2)
plt_int.set_title("Интеграл")
plt_sub, wid_sub = create_graph(3, 4)
plt_sub.set_title("Разность")
root.rowconfigure(index=3, weight=1)
root.mainloop()
