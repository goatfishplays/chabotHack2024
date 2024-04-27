import time


class Time:
    def __init__(self, hours=-1, mins=-1, secs=-1):
        self.secs = secs
        self.mins = mins
        self.hours = hours
        self.reformat()

    def reformat(self):
        self.mins += self.secs // 60
        self.secs %= 60
        self.hours += self.mins // 60
        self.mins %= 60

    def __str__(self):
        return f"{self.hours:02}:{self.mins:02}:{self.secs:02}"


class Node:
    def __init__(self, name, notes, lists, shared, completable=False, completion=0, time=Time()):
        self.name = name
        self.notes = notes
        self.lists = lists
        self.shared = shared
        self.completable = completable
        self.completion = completion
        self.time = time

    def getRelativeTime(self):
        t = time.gmtime()
        hours = self.time.hours - t.tm_hour
        mins = self.time.mins - t.tm_min
        secs = self.time.secs - t.tm_sec
        if secs < 0 and (mins > 0 or hours > 0):
            mins -= 1
            secs += 60
        if mins < 0 and (hours > 0):
            hours -= 1
            mins += 60
        return (hours, mins, secs)

    def setRelativeTime(self, hours, mins, sec):
        t = time.gmtime()
        self.time.hours = t.tm_hour + hours
        self.time.mins = t.tm_min + mins
        self.time.secs = t.tm_sec + sec
        self.time.reformat()


# class TimeNode(Node):
#     def __init__(self, name, notes, lists, shared, completable=False, completed=False, ):
#         super.__init__(name, notes, lists, shared, completable, completed)
#         self.time = time

# def getRelativeTime(self) {
#     return time.localtime()
# }

if __name__ == "__main__":
    a = Node("A Node", "This node is a node", [], shared=False, completable=False, completion=0, time=Time(16, 22, 30))
    print(a.getRelativeTime())
    print(a.time)
    a.setRelativeTime(5, 5, 5)
    print(a.time)
