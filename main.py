import csv
from classes import *
from funcs import *

# initialize projects
projects = readProjects("projects.csv")

people = readPeople("people.csv")

for p in projects:
    print(p)

print()

projectNames = {}

for i in range(0, len(projects)):
    name = projects[i].name
    projectNames[name] = i

for p in people:
    encodeChoices(p, projectNames)

for p in people:
    match(p, projects)

for proj in projects:
    print(proj.name)
    for p in people:
        print(p.name, proj.calcWeight(p))
    print()

print()
print("MATCHES:")

for proj in projects:
    proj.printMatches()
