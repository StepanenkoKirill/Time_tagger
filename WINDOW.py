import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import scipy.special
from tkinter import *
from tkinter import ttk
import time
import random
from collections import deque
import matplotlib.animation as animation
import window_LG
#from holoeye import slmdisplaysdk
# from sys import exit
# exit(0)
#исполняемый участок кода

#from holoeye import slmdisplaysdk

#slmdisplaysdk.SLMDisplay().utilsSLMPreviewShow()
#slm = slmdisplaysdk.SLMDisplay()
#slm.utilsSLMPreviewShow()
a = ('TimeNewRoman', 14)
b = ('TimeNewRoman', 18)
#################################################################################
# Создание окна
window = Tk()
# Название окна
window.title('Окно')
# Размер окна
window.geometry('1920x1080')
# Фон окна
window.configure(bg='white')
#################################################################################
# Создание стиля влкадок и поля вкладок
s = ttk.Style()
s.configure('TNotebook.Tab', width=15, font='helvetica 15', padding=10)
# 'TNotebook.Tab' - рименение к вкладкам
# width=15 - ширина кнопки вкладки
# font='helvetica 15' - размер шрифта
# padding=10 - высота кнопки вкладки
tab_control = ttk.Notebook(window)
tab_control.pack(expand=2, fill='both')
#################################################################################
# Вкладки
tab4 = Frame(tab_control, bg="white")
tab_control.add(tab4, text='      Вкладка 1')

tab1 = Frame(tab_control, bg="white")
tab_control.add(tab1, text='      Вкладка 2')

tab2 = Frame(tab_control, bg="white")
tab_control.add(tab2, text='      Вкладка 3')

tab3 = Frame(tab_control, bg="white")
tab_control.add(tab3, text='      Видность')

tab5 = Frame(tab_control, bg="white")
tab_control.add(tab5, text='      Вкладка 5')
#################################################################################
# Переменные
l_0 = StringVar() # Орбитальная компонента (ОУМ)
l_value_0 = 0
x_0 = StringVar() # Полжение по x
x_value_0 = 0
y_0 = StringVar() # Положение по y
y_value_0 = 0
w_0 = StringVar() # Диаметр пучка
w_value_0 = 150
phase_0 = StringVar() # Фаза
phase_value_0 = 0
blazed_0 = StringVar() # Период дифракционной решетки
blazed_value_0 = 10
weight_0 = StringVar() # Вес
weight_value_0 = 100
gray_level_0 = StringVar() # Уровень серого
gray_level_value_0 = 0.6

l = StringVar()
l_L = StringVar() # Орбитальная компонента (ОУМ)
l_value_L = 0
l_R = StringVar() # Орбитальная компонента (ОУМ)
l_value_R = 0
l_SECOND = StringVar() # Орбитальная компонента (ОУМ)
l_value_SECOND = 0
l_FIRST = StringVar() # Орбитальная компонента (ОУМ)
l_value_FIRST = 0
l_TWO = StringVar() # Орбитальная компонента (ОУМ)
l_value_TWO = 0

A = StringVar()
A_L = StringVar() # Полжение по x
A_value_L = 0
A_R = StringVar() # Полжение по x
A_value_R = 0
A_SECOND = StringVar() # Полжение по x
A_value_SECOND = 0
A_FIRST = StringVar() # Полжение по x
A_value_FIRST = 0
A_TWO = StringVar() # Полжение по x
A_value_TWO = 0

B = StringVar()
B_L = StringVar() # Положение по y
B_value_L = 0
B_R = StringVar() # Положение по y
B_value_R = 0
B_SECOND = StringVar() # Положение по y
B_value_SECOND = 0
B_FIRST = StringVar() # Положение по y
B_value_FIRST = 0
B_TWO = StringVar() # Положение по y
B_value_TWO = 0

w = StringVar()
w_L = StringVar() # Диаметр пучка
w_value_L = 80
w_R = StringVar() # Диаметр пучка
w_value_R = 80
w_SECOND = StringVar() # Диаметр пучка
w_value_SECOND= 80
w_FIRST = StringVar() # Диаметр пучка
w_value_FIRST = 80
w_TWO = StringVar() # Диаметр пучка
w_value_TWO = 80

