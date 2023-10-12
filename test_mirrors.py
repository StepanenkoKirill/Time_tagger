# Подключение зеркала
try:
    from MDT_COMMAND_LIB import *
except OSError as ex:
    print("Warning:", ex)
from ctypes import *

#region import dll functions
import numpy as np
import time
mdtLib = cdll.LoadLibrary(r"C:\Users\A\Mirror\MDT_COMMAND_LIB_x64.dll")

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


##################################################################
C = 1
# Меняем 3 координаты
def MDT693BExample_XYZ(serialNumber):
    hdl = CommonFunc(serialNumber)
    if (hdl < 0):
        return
    Check_X_AXiS(hdl)
    Check_Y_AXiS(hdl)
    Check_Z_AXiS(hdl)

    # xVoltage = 10
    # yVoltage = 0
    # zVoltage = 0

    scan_S = np.arange(8, 20 + 1, 1)
    for b in scan_S:
        xVoltage = scan_S[b]
        yVoltage = scan_S[b]
        zVoltage = scan_S[b]
        result = mdtSetXYZAxisVoltage(hdl, xVoltage, yVoltage, zVoltage)
        if (result < 0):
            print("mdtSetXYZAxisVoltage fail ", result)
        else:
            print("mdtSetXYZAxisVoltage ", xVoltage, yVoltage, zVoltage)
        time.sleep(1)
# Меняем 1 координаты
def MDT693BExample(serialNumber):
    hdl = CommonFunc(serialNumber)
    if (hdl < 0):
        return
    Check_X_AXiS(hdl)
    Check_Y_AXiS(hdl)
    Check_Z_AXiS(hdl)

    # xVoltage = 10
    yVoltage = 0
    zVoltage = 0

    scan_S = np.arange(0, 5 + 1, 1)
    for b in scan_S:
        xVoltage = scan_S[b]
        result = mdtSetXYZAxisVoltage(hdl, xVoltage, yVoltage, zVoltage)
        if (result < 0):
            print("mdtSetXYZAxisVoltage fail ", result)
        else:
            print("mdtSetXYZAxisVoltage ", xVoltage, yVoltage, zVoltage)
        time.sleep(1)

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
               MDT693BExample_XYZ(mdt[0])

    except Exception as ex:
        print("Warning:", ex)
    print("*** End ***")
    input()

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
               MDT693BExample(mdt[0])
               # quit()

    except Exception as ex:
        print("Warning:", ex)
    print("*** End ***")
    # input()
    # exit()


main()