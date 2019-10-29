class Clock:
    def __init__(self, hour=0, minute=0):
        self._hour = hour
        self._minute = minute

    def time(self):
        hour = self._hour
        minute = self._minute
        if minute < 10: minute = "0"+str(minute)
        else: minute = str(minute)
        return f"{hour}:{minute}"

    def toAmPm(self):
        hour = self._hour
        minute = self._minute
        isAM = hour in range(0,12)
        if minute < 10: minute = "0"+str(minute)
        else: minute = str(minute)
        if hour == 0: hour = 12
        elif hour > 12: hour -= 12
        return f"{hour}:{minute} " + ("AM" if isAM else "PM")

    def getMinute(self):
        return self._minute

    def setMinute(self, value):
        if value < 0 or value > 59:
            raise ValueError("Minute out of bounds")
        else: self._minute = value

    minute = property(getMinute,setMinute)

    def addMinute(self, value):
        if value < 0:
            sumMin = self._minute +value
            hourDiff = -1*(sumMin // 60)
            minRem = sumMin % 60
            self.hour = self.hour - hourDiff
            self._minute = minRem
        else:
            sumMin = self._minute+value
            hourDiff = sumMin // 60
            minRem = sumMin % 60
            self.hour = self.hour + hourDiff
            self._minute = minRem

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if value < 0 or value > 23:
            raise ValueError("Hour out of bounds")           
        else: self._hour = value

    def addHour(self, value):
        self._hour = (self._hour + value) % 24

    

if __name__ == "__main__":
    clock = Clock(19,1)
    print(clock.toAmPm(), clock.time())
    # our getters
    print("Get hour:", clock.hour, "Get minute:", clock.minute)
    # our setters
    clock.hour = 5
    clock.minute = 25
    print(clock.time())
    clock.addMinute(123)
    print(clock.time())
    clock.addMinute(-63)
    print(clock.time())
    try:
        clock.hour = 30
    except ValueError as err:
        print("Error!",err)