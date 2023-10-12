import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import scipy.special
from tkinter import *
from tkinter import ttk
import random
import time
from collections import deque
import matplotlib.animation as animation
import TEST_LG
#from holoeye import slmdisplaysdk

#slmdisplaysdk.SLMDisplay().utilsSLMPreviewShow()
#slm = slmdisplaysdk.SLMDisplay()
#slm.utilsSLMPreviewShow()

# Построение окна
window = Tk()
window.title('Окно')
window.geometry('1920x1080')
window.configure(bg='white')

# Создание стиля влкадок и поля вкладок
s = ttk.Style()
s.configure('TNotebook.Tab', width=15, font='helvetica 15', padding=10)

# 'TNotebook.Tab' - применение к вкладкам
# width=15 - ширина кнопки вкладки
# font='helvetica 15' - размер шрифта
# padding=10 - высота кнопки вкладки

tab_control = ttk.Notebook(window)
tab_control.pack(expand=2, fill='both')

tab1 = Frame(tab_control, bg="white")
tab_control.add(tab1, text='      Вкладка 2')

tab2 = Frame(tab_control, bg="white")
tab_control.add(tab2, text='      Вкладка 3')
# scrollbar = ttk.Scrollbar(window, orient="horizontal")
# scrollbar.place(x=0, y=900, width=1920)

# Берет значения
v_1 = StringVar()
x_1 = StringVar()
y_1 = StringVar()
w = StringVar()
phase = StringVar()
blazed = StringVar()
weight = StringVar()
gray = StringVar()
#

fig2, ax2 = plt.subplots(1, 1, figsize=(7, 5), constrained_layout=True)

canvas2 = FigureCanvasTkAgg(fig2, master=tab2)
# canvas2.draw()
canvas2.get_tk_widget().pack(expand=0)
canvas2.get_tk_widget().place(x=0, y=0)

###########################################################################
# def B():
#     newWindow = Toplevel(window)
#     newWindow.geometry('1920x1080')
#     newWindow.configure(bg='white')
#
#
# fig1, ax1 = plt.subplots(1, 1, figsize=(7, 5), constrained_layout=True)
#
# canvas1 = FigureCanvasTkAgg(fig1, master=newWindow)
# canvas1.draw()
# canvas1.get_tk_widget().pack(expand=0)
# canvas1.get_tk_widget().place(x=800, y=0)
#
# line, = ax1.plot([], [], color='black')
#
# npoints = 10
# x_5 = deque([0], maxlen=npoints)
# y_5 = deque([0], maxlen=npoints)
#
# def update(i):
#     x_5.append(x_5[-1] + 1)  # update data
#     y_5.append(y_5[-1] + random.randint(-10, 10))
#     line.set_data(x_5, y_5)
#     ax1.relim()  # update axes limits
#     ax1.autoscale_view()
#     return line,
# def A():
#     interval = 1
#     ani = animation.FuncAnimation(fig1, update, interval=interval)
#     canvas1.draw()


# def a():
#
#     interval = 1
#     ani = animation.FuncAnimation(fig1, update, interval=interval)
#     canvas1.draw()
#################################################################################
# import tkinter as tk
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.btn = tk.Button(self, text="Открыть новое окно")
#         self.btn.place(x=100, y=700)
#         self.fig1, self.ax1 = plt.subplots(1, 1, figsize=(7, 5), constrained_layout=True)
#
#         self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self)
#         self.canvas1.draw()
#         self.canvas1.get_tk_widget().pack(expand=0)
#         self.canvas1.get_tk_widget().place(x=0, y=0)
#         self.geometry('1200x800')
#         self.configure(bg='white')

    # def open_window(self):
    #     about = TEST_LG.file_2.About(self)
    #     about.grab_set()

#################################################################################
a = ('TimeNewRoman', 18)
b = ('TimeNewRoman', 24)
#
Button(window, text='Закрыть окно', bg='white', font=b, command=window.quit).place(x=1650, y=920, width=250, height=50)

Button(tab2, text='Рассчитать LG', font=b, width=15, bg='white', command=lambda: [TEST_LG.file_1.CALCULATE()]).place(x=260, y=880, width=300, height=50)

Button(tab2, text='k', font=b, width=15, bg='white', command=lambda: [TEST_LG.file_2.App()]).place(x=600, y=880, width=260, height=50)
# #Button(window, text='Очистить ОУМ', font=a, width=15, bg='orange', command=clean_value_1).place(x=140, y=620, width=120)

Label(tab2, text='Положение X', font=a, bg='white').place(x=250, y=520, width=200, height=30)
Entry(tab2, font=a, textvariable=x_1).place(x=450, y=520, width=150, height=30)
Entry(tab2, textvariable=x_1).insert(0, int(-540))

Label(tab2, text='Положение Y', font=a, bg='white').place(x=250, y=570, width=200, height=30)
Entry(tab2, font=a, textvariable=y_1).place(x=450, y=570, width=150, height=30)
Entry(tab2, textvariable=y_1).insert(0, int(-40))

Label(tab2, text='Размер пучка', font=a, bg='white').place(x=250, y=620, width=200, height=30)
Entry(tab2, font=a, textvariable=w).place(x=450, y=620, width=150, height=30)
Entry(tab2, textvariable=w).insert(0, int(80))

Label(tab2, text='Фаза ОУМ', font=a, bg='white').place(x=250, y=670, width=200, height=30)
Entry(tab2, font=a, textvariable=phase).place(x=450, y=670, width=150, height=30)
Entry(tab2, textvariable=phase).insert(0, int(0))

Label(tab2, text='ОУМ', font=a, bg='white').place(x=300, y=720, width=150, height=30)
Entry(tab2, font=a, textvariable=v_1).place(x=450, y=720, width=150, height=30)
Entry(tab2, textvariable=v_1).insert(0, int(0))

Label(tab2, text='Bec', font=a, bg='white').place(x=300, y=770, width=150, height=30)
Entry(tab2, font=a, textvariable=weight).place(x=450, y=770, width=150, height=30)
Entry(tab2, textvariable=weight).insert(0, int(100))

Label(tab2, text='Период', font=a, bg='white').place(x=300, y=820, width=150, height=30)
Entry(tab2, font=a, textvariable=blazed).place(x=450, y=820, width=150, height=30)
Entry(tab2, textvariable=blazed).insert(0, int(10))

Label(tab2, text='Уровень' + '\n' + 'серого', font=a, bg='white').place(x=0, y=805, width=150, height=60)
Entry(tab2, font=a, textvariable=gray).place(x=150, y=820, width=150, height=30)
Entry(tab2, textvariable=gray).insert(0, int(1))

window.mainloop()