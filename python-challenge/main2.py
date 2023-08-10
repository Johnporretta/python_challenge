import os
import csv

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
print(csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    tvotes = 0
    charls = "Charles Casper Stockham"
    diana = "Diana DeGette"
    raymon = "Raymon Anthony Doane"

    ccount = 0
    dcount = 0
    rcount = 0

    for row in csvreader:
        tvotes += 1  # Increment total vote count
        if row[2] == charls:
            ccount += 1  # Increment Charles' count
        elif row[2] == diana:
            dcount += 1  # Increment Diana's count
        elif row[2] == raymon:
            rcount += 1  # Increment Raymon's count

    if ccount > dcount and ccount > rcount:
        winner = charls
    elif dcount > ccount and dcount > rcount:
        winner = diana
    else:
        winner = raymon

print("")
print("Election Results")
print('--------------------')
print("Total Votes:", tvotes)
print('--------------------')
print(f"{charls}: {ccount / tvotes * 100:.3f}% ({ccount})")
print(f"{diana}: {dcount / tvotes * 100:.3f}% ({dcount})")
print(f"{raymon}: {rcount / tvotes * 100:.3f}% ({rcount})")
print('--------------------')
print(f"Winnder: {winner}")
print('--------------------')

txtoutput = os.path.join('analysis', 'electionresults.txt')

with open(txtoutput, 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {tvotes}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{charls}: {ccount / tvotes * 100:.3f}% ({ccount})\n")
    outfile.write(f"{diana}: {dcount / tvotes * 100:.3f}% ({dcount})\n")
    outfile.write(f"{raymon}: {rcount / tvotes * 100:.3f}% ({rcount})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------\n")

