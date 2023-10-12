import pyvisa
import time
import threading
from ThorlabsPM100 import ThorlabsPM100

rm = pyvisa.ResourceManager()
rm.list_resources()

m = pyvisa.ResourceManager()
inst = rm.open_resource('USB0::0x1313::0x8078::P0008894::INSTR')
power_meter = ThorlabsPM100(inst=inst)

try:
    from MDT_COMMAND_LIB import *
except OSError as ex:
    print("Warning:", ex)
from ctypes import *

#region import dll functions

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

    xVoltage = 0
    yVoltage = 0
    zVoltage = 0


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

# def MDT693BExample(serialNumber):
#     hdl = CommonFunc(serialNumber)
#     print('hdl:', hdl)
#     if (hdl < 0):
#         return
#     Check_X_AXiS(hdl)
#     Check_Y_AXiS(hdl)
#     Check_Z_AXiS(hdl)
#
#     # power_meter.sense.average.count = 10
#     xVoltage = 10
#     result = mdtSetXYZAxisVoltage(hdl, xVoltage, xVoltage, xVoltage)
#     if (result < 0):
#         print("mdtSetXYZAxisVoltage fail ", result)
#     else:
#         print("mdtSetXYZAxisVoltage ", xVoltage, xVoltage, xVoltage)
#
#     result = mdtClose(hdl)
#     if (result == 0):
#         print("mdtClose ", serialNumber)
#     else:
#         print("mdtClose fail", result)
#     # b = power_meter.read
#     # print(b)
#     # I = int(3.4e-6)
#     # g = 1
#     # while True:
#     #     xVoltage += 0.5 * g
#     #     result = mdtSetXYZAxisVoltage(hdl, xVoltage, xVoltage, xVoltage)
#     #     if (result < 0):
#     #         print("mdtSetXYZAxisVoltage fail ", result)
#     #     else:
#     #         print("mdtSetXYZAxisVoltage ", xVoltage, xVoltage, xVoltage)
#     #
#     #     result = mdtClose(hdl)
#     #     if (result == 0):
#     #         print("mdtClose ", serialNumber)
#     #     else:
#     #         print("mdtClose fail", result)
#     #     if int(I) < int(b):
#     #         I = b
#     #         g = 1
#     #     elif int(I) < int(b):
#     #         g = g * (-1)

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


main()
# threading.Thread(target=MDT693BExample, daemon=True).start()
# input('Press <Enter> to exit.')