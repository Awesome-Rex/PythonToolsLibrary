import math


#pass in lambda arg: modify and return arg

#ret = retrieved
#ev = event

#   eg Axis(lambda _: boolInterpret(value))

#access axis with Axis.axis()

#event functions are (ent, stay / [ ], exit)

class Input:
    def eventCheck (self):
        pass


class Axis(Input):
    def __init__ (self, ret_axis, deadzone = 0.1, accuracy = 0.000000001): #STILL GOTTA CHANGE TO DIGITS
        self.ret_axis = ret_axis
        self.axis = 0
        self.deadzone = deadzone

        self.last_axis = 0
        
        self.ev_stationary = False
        self.ev_move = False
        self.ev_ent_max = False
        self.ev_ent_deadzoned = False
        #MAY ADD SOME MORE EVENTS

    def eventCheck (self):
        self.ev_stationary = False
        self.ev_move = False
        self.ev_ent_max = False
        self.ev_ent_deadzoned = False
        
        self.axis = zoneRound(self)
        self.axis = overRound(self)        #over round
        
        if self.last_axis != axis:
            #move
            self.ev_move = True
        elif self.last_axis == axis:
            #stationary
            self.ev_stationary = True
        if self.last_axis != axis and abs(axis) >= 1:
            #max
            self.ev_ent_max = True
        if self.axis == 0 and self.lastAxis != axis:
            #let go (in deadzone)
            self.ev_ent_deadzoned = True
        
        self.last_axis = axis

class DTAxis(Input):
    #neg and pos are buttons, mutable
    def __init__(self, neg, pos, defaultDT = 0):
        self.defaultDT = defaultDT
        
        self.neg = neg
        self.pos = pos
        self.axis = 0

        self.last_neg = False
        self.last_pos = False
        self.last_axis = 0
        
        self.ev_ent_changeDir = False
        self.ev_stationary = False
        self.ev_ent_dead = False

    def eventCheck(self):
        self.ev_ent_changeDir = False
        self.ev_stationary = False
        self.ev_ent_dead = False
        
        neg.eventCheck()
        pos.eventCheck()

        if neg.ret_pressed() and pos.ret_pressed():
            self.axis = self.defaultDT
        elif neg.ret_pressed() and not pos.ret_pressed():
            self.axis = -1
        elif not neg.ret_pressed() and pos.ret_pressed():
            self.axis = 1
        elif not neg.ret_pressed() and not pos.ret_pressed:
            self.axis = 0

        #check events here
        if self.last_axis != self.axis:
            self.ev_ent_changeDir = True
        elif self.last_axis == self.axis:
            self.ev_stationary = True
        if self.last_axis != self.axis and self.axis == 0:
            self.ev_ent_dead = True

        self.last_neg = self.neg.ret_pressed()
        self.last_pos = self.pos.ret_pressed()
        self.last_axis = self.axis

class Button(Input):
    def __init__ (self, ret_pressed):   #ret_pressed has to be boolInterpreted
        self.ret_pressed = ret_pressed
        self.lastPressed = False
        
        self.ev_down = False
        self.ev_hold = False
        self.ev_up = False
        
    def eventCheck (self):
        self.ev_down = False
        self.ev_hold = False
        self.ev_up = False
        
        if not self.lastPressed and self.ret_pressed() and self.ev_down is not None:
            #down
            self.ev_down = True
        elif self.lastPressed and self.ret_pressed() and self.ev_hold is not None:
            #hold
            self.ev_hold = True
        elif self.lastPressed and not self.ret_pressed() and self.ev_up is not None:
            #up
            self.ev_up = True
        
        self.lastPressed = self.ret_pressed()

class Trigger(Axis):
    def __init__ (self):
        Axis.__init__(self)

        self.ev_down = False
        self.ev_ent_maxDown = False
        self.ev_exit_maxDown = False
        
        self.ev_up = False
        self.ev_ent_maxUp = False
        self.ev_exit_maxUp = False

    def eventCheck(self):
        lastAxis = Axis.last_axis
        
        self.ev_down = False
        self.ev_ent_maxDown = False
        self.ev_exit_maxDown = False
        
        self.ev_up = False
        self.ev_ent_maxUp = False
        self.ev_exit_maxUp = False
        
        Axis.eventCheck(self)
        
        if Axis.ev_move:
            if Axis.ret_axis() > lastAxis:
                self.ev_down = True
                if Axis.ret_axis() == 1:
                    self.ev_ent_maxDown = True
                if lastAxis == -1:
                    self.ev_exit_maxUp = True
            elif Axis.ret_axis() < lastAxis:
                self.ev_up = True
                if Axis.ret_axis == -1:
                    self.ev_ent_maxUp = True
                if lastAxis == 1:
                    self.ev_exit_maxDown = True
        

