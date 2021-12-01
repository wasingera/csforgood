import csv

def readProjects(file):
    pass

def readPeople(file):
    pass

def placePerson(p):
    for c in p.choices:
        if c.isEmptySlot():
            c.assigned.append(p)
            break
        
        compare, i = c.getMinWeight()
        pWeight = c.calcWeight(p)

        if weight > compare[0]:
            old = assigned[i]
            c.assigned[i] = p
            placePerson(temp)
            break
