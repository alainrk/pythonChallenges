'''

From: https://www.codewars.com/kata/525f277c7103571f47000147/train/python
The businesspeople among you will know that it's often not easy to find an appointment. In this kata we want to find such an appointment automatically. You will be given the calendars of our businessperson and a duration for the meeting. Your task is to find the earliest time, when every businessperson is free for at least that duration.

Example Schedule:

Person | Meetings
-------+-----------------------------------------------------------
     A | 09:00 - 11:30, 13:30 - 16:00, 16:00 - 17:30, 17:45 - 19:00
     B | 09:15 - 12:00, 14:00 - 16:30, 17:00 - 17:30
     C | 11:30 - 12:15, 15:00 - 16:30, 17:45 - 19:00
Rules:

All times in the calendars will be given in 24h format "hh:mm", the result must also be in that format
A meeting is represented by its start time (inclusively) and end time (exclusively) -> if a meeting takes place from 09:00 - 11:00, the next possible start time would be 11:00
The businesspeople work from 09:00 (inclusively) - 19:00 (exclusively), the appointment must start and end within that range
If the meeting does not fit into the schedules, return null or None as result
The duration of the meeting will be provided as an integer in minutes
Following these rules and looking at the example above the earliest time for a 60 minutes meeting would be 12:15.

'''

class Daytime:
    h, m = 0,0
    def __init__(self, h, m):
        self.h, self.m = h, m

    def __str__(self):
        h = str(self.h) if self.h > 9 else "0"+str(self.h)
        m = str(self.m) if self.m > 9 else "0"+str(self.m)
        return h+":"+m

    def isMin(self, d):
        return self.h < d.h or (self.h == d.h and self.m < d.m)
    def isMinEqual(self, d):
        return self.h < d.h or (self.h == d.h and self.m <= d.m)
    def isMax(self, d):
        return self.h > d.h or (self.h == d.h and self.m > d.m)
    def isMaxEqual(self, d):
        return self.h > d.h or (self.h == d.h and self.m >= d.m)
    def isEqual(self, d):
        return self.h == d.h and self.m == d.m

    def getPlusTime(self, madd):
        h, m = self.h, self.m
        h += madd/60
        madd = madd%60
        totmin = m + madd
        if totmin < 60:
            m = totmin
        else:
            h += 1 # Always just max 1 hour left to add (0 - 119 min)
            m = totmin % 60
        return Daytime(h,m)

class Task:
    start, end = None, None
    def __init__(self, s, e):
        self.start, self.end = s, e

    def __str__(self):
        return str(self.start)+" - "+str(self.end)

    def doesntTouch(self, meeting): # Meeting is a task
        res = (meeting.start.isMin(self.start) and meeting.end.isMinEqual(self.start)) or (meeting.start.isMaxEqual(self.end) and meeting.end.isMax(self.end))
        #print "COMPARING", self, meeting, res
        return res

class Person:
    tasks = [] # List of Task
    def __init__(self, schedule):
        self.tasks = []
        for item in schedule:
            start = tuple(map(lambda x: int(x), item[0].split(":")))
            end = tuple(map(lambda x: int(x), item[1].split(":")))
            self.tasks += [Task(Daytime(start[0], start[1]), Daytime(end[0], end[1]))]

    def __str__(self):
        res = "Person tasks:\n"
        for t in self.tasks:
            res += str(t) + " | "
        return res.strip(" | ")

    def checkAvailability(self, meeting):
        res = True
        for t in self.tasks:
            res = res and t.doesntTouch(meeting)
        return res


def get_start_time(schedules, duration):
    people = []
    for s in schedules:
        people.append(Person(s))
    for p in people:
        print p

    #Bruteforce
    guessStart = Daytime(9,0)
    meeting = Task(guessStart, guessStart.getPlusTime(duration))

    while True:
        okForAll = True
        for p in people:
            okForAll = okForAll and p.checkAvailability(meeting)
        if okForAll:
            print "FINAL MEETING TIME:",guessStart
            return str(guessStart)
        else:
            if meeting.end.isMaxEqual(Daytime(19,0)):
                print "NOT POSSIBLE TO FIND A MEETING TIME",
                return None

        guessStart = guessStart.getPlusTime(1)
        meeting = Task(guessStart, guessStart.getPlusTime(duration))
