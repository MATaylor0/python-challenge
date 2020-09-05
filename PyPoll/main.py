# Program to read polling data and perform analysis
# Written by Matt Taylor
import os
import csv

# Initialising variable and dictionary to be used later
total_votes = 0
candidate_votes = {
    "Khan": 0,
    "Correy": 0,
    "Li": 0,
    "O'Tooley": 0,
}

# Set the path for the file we are analysing
poll_path = os.path.join("Resources/election_data.csv")

with open(poll_path) as file:
    # Store the data from the CSV into a variable and skip the header
    poll_data = csv.reader(file,delimiter=",")
    next(poll_data,None)

    for row in poll_data:
        # Count the total number of rows
        total_votes += 1
        
        # Look at the third column in the dataset and add 1 to the corresponding value in the dictionary
        candidate_votes[row[2]] += 1

# Convert total number of votes to percentages
percent_khan = 100 * candidate_votes["Khan"] / total_votes
percent_correy = 100 * candidate_votes["Correy"] / total_votes
percent_li = 100 * candidate_votes["Li"] / total_votes
percent_otooley = 100 * candidate_votes["O'Tooley"] / total_votes

# Find the key with the maximum value in the dictionary
winner = max(candidate_votes, key=candidate_votes.get)

otooley_print = "O'Tooley: " + str("%.3f" % percent_li) + "% (" + str(candidate_votes["O'Tooley"]) + ")" 

# Outputting summary results to the terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f'Khan: {"%.3f" % percent_khan}% ({candidate_votes["Khan"]})')
print(f'Correy: {"%.3f" % percent_correy}% ({candidate_votes["Correy"]})')
print(f'Li: {"%.3f" % percent_li}% ({candidate_votes["Li"]})')
print(otooley_print)
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Set the path for the output CSV
output_path = os.path.join("analysis/output.csv")

# Create the CSV with the summary results
with open(output_path, "w",newline="") as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=",")

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f'Khan: {"%.3f" % percent_khan}% ({candidate_votes["Khan"]})'])
    csvwriter.writerow([f'Correy: {"%.3f" % percent_correy}% ({candidate_votes["Correy"]})'])
    csvwriter.writerow([f'Li: {"%.3f" % percent_li}% ({candidate_votes["Li"]})'])
    csvwriter.writerow([otooley_print])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["----------------------------"])