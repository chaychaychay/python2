import os
import time
import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

for root, dirs, files in os.walk("."):
    for filename in files:
        randpath1 = "C:/Users/Simulation/Assets/var/results/gr_ui/py/"
        randpath2 = "C:/Users/Simulation/Assets/var/results/gr_ui/py/store/includes/default_en_US/./languages/voiceover/"
        randpath3 = "A:/SIM_ai/char/"
        randpath4 = "Z:/Network/Shared/IO/includes/frontend/"
        randpath5 = "C:/Windows/sysadmin/check/"
        pathrand = random.randrange(1,5)
        if pathrand == 1:
            print(randpath1 + filename)
        elif pathrand == 2:
            print(randpath2 + filename)
        elif pathrand == 3:
            print(randpath3 + filename)
        elif pathrand == 4:
            print(randpath4 + filename)
        elif pathrand ==5:
            print(randpath5 + filename)
        time.sleep(0.5)
        error2 = random.randrange(0,20)
        if error2 == 1:
            simcpu = str(random.randrange(25,99))
            print("Simulation CPU Usage: " + simcpu + "%")
        elif error2 == 2:
            print(f"{bcolors.FAIL}================================================================================================================================================================================================================================{bcolors.ENDC}")
            print("ERROR: SIM not established properly")
            print(f"{bcolors.FAIL}================================================================================================================================================================================================================================{bcolors.ENDC}")
        elif error2 == 3:
            seed = str(random.randrange(11111111111111, 999999999999999999))
            print("Simulation Seed: " + seed )

