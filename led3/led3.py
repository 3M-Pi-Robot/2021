import pin
import time

def f15():
    # 1 + 5
    pin.Out("LED1",1)
    pin.Out("LED2",0)
    pin.Out("LED3",0)
    pin.Out("LED4",0)
    pin.Out("LED5",1)
    time.sleep(0.5)


def f24():
    # 2 + 4
    pin.Out("LED1",0)
    pin.Out("LED2",1)
    pin.Out("LED3",0)
    pin.Out("LED4",1)
    pin.Out("LED5",0)
    time.sleep(0.5)

def f3():
    # 3
    pin.Out("LED1",0)
    pin.Out("LED2",0)
    pin.Out("LED3",1)
    pin.Out("LED4",0)
    pin.Out("LED5",0)
    time.sleep(0.5)

pin.load("config.json")

for i in range(0,30):
    f15()
    f24()
    f3()
    f24()
    f15

# cleanup
pin.cleanup()
    
