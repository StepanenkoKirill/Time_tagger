import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import time
##############################################################################

# Создание окна
window = Tk()
# Название окна
window.title('Окно')
# Размер окна
window.geometry('600x300')
# Фон окна
window.configure(bg='black')

a = ('TimeNewRoman', 14)
b = ('TimeNewRoman', 18)
c = ('TimeNewRoman', 14)

x = StringVar()
y = StringVar()
z = StringVar()

init = StringVar()
fin = StringVar()
t = StringVar()
step = StringVar()

Lbl = Label(window, text=0, font=a, bg='black', foreground='red')
Lbl.place(x=0, y=10, width=100, height=25)

###########################################################################
# Подключение зеркала
try:
    from MDT_COMMAND_LIB import *
except OSError as ex:
    print("Warning:", ex)
from ctypes import *

#region import dll functions

mdtLib = cdll.LoadLibrary(r"C:\Users\Admin\PycharmProjects\Mirror\MDT_COMMAND_LIB_x64.dll")

def CommonFunc(serialNumber):
    hdl = mdtOpen(serialNumber, 115200, 3)
    # or check by "mdtIsOpen(devs[0])"
    if (hdl < 0):
        print("Connect ", serialNumber, "fail")
        return -1
    else:
        print("Connect ", serialNumber, "successful")

    result = mdtIsOpen(serialNumber)
    print("mdtIsOpen ", result)

    id = []
    result = mdtGetId(hdl, id)
    if (result < 0):
        print("mdtGetId fail ", result)
    else:
        print(id)

    limitVoltage = [0]
    result = mdtGetLimtVoltage(hdl, limitVoltage)
    if (result < 0):
        print("mdtGetLimtVoltage fail ", result)
    else:
        print("mdtGetLimtVoltage ", limitVoltage)
    Lbl.config(text=limitVoltage)
    return hdl

###########################################################
# Проверка подключения пьезовинтов
def Check_X_AXiS(hdl):
    voltage = [0]
    result = mdtGetXAxisVoltage(hdl, voltage)
    if (result < 0):
        print("mdtGetXAxisVoltage fail ", result)
    else:
        print("mdtGetXAxisVoltage ", voltage)
    a = 0
    result = mdtSetXAxisVoltage(hdl, a)
    if (result < 0):
        print("mdtSetXAxisVoltage fail ", result)
    else:
        print("mdtSetXAxisVoltage ", 0)


def Check_Y_AXiS(hdl):
    voltage = [0]
    result = mdtGetYAxisVoltage(hdl, voltage)
    if (result < 0):
        print("mdtGetYAxisVoltage fail ", result)
    else:
        print("mdtGetYAxisVoltage ", voltage)

    result = mdtSetYAxisVoltage(hdl, 0)
    if (result < 0):
        print("mdtSetYAxisVoltage fail ", result)
    else:
        print("mdtSetYAxisVoltage ", 0)


def Check_Z_AXiS(hdl):
    voltage = [0]
    result = mdtGetZAxisVoltage(hdl, voltage)
    if (result < 0):
        print("mdtGetZAxisVoltage fail ", result)
    else:
        print("mdtGetZAxisVoltage ", voltage)

    result = mdtSetZAxisVoltage(hdl, 0)
    if (result < 0):
        print("mdtSetZAxisVoltage fail ", result)
    else:
        print("mdtSetZAxisVoltage ", 0)

# Меняем координаты
def MDT693BExample(serialNumber):
    hdl = CommonFunc(serialNumber)
    print('hdl:', hdl)
    if (hdl < 0):
        return
    Check_X_AXiS(hdl)
    Check_Y_AXiS(hdl)
    Check_Z_AXiS(hdl)

    xVoltage = float(x.get())
    yVoltage = float(y.get())
    zVoltage = float(z.get())


    result = mdtSetXYZAxisVoltage(hdl, xVoltage, yVoltage, zVoltage)
    if (result < 0):
        print("mdtSetXYZAxisVoltage fail ", result)
    else:
        print("mdtSetXYZAxisVoltage ", xVoltage, yVoltage, zVoltage)

    result = mdtClose(hdl)
    if (result == 0):
        print("mdtClose ", serialNumber)
    else:
        print("mdtClose fail", result)

