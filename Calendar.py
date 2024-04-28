import datetime
import NodeList

class Day:
    date : int
    taskList : NodeList.List

    def getList()->NodeList.List:
        return Day.taskList

class Calendar:
    days : Day = []
    month : int
    year : int

    def getDay(date : int) -> Day:
        return Calendar.days[date]
    
    def getListofDay(date : int) -> NodeList.List:
        return Calendar.days[date].getList()