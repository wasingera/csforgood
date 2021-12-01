class Project:

    weights = 4

    def __init__(self, name, major=0, seniority=0, leader=0, leaderApp=0, spots=0):
        self.name = name
        self.major = major
        self.seniority = seniority
        self.leader = leader
        self.leaderApp = leaderApp
        self.spots = spots
        self.assigned = []

    # W = SUM( w * x ) / n -- weighted average
    def calcWeight(person):
        s = person.major * major + person.seniority * seniority + person.leader * leader + person.leaderApp * leaderApp
        return s / weights

    def getMinWeight():
        minW = 100000
        minP = 0
        for i in range(0, len(assigned)):
            weight = calcWeight(p)
            if weight < minW:
                minW = weight
                minP = i

        return (minW, i)

    def isEmptySlot():
        if len(assigned) < spots:
            return True
        return False



class Person:
    def __init__(self, name, major, seniority, leader, leaderApp):
        self.name = name
        self.major = major
        self.seniority = seniority
        self.leader = leader
        self.leaderApp = leaderApp
        self.choices = choices
