import pyvisa
import time
import threading
import numpy
from ThorlabsPM100 import ThorlabsPM100
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from time import sleep
import TimeTagger
import warnings
import ctypes
from search_for_the_maximum_Tim_Tagger import MDT693BExample
warnings.simplefilter("ignore", UserWarning)
try:
    from MDT_COMMAND_LIB import *
except OSError as ex:
    print("Warning:", ex)

if __name__ == "main":
    mdtLib = ctypes.cdll.LoadLibrary(r"C:\Users\photo\PycharmProjects\Time_tagger\MDT_COMMAND_LIB_x64.dll")
    print("*** MDT device python example ***")
    try:
        devs = mdtListDevices()
        print(devs)
        if (len(devs) <= 0):
            print('There is no devices connected')
            exit()
        tagger = TimeTagger.createTimeTagger()
        for mdt in devs:
            if (mdt[1] == "MDT693B"):
                MDT693BExample(mdt[0], tagger)
        TimeTagger.freeTimeTagger(tagger)
    except Exception as ex:
        print("Warning: ", ex)
    print("*** End ***")
