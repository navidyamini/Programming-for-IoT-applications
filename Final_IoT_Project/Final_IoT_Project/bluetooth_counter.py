import time
import bluetooth

class Bluetooth_Counter(object):
    def __init__(self):
        #for countin the number of bluetooth devices
        self.counter = 0

    def search(self):
        devices = bluetooth.discover_devices(duration=30, lookup_names = True)
        return devices

    def count(self):
        self.counter =+1
        return

if __name__=="__main__":
    bluetooth_counter = Bluetooth_Counter()
    while True:
        results = bluetooth_counter.search()
        if (results!=None):
            for addr, name in results:
                #print the macc address and the name of the device
                print "{0} - {1}".format(addr, name)
                #increse the counter
                bluetooth_counter.count()
        # print the nuumber of devices
        print bluetooth_counter.counter
        time.sleep(60)
        #reset the counter to zero for nexrt time
        bluetooth_counter.counter = 0
