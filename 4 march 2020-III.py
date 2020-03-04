import  pandas as pd
Teams = [
    "Rajasthan Royals",
    "Kings XI Punjab",
    "Chennai Super Kings",
    "Mumbai Indians",
    "Delhi Capitals",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    "Deccan Chargers"
    "Deccan Chargers"
    "Kings XI Punjab",
    "Kings XI Punjab",
    "Mumbai Indians",

]

Years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
Ranks =[2,3,4,1,3,4,1,2,5,4]

iplData = {
    "Team": Teams,
    "Ranks": Ranks,
    "Year" : Years
}
anotheriplTeams = {
    "Team": ["Deccan Chargers", "Kings XI Punjab", "Sunrise Hyderabad"],
    "Ranks":[8,9,5]
}

table1 = pd.DataFrame(iplData)
table2 = pd.DataFrame(anotheriplTeams)

print(" ipl Teams")
print(table1)

print()

print(" One more ipl Team")
print(table2)





table = pd.DataFrame(iplData)
print(table)

print()

print("===Group By teams & ranks===")
groupTeams = table.groupby(Teams)
print(groupTeams.groups) # grouping data by Teams-->
groupRanks = table.groupby(Ranks)
print(groupRanks.groups) # group by Ranks--->

for teamname, grp in groupTeams:
    print(grp)  # printing the group
    print(teamname)  # printing the team Names only from the groupTeams and groupRanks

print("only fetching the group form groups")

print(groupTeams.get_group("Delhi Capitals"))
print(groupTeams.get_group("Mumbai Indians"))