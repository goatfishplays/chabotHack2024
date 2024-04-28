import time


class Time:
    def __init__(self, hours=-1, mins=-1, secs=-1):
        self.secs = secs
        self.mins = mins
        self.hours = hours
        self.reformat()

    def reformat(self):
        if self.secs >= 60:
            self.mins += self.secs // 60
            self.secs %= 60
        if self.mins >= 60:
            self.hours += self.mins // 60
            self.mins %= 60

    def __str__(self):
        return f"{self.hours:02}:{self.mins:02}:{self.secs:02}"


class Node:
    def __init__(self, name="No Name", notes="No Notes", lists=set(), shared=False, completable=False, completion=0, time=Time()):
        self.name = name
        self.notes = notes
        self.lists = lists if len(lists) > 0 else set()
        self.shared = shared
        self.completable = completable
        self.completion = completion
        self.time = time

    def __str__(self):
        return f"{self.name}\t{self.notes}\t{self.lists}\t{self.shared}\t{self.completable}\t{self.completion}\t{self.time}"

    def getRelativeTime(self):
        t = time.localtime()
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
        t = time.localtime()
        self.time.hours = t.tm_hour + hours
        self.time.mins = t.tm_min + mins
        self.time.secs = t.tm_sec + sec
        self.time.reformat()

    def getTimeSecs(self):
        return self.time.secs + self.time.mins * 60 + self.time.hours * 3600


# class TimeNode(Node):
#     def __init__(self, name, notes, lists, shared, completable=False, completed=False, ):
#         super.__init__(name, notes, lists, shared, completable, completed)
#         self.time = time

# def getRelativeTime(self) {
#     return time.localtime()
# }

if __name__ == "__main__":
    t = time.localtime()
    a = Node("A Node", "This node is a node", set(), shared=False, completable=False, completion=0, time=Time(t.tm_hour, t.tm_min, t.tm_sec))
    print(a.getRelativeTime())
    print(a.time)
    a.setRelativeTime(5, 5, 5)
    print(a.getRelativeTime())
    print(a.time)
