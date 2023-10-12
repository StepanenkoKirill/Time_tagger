import pyvisa
import threading
import time
from ThorlabsPM100 import ThorlabsPM100
import numpy as np
import TimeTagger
import pyvisa
import time
import threading
import numpy
from ThorlabsPM100 import ThorlabsPM100
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from time import sleep
import TimeTagger
try:
    from MDT_COMMAND_LIB import *
except OSError as ex:
    print("Warning:", ex)
from ctypes import *

mdtLib = cdll.LoadLibrary(r"C:\Users\photo\PycharmProjects\Time_tagger\MDT_COMMAND_LIB_x64.dll")

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
#############################################################################################
tagger = TimeTagger.createTimeTagger()
#
# counter = TimeTagger.Counter(tagger=tagger, channels=[1], binwidth=int(1e9), n_values=1)
# sleep(5)
# a = counter.getData()
# TT = a.flatten().tolist()

# TimeTagger.freeTimeTagger(tagger)

def MDT693BExample(serialNumber):
    hdl = CommonFunc(serialNumber)
    print('hdl:', hdl)
    if (hdl < 0):
        return

    Check_X_AXiS(hdl)
    Check_Y_AXiS(hdl)
    Check_Z_AXiS(hdl)
    volt = 96.38 # Напряжение, на котором есть пик
    mdtSetXYZAxisVoltage(hdl, volt, volt, volt)
    g = 1

    counter = TimeTagger.Counter(tagger=tagger, channels=[1], binwidth=int(1e10), n_values=1)

    while True and (volt > 0) and (volt < 100):
        # counter = TimeTagger.Counter(tagger=tagger, channels=[1], binwidth=int(1e10), n_values=1)

        a = counter.getData()
        TT = a.flatten().tolist()
        time.sleep(2e-3)
        # g = int(''.join(TT))
        # print(g)
        d = [300] # Величина счета, на которую стабилизируемся
        print('d', d)
        print(TT)

        mdtSetXYZAxisVoltage(hdl, volt, volt, volt)
        # Стабилизация
        if TT > d:
            volt += 0.002
        elif TT < d:
            volt -= 0.002
        elif TT == d:
            volt = volt

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
threading.Thread(target=main, daemon=True).start()
input('Press <Enter> to exit.')

main()
TimeTagger.freeTimeTagger(tagger)
