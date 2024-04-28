import time
import json
from os import listdir


# class Time:
#     def __init__(self, hours=-1, mins=-1, secs=-1):
#         self.secs = secs
#         self.mins = mins
#         self.hours = hours
#         self.reformat()

# def reformat(self):
#     if self.secs >= 60:
#         self.mins += self.secs // 60
#         self.secs %= 60
#     if self.mins >= 60:
#         self.hours += self.mins // 60
#         self.mins %= 60

#     def __str__(self):
#         return f"{self.hours:02}:{self.mins:02}:{self.secs:02}"


class Node:
    def __init__(self, name="No Name", notes="No Notes", lists=set(), shared=False, completable="no", completion=0, time_hour=-1, time_min=-1, time_sec=-1, dateRules=[]):
        self.name = name
        self.notes = notes
        self.lists = lists if len(lists) > 0 else set()
        self.shared = shared
        self.completable = completable
        self.completion = completion
        self.time_hour = time_hour
        self.time_min = time_min
        self.time_sec = time_sec
        self.dateRules = dateRules
        self.reformat_time()

    def updateFile(self):
        with open("./Nodes/" + self.name + ".json", "w") as f:
            data = {
                "name": self.name,
                "notes": self.notes,
                "lists": tuple(self.lists),
                "shared": self.shared,
                "completable": self.completable,
                "completion": self.completion,
                "time_hour": self.time_hour,
                "time_min": self.time_min,
                "time_sec": self.time_sec,
                "dateRules": tuple(self.dateRules),
            }
            json.dump(data, f)

    def reformat_time(self):
        if self.time_sec >= 60:
            self.time_min += self.time_sec // 60
            self.time_sec %= 60
        if self.time_min >= 60:
            self.time_hour += self.time_min // 60
            self.time_min %= 60

    def loadFile(self, name):
        with open("./Nodes/" + name, "r") as rawRead:
            f = json.load(rawRead)
            # print(f)
            self.name = f["name"]
            self.notes = f["notes"]
            self.lists = set(f["lists"])
            self.shared = f["shared"]
            self.completable = f["completable"]
            self.completion = f["completion"]
            self.time_hour = f["time_hour"]
            self.time_min = f["time_min"]
            self.time_sec = f["time_sec"]
            self.dateRules = f["dateRules"]

    def __str__(self):
        return f"Name: {self.name}\nNotes: {self.notes}\nLists: {self.lists}\nShared: {self.shared}\nCompletion Type: {self.completable}\nAmount Completed: {self.completion}\nTime: {self.time_hour}::{self.time_min}::{self.time_sec}\nDate Rules: {self.dateRules}"

    def defaultView(self):

        return f"{self.name}\t{self.readCompletion()}\t{self.readTime()}"

    def readCompletion(self):
        if self.completable == "no":
            return "n/a"
        elif self.completable == "perc":
            return f"{self.completion}%"
        elif self.completable == "amount":
            return f"{self.completion}"

    def readTime(self):
        if self.getTimeSecs() > 0:
            return f"{self.time_hour}::{self.time_min}::{self.time_sec}"
        return "n/a"

    def getRelativeTime(self):
        t = time.localtime()
        hours = self.time_hour - t.tm_hour
        mins = self.time_min - t.tm_min
        secs = self.time_sec - t.tm_sec
        if secs < 0 and (mins > 0 or hours > 0):
            mins -= 1
            secs += 60
        if mins < 0 and (hours > 0):
            hours -= 1
            mins += 60
        return (hours, mins, secs)

    def setRelativeTime(self, hours, mins, secs):
        t = time.localtime()
        self.time_hour = t.tm_hour + hours
        self.time_min = t.tm_min + mins
        self.time_sec = t.tm_sec + secs
        self.reformat_time()

    def getTimeSecs(self):
        return self.time_sec + self.time_min * 60 + self.time_hour * 3600


# class TimeNode(Node):
#     def __init__(self, name, notes, lists, shared, completable=False, completed=False, ):
#         super.__init__(name, notes, lists, shared, completable, completed)
#         self.time = time

# def getRelativeTime(self) {
#     return time.localtime()
# }

if __name__ == "__main__":
    t = time.localtime() # This doesn't do anything

    a = Node("A Node", "This node is a node", set(), shared=False, completable=False, completion=0, time_hour=t.tm_hour, time_min=t.tm_min, time_sec=t.tm_sec)
    print(a.getRelativeTime())
    # print(a.time)
    a.setRelativeTime(5, 5, 5)
    print(a.getRelativeTime())
    # print(a.time)
    for file in listdir("chabotHack2024/Nodes"):
        a.loadFile(file)
        print(a)
