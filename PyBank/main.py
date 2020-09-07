# Program to read financial data of a company and perform analysis
# Written by Matt Taylor
import os
import csv

# Initialising variables to be used later
num_months = 0
total_profit = 0
profit_change = 0
total_change = 0
max_profit = 0
min_profit = 0
x = 0

# Set the path for the file we are analysing
bank_path = os.path.join("Resources/budget_data.csv")

with open(bank_path) as file:
    # Store the data from the CSV into a variable and skip the header
    bank_data = csv.reader(file,delimiter=",")
    next(bank_data,None)

    for row in bank_data:
        # On the first loop, find the profit/loss
        if x == 0:
            previous_profit = int(row[1])
            x += 1
            
        # Total amount of months in the dataset
        num_months += 1

        # Calculate the total profit/loss
        total_profit += int(row[1])

        # Calculate the change in profit/loss
        current_change = int(row[1]) - previous_profit
        total_change += current_change

        # Find the maximum profit
        if current_change > max_profit:
            max_profit = current_change
            max_month = row[0]
        
        # Find the minimum profit
        if current_change < min_profit:
            min_profit = current_change
            min_month = row[0]
        
        # Store the current profit/loss for the next loop
        previous_profit = int(row[1])

average_change = round(total_change/(num_months-1),2)

# Set the path for the output TXT
output_path = os.path.join("analysis/output.txt")

# Create the TXT file with the summary results
with open(output_path, "w",newline="") as file:
    csvwriter = csv.writer(file,delimiter=",")

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {num_months}"])
    csvwriter.writerow([f"Total Profit/Loss: ${total_profit}"])
    csvwriter.writerow([f"Average Change: ${average_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {max_month} (${max_profit})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {min_month} (${min_profit})"])


# Outputting summary results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total Profit/Loss: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_month} (${min_profit})")