phase = StringVar()
phase_L = StringVar() # Фаза
phase_value_L = 0
phase_R = StringVar() # Фаза
phase_value_R = 0
phase_SECOND = StringVar() # Фаза
phase_value_SECOND = 0
phase_FIRST = StringVar() # Фаза
phase_value_FIRST = 0
phase_TWO = StringVar() # Фаза
phase_value_TWO = 0

blazed = StringVar()
blazed_L = StringVar() # Период дифракционной решетки
blazed_value_L = 10
blazed_R = StringVar() # Период дифракционной решетки
blazed_value_R = 10
blazed_SECOND = StringVar() # Период дифракционной решетки
blazed_value_SECOND = 10
blazed_FIRST = StringVar() # Период дифракционной решетки
blazed_value_FIRST = 10
blazed_TWO = StringVar() # Период дифракционной решетки
blazed_value_TWO = 10

weight = StringVar()
weight_L = StringVar() # Вес
weight_value_L = 100
weight_R = StringVar() # Вес
weight_value_R = 100
weight_SECOND = StringVar() # Вес
weight_value_SECOND = 100
weight_FIRST = StringVar() # Вес
weight_value_FIRST = 100
weight_TWO = StringVar() # Вес
weight_value_TWO = 100

gray_level = StringVar()
gray_level_L = StringVar() # Уровень серого
gray_level_value_L = 0.6
gray_level_R = StringVar() # Уровень серого
gray_level_value_R = 0.6
gray_level_SECOND = StringVar() # Уровень серого
gray_level_value_SECOND = 0.6
gray_level_FIRST = StringVar() # Уровень серого
gray_level_value_FIRST = 0.6
gray_level_TWO = StringVar() # Уровень серого
gray_level_value_TWO = 0.6
#################################################################################
# Построение координатной плоскости
fig4, ax4 = plt.subplots(1, 3, figsize=(19, 4), constrained_layout=True)
canvas_4 = FigureCanvasTkAgg(fig4, tab4)
canvas_4.draw()
canvas_4.get_tk_widget().place(x=0, y=0)

fig1, ax1 = plt.subplots(1, 2, figsize=(13, 4), constrained_layout=True)
canvas_1 = FigureCanvasTkAgg(fig1, tab1)
canvas_1.draw()
canvas_1.get_tk_widget().place(x=30, y=10)

fig2, ax2 = plt.subplots(1, 2, figsize=(13, 4), constrained_layout=True)
canvas_2 = FigureCanvasTkAgg(fig2, tab2)
canvas_2.draw()
canvas_2.get_tk_widget().place(x=30, y=10)

fig5, ax5 = plt.subplots(1, 1, figsize=(13, 4), constrained_layout=True)
canvas_5 = FigureCanvasTkAgg(fig5, tab5)

canvas_5.draw()
canvas_5.get_tk_widget().place(x=0, y=0)

#################################################################################
# Жертва
fig3, ax3 = plt.subplots(1, figsize=(0.0000000000000000000001, 0.0000000000000000000001), constrained_layout=True)
plt.xticks([])
plt.yticks([])
canvas_3 = FigureCanvasTkAgg(fig3, tab3)
canvas_3.draw()
canvas_3.get_tk_widget().place(x=0, y=0)
#################################################################################

# Расчет видности
l_initial_1 = StringVar()
l_final_1 = StringVar()
l_initial_2 = StringVar()
l_final_2 = StringVar()
l_initial_3 = StringVar()
l_final_3 = StringVar()
l_initial_first = StringVar()
l_final_first = StringVar()
l_initial_second = StringVar()
l_final_second = StringVar()
sleep1 = StringVar()
sleep2 = StringVar()
scan1 = StringVar()
scan2 = StringVar()
spin1 = Spinbox(tab3, values=(1, 2, 3, 4, 5, 6), font=a, wrap=True, textvariable=scan1).place(x=640, y=800, width=50, height=30)
# Создаем виджет Spinbox
spin2 = Spinbox(tab3, values=(1, 2), font=a, wrap=True, textvariable=scan2).place(x=1305, y=800, width=50, height=30)

