import numpy as np
import pyvisa
import time
import threading
from ThorlabsPM100 import ThorlabsPM100
from datetime import date
from matplotlib import pyplot as plt
import TimeTagger
import warnings
warnings.simplefilter("ignore", UserWarning)
try:
    from MDT_COMMAND_LIB import *
except OSError as ex:
    print("Warning:", ex)

# Заменить путь библиотеки (скопировать из другой программы)
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

def slope_detector(delta_volt, hdl, volt, TT_cur, TT_max, counter) -> bool:
    voltage = volt + delta_volt
    mdtSetXYZAxisVoltage(hdl, voltage, voltage, voltage)
    time.sleep(0.001)
    l = counter.getData()
    if(TT_cur < TT_max):
        if(l[0] > TT_cur):

    if(l[0]-TT_max)/delta_volt < 0:
        return True
    elif(l[0]-TT_max)/delta_volt > 0:
        return False

def plotter(args, func, x_lbl, y_lbl, plot_name: str):
    plt.plot(args, func, 'black', linewidth=0.5)
    plt.xlabel(x_lbl)
    plt.ylabel(y_lbl)
    plt.grid(True)
    plt.savefig(plot_name + str(round(time.time())) + ".png")

def MDT693BExample(serialNumber, tagger, stabilisation_timer_pause = 0, scan_flag = True,
                   make_scanned_plot_flag = False, make_time_counts_plot = False):
    # Check the connectivity
    hdl = CommonFunc(serialNumber)
    print('hdl:', hdl)
    if (hdl < 0):
        return

    # Check piezo-elements
    Check_X_AXiS(hdl)
    Check_Y_AXiS(hdl)
    Check_Z_AXiS(hdl)

    # initialise some vars
    index = 0
    counts_max = 0
    volt_max = 0

    # if we want to scan before stabilisation
    if scan_flag:
        volt = 0
        print('Start voltage: ', volt)
        mdtSetXYZAxisVoltage(hdl, volt, volt, volt)

        N = 10000
        step = 0.01
        voltage_list = []

        mdtSetXYZAxisVoltage(hdl, volt, volt, volt) # setting start distance in the mirror with piezo
        counter = TimeTagger.Counter(tagger=tagger, channels=[1], binwidth=int(1e10), n_values=N) # tagger counter

        for _ in range(N):
            volt += step
            voltage_list.append(round(volt, 3))
            mdtSetXYZAxisVoltage(hdl, volt, volt, volt)

        counter_data = counter.getData()
        counts = counter_data.flatten().tolist().copy()

        # Finding max
        index = counts.index(max(counts))
        counts_max = counts[index]
        volt_max = voltage_list[index]

        # If we want to draw the plot of scanned area
        # Remark: you can find plots in the folder of the current project
        if make_scanned_plot_flag:
            plotter(voltage_list, counts, "Voltage", "Counts in channel", "Resonator")

    else: # if we don't scan and go straight to stabilisation. e.g. we have needed vals in advance
        # Setting max. Values below should be replaced with correct!
        counts_max = 500
        volt_max = 75

    # create new counter and making stabilisation
    new_counter = TimeTagger.Counter(tagger=tagger, channels=[1], binwidth=int(1e10), n_values=1)
    volt = volt_max
    mdtSetXYZAxisVoltage(hdl, volt, volt, volt)

    i = 0
    max_iteration = 1000
    counts_for_plot = {}
    time_stamp = 0.0

    # Plot max_iteration points of new_counter

    while True and (volt > 0) and (volt < 100):
        # Getting new_counter data and plotting if needed
        new_counter_data = new_counter.getData()
        if make_time_counts_plot and i == 0:
            time_stamp = time.time()
        counts_cur = new_counter_data.flatten().tolist()  # for current counts from tagger

        # Plotting the time / counts dependency
        if make_time_counts_plot:
            if i < max_iteration:
                counts_for_plot[i] = ((time.time() - time_stamp), counts_cur[0]) # There is only one number in the list
                                                                                 #  as "nvalue=1" in new_counter
                i += 1
            elif i == max_iteration:
                counts_for_plot_size = len(counts_for_plot)
                x = [counts_for_plot[i][0] for i in range(counts_for_plot_size)]
                y = [counts_for_plot[i][1] for i in range(counts_for_plot_size)]
                plotter(x, y, "Time", "Counts in channel", "Dependency_counts_of_time")
        time.sleep(stabilisation_timer_pause)

        # Stabilisation
        print(f"Maximum counts in channel:  {counts_max}; Current counts value: {counts_cur[0]}")
        relative_counts = counts_cur / counts_max
        if (relative_counts < 0.95) & (relative_counts >= 0.8):
            if not slope_detector(hdl, volt, counts_cur[0], counts_max, new_counter):
                volt += 0.002
            else:
                volt -= 0.002
        elif (relative_counts < 0.8) & (relative_counts >= 0.5):
            if not slope_detector(volt, new_counter):
                volt += 0.01
            else:
                volt -= 0.01
        elif relative_counts < 0.5:
            # Если ниже половины высоты то нужно шагнуть на ширину моды. То есть надо определять ширину моды
            print("Count value is lower than half-height!")
        mdtSetXYZAxisVoltage(hdl, volt, volt, volt)
