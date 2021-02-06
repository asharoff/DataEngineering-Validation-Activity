import pandas as pd
import math

file_object = pd.read_csv("data.csv")
CrashesDF = file_object[file_object['Record Type'] == 1]
VehiclesDF = file_object[file_object['Record Type'] == 2]
ParticipantsDF = file_object[file_object['Record Type'] == 3]

b = 0
assertion1_pt1 = 0
assertion1_pt2 = 0

#validate assertion one
for index, row in file_object.iterrows():
    if(math.isnan(row["Serial #"]) and row["Record Type"] == 1):
        assertion1_pt1 = assertion1_pt1 + 1
    else:
        b = b + 1
    if(math.isnan(row["County Code"]) and row["Record Type"] == 1):
        assertion1_pt2 = assertion1_pt2 + 1
    else:
        b = b + 1
print(assertion1_pt1)
print(assertion1_pt2)

#validate assertion two
for index, row in CrashesDF.iterrows():
    if(row["Crash Month"] > 12 or row["Crash Month"] <= 0):
        print("assertion two part 1 failed")
        break
print("assertion two part 1 passed")

for index, row in CrashesDF.iterrows():
    if(row["Crash Day"] > 31 or row["Crash Day"] <= 0):
        print("assertion two part 2 failed")
        break
print("assertion two part 2 passed")

#validate assertion 3
def is_leap_year(year):
    a = 0
    if(year%4 == 0):
        a = 1
    else:
        return 0
    if(year%100 == 0):
        a = 1
    else:
        return 0
    if(year%400 == 0):
        a = 1
    else:
        return 0
    return a

works = 0
for index, row in CrashesDF.iterrows():
    if(row["Crash Month"] == 2 and is_leap_year(row["Crash Year"]) == 0):
        if(row["Crash Day"] == 29):
            works = 1 
        else:
            works = 0
            break
    elif(row["Crash Month"] == 2 and is_leap_year(row["Crash Year"]) == 1):
        if(row["Crash Day"] >28):
            works = 0
            break
    else:
        works = 1

if(works == 0):
    print("assertion 3 part 1 and 2 failed")
else:
    print("assertion 3 part 1 and 2 passed")