#################################################################################
# def P():
#     ax5.imshow(Laguerre_Gauss().LG_LEFT())
#     canvas_5.draw()
# def Class_Calculate_of_OAM():
#     #M = np.hstack((Laguerre_Gauss().LG_LEFT(), Calculation_of_OAM().Calculate()))
#     ax3[0].imshow(Calculation_of_OAM().Calculate(), cmap='gray')
#     #slm.showData(U)
#     canvas_3.draw()
#################################################################################

[line] = ax5.plot([], [], color='black')
plt.xticks([])
plt.yticks([])
npoints = 10
x_5 = deque([0], maxlen=npoints)
y_5 = deque([0], maxlen=npoints)

    # def __init__(self):
    #     self.line = ax[1].plot([], [], color='black')
    #     # plt.xticks([])
    #     self.npoints = 10
    #     self.x = deque([0], maxlen=self.npoints)
    #     self.y = deque([0], maxlen=self.npoints)

def update(i):
    pass
    x_5.append(x_5[-1] + 1)  # update data
    y_5.append(y_5[-1] + random.randint(-10, 10))
    line.set_data(x_5, y_5)
    ax5.relim()  # update axes limits
    ax5.autoscale_view()

def a():

    interval = 100
    ani = animation.FuncAnimation(fig5, update, interval=interval)
    canvas_5.draw()

#################################################################################
# Создание полей вводи и кнопок ввода

# Общие кнопки
Button(window, text='Закрыть', bg='white', font=b, command=window.quit).place(x=1650, y=920, width=250, height=40)
# Button(window, text='Закрыть', bg='white', font=b, command=lambda: [Plot().update()]).place(x=1650, y=800, width=250, height=40)
# Кнопки 2-й вкладки
Button(tab5, text='START', font=b, width=15, bg='white', command=lambda: [a()]).place(x=70, y=870, width=250, height=40)

Button(tab1, text='Рассчитать LG_L', font=b, width=15, bg='white', command=lambda: [window_LG.tab_1.Laguerre_Gauss().LG_LEFT(),\
window_LG.tab_1.Class_LG()]).place(x=70, y=870, width=250, height=40)

Button(tab1, text='Рассчитать LG_R', font=b, width=15, bg='white', command=lambda: [window_LG.tab_1.Laguerre_Gauss().LG_RIGHT(),\
window_LG.tab_1.Class_LG()]).place(x=440, y=870, width=250, height=40)

Button(tab1, text='Рассчитать LG_T', font=b, width=15, bg='white', command=lambda: [window_LG.tab_1.Laguerre_Gauss().LG_T(),\
window_LG.tab_1.Class_LG_1()]).place(x=870, y=870, width=250, height=40)

# Кнопки 3-й вкладки
Button(tab2, text='Рассчитать LG_L', font=b, width=15, bg='white', command=lambda: [window_LG.tab_2.Classic_LG_1()]).place(x=70, y=870, width=250, height=40)

Button(tab2, text='Рассчитать LG_R', font=b, width=15, bg='white', command=lambda: [window_LG.tab_2.Classic_LG_2()]).place(x=870, y=870, width=250, height=40)

# Кнопки 4-й вкладки
Button(tab3, text='Рассчитать OAM', font=b, width=15, bg='white', command=lambda: [window_LG.tab_3.Calculation_of_OAM().Calculate()]).\
place(x=280, y=840, width=250, height=40)

Button(tab3, text='Рассчитать OAM', font=b, width=15, bg='white', command=lambda: [window_LG.tab_3.Calculation_of_OAM().Calculate_1()]).\
place(x=980, y=840, width=250, height=40)

Button(tab4, text='Рассчитать LG', font=b, width=15, bg='white', command=lambda: [window_LG.tab_4.L_G().LG()]).\
place(x=50, y=880, width=250, height=40)

