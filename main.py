# Import modules
import os
import csv

# Set source file path
csvpath = os.path.join("..","election_data.csv")

# Open the source file
election = "election_data.csv"
file = open(election)

# Read the source file
csvreader = csv.reader(file)

# Write a function that does:

Dict = {}
total = 0
next(csvreader)
for row in csvreader:
    if (row[2] in Dict):
        Dict[row[2]]+=1
        total +=1
    else:
        Dict[row[2]]=1
        total +=1

winner = max(Dict, key=Dict.get)
khan = Dict.get("Khan")
khanperc = khan/total*100
li = Dict.get("Li")
liperc = li/total*100
correy = Dict.get("Correy")
correyperc = correy/total*100
tool= Dict.get("O'Tooley")
toolperc = tool/total*100
total

print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total))
print("--------------------------")
print("Khan: {0:.3f}% (".format(khanperc) +str(khan)+")")
print("Tooley: {0:.3f}% (".format(correyperc) +str(correy)+")")
print("Li: {0:.3f}% (".format(liperc)+str(li)+")")
print("O'Tooley: {0:.3f}% (".format(toolperc) +str(tool)+")")
print("--------------------------")
print("Winner: "+winner)
print("--------------------------")

with open("output.txt", "a") as f:
    print("Election Results", file=f)
    print("--------------------------", file=f)
    print("Total Votes: " + str(total), file=f)
    print("--------------------------", file=f)
    print("Khan: {0:.3f}% (".format(khanperc) +str(khan)+")", file=f)
    print("Tooley: {0:.3f}% (".format(correyperc) +str(correy)+")", file=f)
    print("Li: {0:.3f}% (".format(liperc)+str(li)+")", file=f)
    print("O'Tooley: {0:.3f}% (".format(toolperc) +str(tool)+")", file=f)
    print("--------------------------", file=f)
    print("Winner: "+winner, file=f)
    print("--------------------------", file=f)