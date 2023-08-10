import os
import csv

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
print(csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    months = 0
    total = int(0)  
    pandl = []

    for row in csvreader:
        months = int(months) + 1
        total = total + int(row[1]) 
        pandl.append(int(row[1]))


print("")
print("Financial Analysis")
print("------------------")

print(f"Total Months: {months}")
print(f"Total: ${total}")




#print(pandl[1])

avcount = 0
average = []

while avcount < months -1 :
    average.append(pandl[avcount] - pandl[avcount + 1]) 
    
    #print(avcount)
    #print(avcount+1)
    avcount = avcount + 1

change = 0

for i in average:
    change = change + i

change = change / 85
rounded_change = round(change, 2)

print(f"Average Change: ${rounded_change}")

average.sort()
average[0] = average[0] * -1
average[-1] = average[-1] * -1

print(f"Greatest increase in profits: ${average[0]}")
print(f"Greatest decrease in profits: ${average[-1]}")
#print(average)


txtoutput = os.path.join('analysis', 'bankresults.txt')

with open(txtoutput, 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("")
    outfile.write("Financial Analysis\n")
    outfile.write("------------------\n")
    outfile.write(f"Total Months: {months}\n")
    outfile.write(f"Total: ${total}\n")
    outfile.write(f"Average Change: ${rounded_change}\n")
    outfile.write(f"Greatest increase in profits: ${average[0]}\n")
    outfile.write(f"Greatest decrease in profits: ${average[-1]}\n")