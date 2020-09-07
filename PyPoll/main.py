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

# Creating the strings to be printed later
khan_print = "Khan: " + str("%.3f" % percent_khan) + "% (" + str(candidate_votes["Khan"]) + ")" 
correy_print = "Correy: " + str("%.3f" % percent_correy) + "% (" + str(candidate_votes["Correy"]) + ")" 
li_print = "Li: " + str("%.3f" % percent_li) + "% (" + str(candidate_votes["Li"]) + ")" 
otooley_print = "O'Tooley: " + str("%.3f" % percent_li) + "% (" + str(candidate_votes["O'Tooley"]) + ")" 

# Outputting summary results to the terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(khan_print)
print(correy_print)
print(li_print)
print(otooley_print)
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Set the path for the output TXT file
output_path = os.path.join("analysis/output.txt")

# Create the TXT file with the summary results
with open(output_path, "w",newline="") as file:
    csvwriter = csv.writer(file,delimiter=",")

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([khan_print])
    csvwriter.writerow([correy_print])
    csvwriter.writerow([li_print])
    csvwriter.writerow([otooley_print])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["----------------------------"])