#################################################################################
Label(tab4, text='Положение X', font=a, bg='white').place(x=0, y=520, width=200, height=25)
Entry(tab4, font=a, textvariable=x_0).place(x=200, y=520, width=150, height=30)
Entry(tab4, textvariable=x_0).insert(0, x_value_0)

Label(tab4, text='Положение Y', font=a, bg='white').place(x=0, y=560, width=200, height=25)
Entry(tab4, font=a, textvariable=y_0).place(x=200, y=560, width=150, height=30)
Entry(tab4, textvariable=y_0).insert(0, y_value_0)

Label(tab4, text='Размер пучка', font=a, bg='white').place(x=0, y=600, width=200, height=25)
Entry(tab4, font=a, textvariable=w_0).place(x=200, y=600, width=150, height=30)
Entry(window, textvariable=w_0).insert(0, w_value_0)

Label(tab4, text='Фаза ОУМ', font=a, bg='white').place(x=0, y=640, width=200, height=25)
Entry(tab4, font=a, textvariable=phase_0).place(x=200, y=640, width=150, height=25)
Entry(tab4, textvariable=phase_0).insert(0, phase_value_0)

Label(tab4, text='ОУМ', font=a, bg='white').place(x=50, y=680, width=150, height=25)
Entry(tab4, font=a, textvariable=l_0).place(x=200, y=680, width=150, height=25)
Entry(tab4, textvariable=l_0).insert(0, l_value_0)

Label(tab4, text='Bec', font=a, bg='white').place(x=50, y=720, width=150, height=25)
Entry(tab4, font=a, textvariable=weight_0).place(x=200, y=720, width=150, height=25)
Entry(tab4, textvariable=weight_0).insert(0, weight_value_0)

Label(tab4, text='Период', font=a, bg='white').place(x=50, y=760, width=150, height=25)
Entry(tab4, font=a, textvariable=blazed_0).place(x=200, y=760, width=150, height=25)
Entry(tab4, textvariable=blazed_0).insert(0, blazed_value_0)

Label(tab4, text='Уровень' + '\n' + 'серого', font=a, bg='white').place(x=50, y=790, width=150, height=60)
Entry(tab4, font=a, textvariable=gray_level_0).place(x=200, y=805, width=150, height=25)
Entry(tab4, textvariable=gray_level_0).insert(0, gray_level_value_0)
#################################################################################
# Вкладка 2
# command=lambda: [Calculation_of_OAM()]
# Left_Side

Label(tab1, text='Положение X', font=a, bg='white').place(x=0, y=520, width=200, height=25)
Entry(tab1, font=a, textvariable=A_L).place(x=200, y=520, width=150, height=30)
Entry(tab1, textvariable=A_L).insert(0, A_value_L)

Label(tab1, text='Положение Y', font=a, bg='white').place(x=0, y=560, width=200, height=25)
Entry(tab1, font=a, textvariable=B_L).place(x=200, y=560, width=150, height=30)
Entry(tab1, textvariable=B_L).insert(0, B_value_L)

Label(tab1, text='Размер пучка', font=a, bg='white').place(x=0, y=600, width=200, height=25)
Entry(tab1, font=a, textvariable=w_L).place(x=200, y=600, width=150, height=30)
Entry(tab1, textvariable=w_L).insert(0, w_value_L)

Label(tab1, text='Фаза ОУМ', font=a, bg='white').place(x=0, y=640, width=200, height=25)
Entry(tab1, font=a, textvariable=phase_L).place(x=200, y=640, width=150, height=25)
Entry(tab1, textvariable=phase_L).insert(0, phase_value_L)

Label(tab1, text='ОУМ', font=a, bg='white').place(x=50, y=680, width=150, height=25)
Entry(tab1, font=a, textvariable=l_L).place(x=200, y=680, width=150, height=25)
Entry(tab1, textvariable=l_L).insert(0, l_value_L)

Label(tab1, text='Bec', font=a, bg='white').place(x=50, y=720, width=150, height=25)
Entry(tab1, font=a, textvariable=weight_L).place(x=200, y=720, width=150, height=25)
Entry(tab1, textvariable=weight_L).insert(0, weight_value_L)

