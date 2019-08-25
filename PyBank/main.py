# Import modules
import os
import csv

# Set source file path
csvpath = os.path.join("..","budget_data.csv")

# Open the source file

budget = "budget_data.csv"
file = open(budget)

# Read the source file

csvreader = csv.reader(file)

# Write a function that does:
def getstuff(csv):
    months = 0
    total = 0
    maxrev = 0
    minrev = 0
    avgchange = 0
    maxmonth = ""
    minmonth = ""
    lastmonth = None
    changes = []
    for row in csv:
        current_month = row[0]
        current_pnl = int(row[1])
        total += current_pnl
        months += 1
        if lastmonth is not None:
            changes.append(current_pnl-lastmonth)
            current_change = current_pnl-lastmonth
            if current_change > maxrev:
                maxrev = current_change
                maxmonth = current_month
            if current_change < minrev:
                minrev = current_change
                minmonth = current_month

        lastmonth = current_pnl
    avgchange = sum(changes)/len(changes)
    return(months, total, maxrev, minrev, avgchange, maxmonth, minmonth)

## Number of months = months
## Net Profit = total
## Greatest Profit and Month = maxmonth/maxrev
## Greatest Loss and Month = minmonth/minrev
## Average Change = avgchange
## Print the stuff

with open("budget_data.csv") as file:
    csvreader = csv.reader(file, delimiter = ",")
    header = next(csvreader)
    analysis = getstuff(csvreader)

with open("output.txt", "a") as f:
    print("Financial Analysis", file=f)
    print("---------------------------------", file=f)
    print("Total Months: " + str(analysis[0]), file=f)
    print("Total: $" + str(analysis[1]), file=f)
    print("Average Change: $" + str(round(analysis[4],2)), file=f)
    print("Greatest Increase in Profits: " + str(analysis[5]) + " ($"+ str(analysis[2])+")", file=f)
    print("Greatest Decrease in Profits: " + str(analysis[6]) + " ($"+ str(analysis[3])+")", file=f)

print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(analysis[0]))
print("Total: $" + str(analysis[1]))
print("Average Change: $" + str(round(analysis[4],2)))
print("Greatest Increase in Profits: " + str(analysis[5]) + " ($"+ str(analysis[2])+")")
print("Greatest Decrease in Profits: " + str(analysis[6]) + " ($"+ str(analysis[3])+")")

# Set output file path
# Save the stuff to the text file