class JoyStick(Input):
    def __init__ (self, xAxis, yAxis, deadzone = 0.1, maxzone = 0.1):  #2 Axis mutable objects
        self.xAxis = xAxis
        self.xAxis.deadzone = deadzone
        self.yAxis = yAxis
        self.yAxis.deadzone = deadzone
        
        self.deadzone = deadzone
        self.maxzone = maxzone
        
        self.ev_move = False
        self.ev_stationary = False
        self.ev_deadzoned = False
        
        self.ev_ent_max = False
        self.ev_max = False
        self.ev_exit_max = False
    
    def eventCheck(self):
        lastXAxis = self.xAxis.axis
        lastYAxis = self.yAxis.axis
        
        
        self.ev_move = False
        self.ev_stationary = False
        
        self.ev_ent_deadzoned = False
        self.ev_deadzoned = False
        self.ev_exit_deadzoned = False
        
        self.ev_ent_max = False
        self.ev_max = False
        self.ev_exit_max = False
        
        
        self.xAxis.eventCheck()
        self.yAxis.eventCheck()
        
        
        if self.xAxis.ev_move or self.yAxis.ev_move:
            self.ev_move = True
            
            if self.xAxis.axis == 0 and self.yAxis.axis == 0:
                self.ev_ent_deadzoned = True
            elif lastXAxis == 0 and lastYAxis == 0:
                self.ev_exit_deadzoned = True
                
            if math.hypot(self.xAxis.axis, self.yAxis.axis) > (1 - self.maxzone):
                self.ev_ent_max = True
            if math.hypot(lastXAxis, lastYAxis) > (1 - self.maxzone) and not (math.hypot(self.xAxis.axis, self.yAxis.axis) > (1 - self.maxzone)):
                self.ev_exit_max = True
        elif self.xAxis.ev_stationary and self.yAxis.ev_stationary:
            self.ev_stationary = True
        
        if self.xAxis.axis == 0 and self.yAxis.axis == 0:
            self.ev_deadzoned = True
        if math.hypot(self.xAxis.axis, self.yAxis.axis) > (1 - self.maxzone):
            self.ev_max = True

class JoyHat(Input):
    def __init__ (self, xAxis, yAxis):  #2 DTAxis mutable objects
        self.xAxis = xAxis
        self.yAxis = yAxis
        
        self.ev_change = False
        self.ev_stationary = False
        
        self.ev_ent_dead = False
        self.ev_dead = False
        self.ev_exit_dead = False
    
    def eventCheck (self):
        lastXAxis = self.xAxis.axis
        lastYAxis = self.yAxis.axis
        
        
        self.ev_change = False
        self.ev_stationary = False
        
        self.ev_ent_dead = False
        self.ev_dead = False
        self.ev_exit_dead = False
        
        
        self.xAxis.eventCheck()
        self.yAxis.eventCheck()
        
        
        if self.xAxis.changeDir or self.yAxis.changeDir:
            self.ev_change = True
            
            if self.xAxis.axis == 0 and self.yAxis.axis == 0:
                self.ev_ent_dead = True
            elif lastXAxis == 0 and lastYAxis == 0:
                self.ev_exit_dead = True
        elif self.xAxis.stationary and self.yAxis.stationary:
            self.ev_stationary = True
        
        if self.xAxis.axis == 0 and self.yAxis.axis == 0:
            self.ev_dead = True


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
    if abs(axis.ret_axis()) > axis.deadzone:
        return axis.ret_axis()
    else:
        return 0

def overshot(axis):
    if abs(axis.axis) <= 1:
        return False
    else:
        return True
def overRound(axis):
    if abs(axis.axis) <= 1:
        return axis.axis
    else:
        return axis.axis / abs(axis.axis)