Label(tab1, text='Период', font=a, bg='white').place(x=50, y=760, width=150, height=25)
Entry(tab1, font=a, textvariable=blazed_L).place(x=200, y=760, width=150, height=25)
Entry(tab1, textvariable=blazed_L).insert(0, blazed_value_L)

Label(tab1, text='Уровень' + '\n' + 'серого', font=a, bg='white').place(x=50, y=790, width=150, height=60)
Entry(tab1, font=a, textvariable=gray_level_L).place(x=200, y=805, width=150, height=25)
Entry(tab1, textvariable=gray_level_L).insert(0, gray_level_value_L)

# Right_Side

Label(tab1, text='Положение X', font=a, bg='white').place(x=360, y=520, width=200, height=25)
Entry(tab1, font=a, textvariable=A_R).place(x=560, y=520, width=150, height=30)
Entry(tab1, textvariable=A_R).insert(0, A_value_R)

Label(tab1, text='Положение Y', font=a, bg='white').place(x=360, y=560, width=200, height=25)
Entry(tab1, font=a, textvariable=B_R).place(x=560, y=560, width=150, height=30)
Entry(tab1, textvariable=B_R).insert(0, B_value_R)

Label(tab1, text='Размер пучка', font=a, bg='white').place(x=360, y=600, width=200, height=25)
Entry(tab1, font=a, textvariable=w_R).place(x=560, y=600, width=150, height=30)
Entry(tab1, textvariable=w_R).insert(0, w_value_R)

Label(tab1, text='Фаза ОУМ', font=a, bg='white').place(x=360, y=640, width=200, height=25)
Entry(tab1, font=a, textvariable=phase_R).place(x=560, y=640, width=150, height=25)
Entry(tab1, textvariable=phase_R).insert(0, phase_value_R)

Label(tab1, text='ОУМ', font=a, bg='white').place(x=410, y=680, width=150, height=25)
Entry(tab1, font=a, textvariable=l_R).place(x=560, y=680, width=150, height=25)
Entry(tab1, textvariable=l_R).insert(0, l_value_R)

Label(tab1, text='Bec', font=a, bg='white').place(x=410, y=720, width=150, height=25)
Entry(tab1, font=a, textvariable=weight_R).place(x=560, y=720, width=150, height=25)
Entry(tab1, textvariable=weight_R).insert(0, weight_value_R)

Label(tab1, text='Период', font=a, bg='white').place(x=410, y=760, width=150, height=25)
Entry(tab1, font=a, textvariable=blazed_R).place(x=560, y=760, width=150, height=25)
Entry(tab1, textvariable=blazed_R).insert(0, blazed_value_R)

Label(tab1, text='Уровень' + '\n' + 'серого', font=a, bg='white').place(x=410, y=790, width=150, height=60)
Entry(tab1, font=a, textvariable=gray_level_R).place(x=560, y=805, width=150, height=25)
Entry(tab1, textvariable=gray_level_R).insert(0, gray_level_value_R)

# TWO_Side

Label(tab1, text='Положение X', font=a, bg='white').place(x=800, y=520, width=200, height=25)
Entry(tab1, font=a, textvariable=A_TWO).place(x=1000, y=520, width=150, height=30)
Entry(tab1, textvariable=A_TWO).insert(0, A_value_TWO)

Label(tab1, text='Положение Y', font=a, bg='white').place(x=800, y=560, width=200, height=25)
Entry(tab1, font=a, textvariable=B_TWO).place(x=1000, y=560, width=150, height=30)
Entry(tab1, textvariable=B_TWO).insert(0, B_value_TWO)

Label(tab1, text='Размер пучка', font=a, bg='white').place(x=800, y=600, width=200, height=25)
Entry(tab1, font=a, textvariable=w_TWO).place(x=1000, y=600, width=150, height=30)
Entry(tab1, textvariable=w_TWO).insert(0, w_value_TWO)

