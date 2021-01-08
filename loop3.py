import time
import random

while True:
    cpu = str(random.randrange(80,99))
    gpu = str(random.randrange(80, 99))
    ram = str(random.randrange(512, 600))
    print("=============================================================================================================================================================================================================================================================")
    print("           SIM STATUS: ACTIVE")
    print("           ERROR(S): 0")
    print("           OS: Saturn 0.89.152 build 112 ALPHA [NOT PERMITTED FOR USE OUTSIDE OF CONTROLLED LAB]")
    print("           MASTER CODE: false;")
    print("           SIM CORE ALLOCATION: 12 (out of 12)")
    print("           CPU USAGE: " + cpu + "%")
    print("           GPU USAGE: " + gpu + "%")
    print("           RAM USAGE: " + ram + "GB (out of 2048GB)")
    print("           TURBO BOOST: not_active")
    print("           SIM UI: SATURN_v02 CMD")
    print("=============================================================================================================================================================================================================================================================")
    time.sleep(2)