Lbl1 = Label(window, text=0, font=a, bg='black', fg='white')
Lbl1.place(x=350, y=10, width=150, height=25)

def MDT693BExample_2(serialNumber):
    hdl = CommonFunc(serialNumber)
    if (hdl < 0):
        return
    Check_X_AXiS(hdl)
    Check_Y_AXiS(hdl)
    Check_Z_AXiS(hdl)

    xVoltage = 0
    yVoltage = 0
    zVoltage = 0

    scan_S = np.arange(float(init.get()), float(fin.get()) + 1, float(step.get()))


    for b in scan_S:

        xVoltage = b
        result = mdtSetXYZAxisVoltage(hdl, xVoltage, xVoltage, xVoltage)
        if (result < 0):
            print("mdtSetXYZAxisVoltage fail ", result)
        else:
            print("mdtSetXYZAxisVoltage ", xVoltage, yVoltage, zVoltage)
        Lbl1.config(text=b)
        plt.clf()

        plt.gcf().canvas.flush_events()
        time.sleep(float(t.get()))
    plt.ioff()


    result = mdtClose(hdl)
    if (result == 0):
        print("mdtClose ", serialNumber)
    else:
        print("mdtClose fail", result)
####################################################################
def main():
    print("*** MDT device python example ***")
    try:
        devs = mdtListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()

        for mdt in devs:
            if(mdt[1] == "MDT693B"):
                MDT693BExample(mdt[0])


    except Exception as ex:
        print("Warning:", ex)
    print("*** End ***")

def main_1():
    print("*** MDT device python example ***")
    try:
        devs = mdtListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()

        for mdt in devs:
            if(mdt[1] == "MDT693B"):
                MDT693BExample_2(mdt[0])


    except Exception as ex:
        print("Warning:", ex)
    print("*** End ***")
#######################################################################################

Label(window, text='Inital', font=a, bg='black', fg='white').place(x=200, y=50, width=200, height=25)
Entry(window, font=a, textvariable=init, bg='black', fg='white').place(x=350, y=50, width=45, height=30)
Entry(window, textvariable=init).insert(0, int(0))

Label(window, text='Final', font=a, bg='black', fg='white').place(x=200, y=80, width=200, height=25)
Entry(window, font=a, textvariable=fin, bg='black', fg='white').place(x=350, y=80, width=45, height=30)
Entry(window, textvariable=fin).insert(0, int(0))

Label(window, text='Time', font=a, bg='black', fg='white').place(x=200, y=110, width=200, height=25)
Entry(window, font=a, textvariable=t, bg='black', fg='white').place(x=350, y=110, width=45, height=30)
Entry(window, textvariable=t).insert(0, int(0))

Label(window, text='Step', font=a, bg='black', fg='white').place(x=200, y=140, width=200, height=25)
Entry(window, font=a, textvariable=step, bg='black', fg='white').place(x=350, y=140, width=45, height=30)
Entry(window, textvariable=step).insert(0, int(1))
############################################################################


Label(window, text='Voltage X', font=a, bg='black', fg='white').place(x=0, y=50, width=200, height=25)
Entry(window, font=a, textvariable=x, bg='black', fg='white').place(x=165, y=50, width=45, height=30)
Entry(window, textvariable=x).insert(0, 0)

Label(window, text='Voltage Y', font=a, bg='black', fg='white').place(x=0, y=80, width=200, height=25)
Entry(window, font=a, textvariable=y, bg='black', fg='white').place(x=165, y=80, width=45, height=30)
Entry(window, textvariable=y).insert(0, int(0))

Label(window, text='Voltage Z', font=a, bg='black', fg='white').place(x=0, y=110, width=200, height=25)
Entry(window, font=a, textvariable=z, bg='black', fg='white').place(x=165, y=110, width=45, height=30)
Entry(window, textvariable=z).insert(0, 0)
###################################################################
Button(window, text='Start scan', font=b, width=15, bg='gray', command=lambda: [main_1()]).place(x=300, y=200, width=250, height=40)

Button(window, text='OK', font=b, width=15, bg='gray', command=lambda: [main()]).place(x=20, y=200, width=250, height=40)

Button(window, text='Close', font=b, width=15, bg='red', command=window.quit).place(x=160, y=250, width=250, height=40)

window.mainloop()