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

print("MERGING--------------->\n")

#table3 = pd.merge(table1,table2, on="Team", how="left") # merges records of left matching to the right records, NaN for those if
# match not found in the right table
table3 = pd.merge(table1,table2, on="Team", how="right") # merges right tables record matching to the records in left table
#table3 = pd.merge(table1,table2, on="Team", how="inner")# merges records which are common to both
table3 = pd.merge(table1,table2, on="Team", how="outer") # merges

print(table3)

