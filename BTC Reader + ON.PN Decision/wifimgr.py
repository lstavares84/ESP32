
import machine #for Pin() function
import time #for sleep() function

rest_time=0.5 #time of blinking

led1 = machine.Pin(21, machine.Pin.OUT) #It was used GPIO 21 to run this test.

led1.off() #When the microcontroller is turned on or restarted, this guarantees that the LED will be in the initial operating stage.

def connect():
    import network
 
    ssid = "LST+NSA.2.4Ghz"
    password =  "Get!040215"
       
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        led1.on()
        time.sleep(2)
        return
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())