Label(tab1, text='Фаза ОУМ', font=a, bg='white').place(x=800, y=640, width=200, height=25)
Entry(tab1, font=a, textvariable=phase_TWO).place(x=1000, y=640, width=150, height=25)
Entry(tab1, textvariable=phase_TWO).insert(0, phase_value_TWO)

Label(tab1, text='ОУМ', font=a, bg='white').place(x=850, y=680, width=150, height=25)
Entry(tab1, font=a, textvariable=l_TWO).place(x=1000, y=680, width=150, height=25)
Entry(tab1, textvariable=l_TWO).insert(0, l_value_TWO)

Label(tab1, text='Bec', font=a, bg='white').place(x=850, y=720, width=150, height=25)
Entry(tab1, font=a, textvariable=weight_TWO).place(x=1000, y=720, width=150, height=25)
Entry(tab1, textvariable=weight_TWO).insert(0, weight_value_TWO)

Label(tab1, text='Период', font=a, bg='white').place(x=850, y=760, width=150, height=25)
Entry(tab1, font=a, textvariable=blazed_TWO).place(x=1000, y=760, width=150, height=25)
Entry(tab1, textvariable=blazed_TWO).insert(0, blazed_value_TWO)

Label(tab1, text='Уровень' + '\n' + 'серого', font=a, bg='white').place(x=850, y=790, width=150, height=60)
Entry(tab1, font=a, textvariable=gray_level_TWO).place(x=1000, y=805, width=150, height=25)
Entry(tab1, textvariable=gray_level_TWO).insert(0, gray_level_value_TWO)
#################################################################################
# Вкладка 3
# FIRST_Side

Label(tab2, text='Положение X', font=a, bg='white').place(x=0, y=520, width=200, height=25)
Entry(tab2, font=a, textvariable=A_FIRST).place(x=200, y=520, width=150, height=30)
Entry(tab2, textvariable=A_FIRST).insert(0, A_value_FIRST)

Label(tab2, text='Положение Y', font=a, bg='white').place(x=0, y=560, width=200, height=25)
Entry(tab2, font=a, textvariable=B_FIRST).place(x=200, y=560, width=150, height=30)
Entry(tab2, textvariable=B_FIRST).insert(0, B_value_FIRST)

Label(tab2, text='Размер пучка', font=a, bg='white').place(x=0, y=600, width=200, height=25)
Entry(tab2, font=a, textvariable=w_FIRST).place(x=200, y=600, width=150, height=30)
Entry(tab2, textvariable=w_FIRST).insert(0, w_value_FIRST)

Label(tab2, text='Фаза ОУМ', font=a, bg='white').place(x=0, y=640, width=200, height=25)
Entry(tab2, font=a, textvariable=phase_FIRST).place(x=200, y=640, width=150, height=25)
Entry(tab2, textvariable=phase_FIRST).insert(0, phase_value_FIRST)

Label(tab2, text='ОУМ', font=a, bg='white').place(x=50, y=680, width=150, height=25)
Entry(tab2, font=a, textvariable=l_FIRST).place(x=200, y=680, width=150, height=25)
Entry(tab2, textvariable=l_FIRST).insert(0, l_value_FIRST)

Label(tab2, text='Bec', font=a, bg='white').place(x=50, y=720, width=150, height=25)
Entry(tab2, font=a, textvariable=weight_FIRST).place(x=200, y=720, width=150, height=25)
Entry(tab2, textvariable=weight_FIRST).insert(0, weight_value_FIRST)

Label(tab2, text='Период', font=a, bg='white').place(x=50, y=760, width=150, height=25)
Entry(tab2, font=a, textvariable=blazed_FIRST).place(x=200, y=760, width=150, height=25)
Entry(tab2, textvariable=blazed_FIRST).insert(0, blazed_value_FIRST)

Label(tab2, text='Уровень' + '\n' + 'серого', font=a, bg='white').place(x=50, y=790, width=150, height=60)
Entry(tab2, font=a, textvariable=gray_level_FIRST).place(x=200, y=805, width=150, height=25)
Entry(tab2, textvariable=gray_level_FIRST).insert(0, gray_level_value_FIRST)

