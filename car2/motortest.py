import pin
import time

pin.load("config.json")

pin.Out("IN1",1) # forward
pin.Out("IN2",0)
pin.Out("ENA",1)
time.sleep(5)

pin.Out("IN1",0) # backward
pin.Out("IN2",1)
pin.Out("ENA",1)
time.sleep(5)

pin.Out("ENA",0) # stop
pin.cleanup()
