# Program to read employee data and make changes to the formatting to meet company standards
# Written by Matt Taylor
import os
import csv

# Define variables and lists to be used later
new_dob = []
first_name = []
last_name = []
employee_id = []
new_ssn = []
new_state = []

# US State abbreviation dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Set the path for the file we are analysing
boss_path = os.path.join("Resources/employee_data.csv")

# Using the file path open the CSV and read data into a variable
with open(boss_path) as file:
    boss_data = csv.reader(file,delimiter=",")
    next(boss_data,None)

    for row in boss_data:
        # Read the employee data into a list
        employee_id.append(row[0])

        # Split the name into First and Last name
        split_name = row[1].split()
        first_name.append(split_name[0])
        last_name.append(split_name[1])

        # Split the DOB and re-order into different date format
        split_dob = row[2].split("-")
        new_dob.append(str(split_dob[1] + "/" + split_dob[2] + "/" + split_dob[0]))

        # Split the SSN and hide the first 5 digits
        split_ssn = row[3].split("-")
        new_ssn.append("***-**-" + split_ssn[2])

        # Use the dictionary to find the abbreviation for the state
        new_state.append(us_state_abbrev[row[4]])

headers = ["Emp ID", "First Name", "Last Name", "DOB", "SSN","State"]

cleaned_data = zip(employee_id,first_name,last_name,new_dob,new_ssn,new_state)

output_path = os.path.join("analysis/output.csv")

with open(output_path, "w", newline="") as file:
    csvwriter = csv.writer(file,delimiter=",")
    csvwriter.writerow(headers)
    csvwriter.writerows(cleaned_data)