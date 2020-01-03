import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#can be changed

class Pin:
    def __init__ (self, name, number, setup, pwm = False, freq = 50):
        self.name = name
        self.number = number
        self.setup = setup
        GPIO.setup(self.number, self.setup)
        if setup == GPIO.OUT:
            GPIO.output(self.number, GPIO.LOW)

        self.pwm = None
        if pwm:
            self.pwm = GPIO.PWM(number, freq)
            self.pwm.start(0)
    
    def output (self, value):
        if value == 1 or value == GPIO.HIGH or value == True:
            GPIO.output(self.number, GPIO.HIGH)
        elif value == 0 or value == GPIO.LOW or value == False:
            GPIO.output(self.number, GPIO.LOW)
    
    def input (self):
        return GPIO.input(self.number) == 1

Pins = []

def GetPin(name):
    for x in Pins:
        if x.name == name:
            return x

class RGBMatrix:
    def __init__(self, anodes, cathodes):
        self.image = None
        self.anodes = anodes
        self.cathodes = cathodes

    def imagePixel (self):
        pass
    
    def imageInterpret (self):
        pass
    
    def render(self):
        pass

def Exit ():
    for x in Pins:
        if Pins[x].pwm is not None:
            Pins[x].pwm.stop()

    GPIO.cleanup()
