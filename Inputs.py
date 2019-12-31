
#pass in lambda arg: modify and return arg
#ret means retrieved
#   eg Axis(lambda _: boolInterpret(value))
#access axis with Axis.axis()

class Input:
    def eventCheck (self):
        pass

class Axis(Input):
    def __init__ (self, ret_axis, deadzone = 0.1, accuracy = 1000000000): #STILL GOTTA CHANGE TO DIGITS
        self.axis = ret_axis
        self.lastAxis = False
        
        self.deadzone = deadzone
        
        self.ev_stationary = None
        self.ev_move = None
        self.ev_max = None
        self.ev_deadzoned = None
        #MAY ADD SOME MORE EVENTS

    def eventCheck (self):
        if not self.lastAxis != self.axis() and self.ev_move is not None:
            #down
            self.ev_move(self)
        elif self.lastAxis == self.axis() and self.ev_stationary is not None:
            #hold
            self.ev_stationary(self)
            if deadzoned(self) and self.ev_deadzoned is not None:
                self.ev_deadzoned(self)
        if abs(self.axis()) >= 1 and self.ev_max is not None:
            #up
            self.ev_max(self)
        
        self.lastAxis = self.axis()
        
class Button(Input):
    def __init__ (self, ret_pressed):
        self.pressed = ret_pressed
        self.lastPressed = False
        
        self.ev_down = None
        self.ev_hold = None
        self.ev_up = None
        
    def eventCheck (self):
        if not self.lastPressed and self.pressed() and self.ev_down is not None:
            #down
            self.ev_down(self)
        elif self.lastPressed and self.pressed() and self.ev_hold is not None:
            #hold
            self.ev_hold(self)
        elif self.lastPressed and not self.pressed() and self.ev_up is not None:
            #up
            self.ev_up(self)
        
        self.lastPressed = self.pressed()

class Trigger(Axis):
    def __init__ (self):
        pass

class JoyStick(Input):
    def __init__ (self, ret_xAxis, ret_yAxis):
        pass

class JoyHat(Input):
    def __init__ (self, ret_xAxis, ret_yAxis):
        pass

def boolInterpret(value):
    if value == 1 or value == GPIO.HIGH or value == True:
        return True
    elif value == 0 or value == GPIO.LOW or value == False:
        return False

def deadzoned(axis):
    if abs(axis.axis) > axis.deadzone:
        return False
    else:
        return True
def zoneRound(axis):    #axis is mutable (changeable)
    if abs(axis.axis) > axis.deadzone:
        pass
    else:
        axis.axis = 0

def overshot(axis):
    if abs(axis.axis) <= 1:
        return False
    else:
        return True
def overRound(axis):
    if abs(axis.axis) <= 1:
        pass
    else:
        axis.axis = axis.axis / abs(axis.axis)
