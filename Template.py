#importing packages
import time
from threading import Thread
import math

import RPi.GPIO as GPIO

import pygame
import tkinter

pygame.init()

print("Running")

#constant variables and setup

Killed = False


GPIO.setmode(GPIO.BOARD)

class Pin:
    def __init__ (self, number, setup, pwm = False, freq = 50):
        self.number = number
        self.setup = setup
        GPIO.setup(self.number, self.setup)

        self.pwm = None
        if pwm:
            self.pwm = GPIO.PWM(number, freq)
            self.pwm.start(0)

Pins = {"RF" : Pin(35, GPIO.OUT),
        "RB" : Pin(33, GPIO.OUT),
        "LF" : Pin(29, GPIO.OUT),
        "LB" : Pin(31, GPIO.OUT),
        "LPWM" : Pin(16, GPIO.OUT, True, 50),
        "RPWM" : Pin(18, GPIO.OUT, True, 50)}

class Wheel:
    def __init__ (self, forward, backward, deadzone = 0.1, speed = False, pwm = None):
        self.forward = forward
        self.backward = backward
        
        self.deadzone = deadzone
        
        self.pwm = None
        if speed:
            self.pwm = pwm

    def outAxis (self, axis):
        
        if axis > 1:
            axis = 1
        elif axis < -1:
            axis = -1
        
        if abs(axis) > self.deadzone:
            if axis > 0:
                GPIO.output(self.forward.number, GPIO.HIGH)
                GPIO.output(self.backward.number, GPIO.LOW)
                if self.pwm is not None:
                    self.pwm.pwm.ChangeDutyCycle(abs(axis) * 100)
            elif axis < 0:
                GPIO.output(self.forward.number, GPIO.LOW)
                GPIO.output(self.backward.number, GPIO.HIGH)
                if self.pwm is not None:
                    self.pwm.pwm.ChangeDutyCycle(abs(axis) * 100)
        else:
            GPIO.output(self.forward.number, GPIO.LOW)
            GPIO.output(self.backward.number, GPIO.LOW)
            if self.pwm is not None:
                self.pwm.pwm.ChangeDutyCycle(0)
        

wheelL = Wheel(Pins["LF"], Pins["LB"], 0.1, True, Pins["LPWM"])
wheelR = Wheel(Pins["RF"], Pins["RB"], 0.1, True, Pins["RPWM"])

Clock = pygame.time.Clock()

Controller = pygame.joystick.Joystick(0)
Controller.init()

class ControllerInputs:
    def __init__ (self):
        self.joy1X = 0   #controller.get_axis()
        self.joy1Y = 1
        self.a = 0

Inputs = ControllerInputs()

#execution

    #runtime variables, functions

locked = False
joy1Event = False

axisL = 0
axisR = 0

def printAxis ():
    global axisR
    global axisL
    
    while (not Killed):
        time.sleep(0.5)
        print ("Left Axis: " + str(round(axisL / 0.01) * 0.01) + "    Right Axis: " + str(round(axisR / 0.01) * 0.01))

try:
    Thread(target=printAxis).start()
    
    while True:
        if Controller.get_button(Inputs.a) == 1:
            locked = True
        else:
            locked = False
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN and locked and controller.get_button(Inputs.a) == 0:
                locked = false
            elif event.type == pygame.JOYAXISMOTION:
                    joy1Event = True

                    #+ left and right reversed sides on joystick
                    a = (-Controller.get_axis(Inputs.joy1X) - (-Controller.get_axis(Inputs.joy1Y))) / 2
                    axisR = -(Controller.get_axis(Inputs.joy1X) + a) / math.sqrt(1/2)

                    b = (-Controller.get_axis(Inputs.joy1Y) - Controller.get_axis(Inputs.joy1X)) / 2
                    axisL = (Controller.get_axis(Inputs.joy1X) + b) / math.sqrt(1/2)
                    
                    if locked:
                        oldAxisL = axisL
                        oldAxisR = axisR

                        if oldAxisL > oldAxisR:
                            axisL = (oldAxisL - oldAxisR) / 2
                            axisR = -(oldAxisL - oldAxisR) / 2
                        elif oldAxisL < oldAxisR:
                            axisR = (oldAxisR - oldAxisL) / 2
                            axisL = -(oldAxisR - oldAxisL) / 2
                    
                    wheelL.outAxis(axisL)
                    wheelR.outAxis(axisR)
        if not joy1Event:
            #print("No Event")
            '''if abs(axisL) > wheelL.deadzone:
                axisL = (abs(axisL) - ((1 / 10) * (Clock.get_time() / 1000))) * (axisL / abs(axisL))
                wheelL.outAxis(axisL)
            else:
                axisL = 0
                wheelL.outAxis(0)
            if abs(axisR) > wheelR.deadzone:
                axisR = (abs(axisR) - ((1 / 10) * (Clock.get_time() / 1000 ))) * (axisR / abs(axisR))
                wheelL.outAxis(axisR)
            else:
                axisR = 0
                wheelR.outAxis(0)'''

        joy1Event = False
        Clock.tick(60)
except KeyboardInterrupt:
    pass
finally:
    print ("Program exited")
    
    Killed = True
    
    pygame.quit()

    for x in Pins:
        if Pins[x].pwm is not None:
            Pins[x].pwm.stop()

    GPIO.cleanup()