# SECOND_Side

Label(tab2, text='Положение X', font=a, bg='white').place(x=800, y=520, width=200, height=25)
Entry(tab2, font=a, textvariable=A_SECOND).place(x=1000, y=520, width=150, height=30)
Entry(tab2, textvariable=A_SECOND).insert(0, A_value_SECOND)

Label(tab2, text='Положение Y', font=a, bg='white').place(x=800, y=560, width=200, height=25)
Entry(tab2, font=a, textvariable=B_SECOND).place(x=1000, y=560, width=150, height=30)
Entry(tab2, textvariable=B_SECOND).insert(0, B_value_SECOND)

Label(tab2, text='Размер пучка', font=a, bg='white').place(x=800, y=600, width=200, height=25)
Entry(tab2, font=a, textvariable=w_SECOND).place(x=1000, y=600, width=150, height=30)
Entry(tab2, textvariable=w_SECOND).insert(0, w_value_SECOND)

Label(tab2, text='Фаза ОУМ', font=a, bg='white').place(x=800, y=640, width=200, height=25)
Entry(tab2, font=a, textvariable=phase_SECOND).place(x=1000, y=640, width=150, height=25)
Entry(tab2, textvariable=phase_SECOND).insert(0, phase_value_SECOND)

Label(tab2, text='ОУМ', font=a, bg='white').place(x=850, y=680, width=150, height=25)
Entry(tab2, font=a, textvariable=l_SECOND).place(x=1000, y=680, width=150, height=25)
Entry(tab2, textvariable=l_SECOND).insert(0, l_value_SECOND)

Label(tab2, text='Bec', font=a, bg='white').place(x=850, y=720, width=150, height=25)
Entry(tab2, font=a, textvariable=weight_SECOND).place(x=1000, y=720, width=150, height=25)
Entry(tab2, textvariable=weight_SECOND).insert(0, weight_value_SECOND)

Label(tab2, text='Период', font=a, bg='white').place(x=850, y=760, width=150, height=25)
Entry(tab2, font=a, textvariable=blazed_SECOND).place(x=1000, y=760, width=150, height=25)
Entry(tab2, textvariable=blazed_SECOND).insert(0, blazed_value_SECOND)

Label(tab2, text='Уровень' + '\n' + 'серого', font=a, bg='white').place(x=850, y=790, width=150, height=60)
Entry(tab2, font=a, textvariable=gray_level_SECOND).place(x=1000, y=805, width=150, height=25)
Entry(tab2, textvariable=gray_level_SECOND).insert(0, gray_level_value_SECOND)
#################################################################################
# Видность
Label(tab3, text='l_initial_1', font=a, bg='white').place(x=105, y=720, width=100, height=25)
Entry(tab3, font=a, textvariable=l_initial_1).place(x=205, y=720, width=100, height=30)
Entry(tab3, textvariable=l_initial_1).insert(0, int(-5))

Label(tab3, text='l_final_1', font=a, bg='white').place(x=105, y=760, width=100, height=25)
Entry(tab3, font=a, textvariable=l_final_1).place(x=205, y=760, width=100, height=30)
Entry(tab3, textvariable=l_final_1).insert(0, int(5))

Label(tab3, text='l_initial_2', font=a, bg='white').place(x=305, y=720, width=100, height=25)
Entry(tab3, font=a, textvariable=l_initial_2).place(x=405, y=720, width=100, height=30)
Entry(tab3, textvariable=l_initial_2).insert(0, int(-5))

Label(tab3, text='l_final_2', font=a, bg='white').place(x=305, y=760, width=100, height=25)
Entry(tab3, font=a, textvariable=l_final_2).place(x=405, y=760, width=100, height=30)
Entry(tab3, textvariable=l_final_2).insert(0, int(5))

Label(tab3, text='l_initial_3', font=a, bg='white').place(x=505, y=720, width=100, height=25)
Entry(tab3, font=a, textvariable=l_initial_3).place(x=605, y=720, width=100, height=30)
Entry(tab3, textvariable=l_initial_3).insert(0, int(-5))

