class HW1Q1():
    def __init__(self):
        self.second = 1
        self.minute = 60
        self.hour = 60*60
        self.day = 60*60*24

    def timeConvert(self, input_seconds):
        numDays = input_seconds/self.day
        numHours = (input_seconds - int(numDays)*self.day)/self.hour
        numMin = (numHours*self.hour - int(numHours)*self.hour)/self.minute
        numSec = (numMin*self.minute - int(numMin)*self.minute)/self.second
        return str(int(numDays))+' Days '+str(int(numHours))+' Hours '+str(int(numMin))+' Minutes '+str(int(numSec))+' Seconds '


time = HW1Q1()
convert = HW1Q1.timeConvert(time, 100000)
print(convert)
