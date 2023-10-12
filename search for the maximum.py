import pyvisa
import time
import threading
import numpy
from ThorlabsPM100 import ThorlabsPM100

try:
    from MDT_COMMAND_LIB import *
except OSError as ex:
    print("Warning:", ex)
from ctypes import *

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
rm = pyvisa.ResourceManager()
rm.list_resources()

m = pyvisa.ResourceManager()
inst = rm.open_resource('USB0::0x1313::0x8078::P0008894::INSTR')
power_meter = ThorlabsPM100(inst=inst)

def MDT693BExample(serialNumber):
    hdl = CommonFunc(serialNumber)
    print('hdl:', hdl)
    if (hdl < 0):
        return

    Check_X_AXiS(hdl)
    Check_Y_AXiS(hdl)
    Check_Z_AXiS(hdl)

    s = power_meter.sense.average.count = 10
    # a = power_meter.read // 1e-7
    # print(a)
    # # print(type(a))
    #
    # volt = 10
    # g = 1
    # while True and (volt > 0) and (volt < 100):
    #     # time.sleep(100e-3)
    #     volt += 0.1 * g
    #     mdtSetXYZAxisVoltage(hdl, volt, volt, volt)
    #     b = power_meter.read // 1e-7
    #     c = power_meter.read // 1e-7
    #     if (b / a) != 1:
    #         a = b
    #         if c > a:
    #             volt -= 0.1
    #         elif c < a:
    #             volt += 0.1
    #         elif c == a:
    #             volt = volt
    #     elif (b / a) == 1:
    #         volt = volt
    #         g = 0
    #         if b > a:
    #             volt -= 0.1
    #         elif b < a:
    #             volt += 0.1
    #         elif b == a:
    #             volt = volt
    n = 0
    volt = 0
    mdtSetXYZAxisVoltage(hdl, volt, volt, volt)
    A = numpy.zeros(100)
    for i in range(A.__len__()):
        A[i] = power_meter.read // 1e-7
        volt += 0.1
        mdtSetXYZAxisVoltage(hdl, volt, volt, volt)
    a = max(A)
    print(a)

    volt = 20
    while True and (volt > 0) and (volt < 75):
        # time.sleep(100e-3)

        mdtSetXYZAxisVoltage(hdl, volt, volt, volt)
        b = power_meter.read // 1e-7
        c = power_meter.read // 1e-8
        if c > a:
            volt -= 0.005
        elif c < a:
            volt += 0.005
        elif c == a:
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
