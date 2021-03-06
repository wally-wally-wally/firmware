import threading
import global_vars
from system_monitor import sysMon
from main_task import mainTask
from battery_monitor import batMon

# Shared resources 
# Since we're accessing different pins I don't think locks are needed on GPIO functions 
#import GPIO

#lock = threading.Lock()

# General inits used by both threads
def init():
 #   GPIO.init()
    pass

if __name__ == '__main__':
  #  init()
    global_vars.init()
    sysMon = threading.Thread(target=sysMon)
    batMon = threading.Thread(target=batMon)
    mainTask = threading.Thread(target=mainTask)
       
    sysMon.start()
    mainTask.start()
    batMon.start()

    sysMon.join()
    mainTask.join()
    batMon.join()