Label(tab3, text='l_final_3', font=a, bg='white').place(x=505, y=760, width=100, height=25)
Entry(tab3, font=a, textvariable=l_final_3).place(x=605, y=760, width=100, height=30)
Entry(tab3, textvariable=l_final_3).insert(0, int(5))

Label(tab3, text='Sleep', font=a, bg='white').place(x=305, y=800, width=100, height=25)
Entry(tab3, font=a, textvariable=sleep1).place(x=405, y=800, width=100, height=30)
Entry(tab3, textvariable=sleep1).insert(0, float(0.5))
#
Label(tab3, text='l_initial_f', font=a, bg='white').place(x=905, y=720, width=100, height=25)
Entry(tab3, font=a, textvariable=l_initial_first).place(x=1005, y=720, width=100, height=30)
Entry(tab3, textvariable=l_initial_first).insert(0, int(-5))

Label(tab3, text='l_final_f', font=a, bg='white').place(x=905, y=760, width=100, height=25)
Entry(tab3, font=a, textvariable=l_final_first).place(x=1005, y=760, width=100, height=30)
Entry(tab3, textvariable=l_final_first).insert(0, int(5))

Label(tab3, text='l_initial_s', font=a, bg='white').place(x=1105, y=720, width=100, height=25)
Entry(tab3, font=a, textvariable=l_initial_second).place(x=1205, y=720, width=100, height=30)
Entry(tab3, textvariable=l_initial_second).insert(0, int(-5))

Label(tab3, text='l_final_s', font=a, bg='white').place(x=1105, y=760, width=100, height=25)
Entry(tab3, font=a, textvariable=l_final_second).place(x=1205, y=760, width=100, height=30)
Entry(tab3, textvariable=l_final_second).insert(0, int(5))

Label(tab3, text='Sleep', font=a, bg='white').place(x=1005, y=800, width=100, height=25)
Entry(tab3, font=a, textvariable=sleep2).place(x=1105, y=800, width=100, height=30)
Entry(tab3, textvariable=sleep2).insert(0, float(0.5))
#
Label(tab3, text='Левая часть:', font=a, bg='white').place(x=120, y=680, width=110, height=25)
Lbl1 = Label(tab3, text=0, font=a, bg='white')
Lbl1.place(x=235, y=680, width=35, height=25)

Label(tab3, text='Правая часть:', font=a, bg='white').place(x=300, y=680, width=150, height=25)
Lbl2 = Label(tab3, text=0, font=a, bg='white')
Lbl2.place(x=440, y=680, width=35, height=25)

Label(tab3, text='Второй SLM:', font=a, bg='white').place(x=495, y=680, width=150, height=25)
Lbl3 = Label(tab3, text=0, font=a, bg='white')
Lbl3.place(x=630, y=680, width=35, height=25)

Label(tab3, text='SLM 1:', font=a, bg='white').place(x=900, y=680, width=110, height=25)
Lbl4 = Label(tab3, text=0, font=a, bg='white')
Lbl4.place(x=990, y=680, width=35, height=25)

Label(tab3, text='SLM 2:', font=a, bg='white').place(x=1080, y=680, width=150, height=25)
Lbl5 = Label(tab3, text=0, font=a, bg='white')
Lbl5.place(x=1190, y=680, width=35, height=25)

Label(tab3, text='Режим:' + '\n' + '1: L->R' + '\n' + '2: R->L' + '\n' + '3: R->2' + '\n' + '4: 2->R' + '\n'\
                 + '5: L->2' + '\n' + '6: 2->L', font=a, bg='white').place(x=700, y=680, width=100, height=150)

Label(tab3, text='Режим:' + '\n' + '1: L->R' + '\n' + '2: R->L', font=a, bg='white').place(x=1300, y=635, width=100, height=150)

Label(tab3, text='Для нахождения видности необходимо сначала выбрать режим !!!', font=a, bg='white', fg='red').place(x=120, y=640, width=600, height=35)
#################################################################################
window.mainloop()