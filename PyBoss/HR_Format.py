# Import the necessary dependencies for os.path.join() and csv files
import os
import csv

# Is it possible to include it instead of copying??? ****
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

# Initialize variables
Emp_Name = []
DOB = []
DOB_str = ""
SSN = ""
State_Abb = ""

# Specify path and file name for input and output
in_csv_file = os.path.join(os.sep, "Rice", "Data_Analytics", "RICEHOU201906DATA1", "HW", 
    "03-Python", "ExtraContent", "Instructions", "PyBoss", "employee_data.csv")
out_csv_file = os.path.join(".", "NEW_employee_data.csv")


# Read in the CSV file and open the out file
with open(in_csv_file, newline='') as infile, open(out_csv_file, "w", newline='') as outfile:
    # csvreader specifies delimiter and variable that holds contents
     csvreader = csv.reader(infile, delimiter=',')
     # cvswriter specifies delimiter and variable that point to file
     csvwriter = csv.writer(outfile, delimiter=',')

    # Skip the header
     next(csvreader, None)
     # Write the header to the new file
     csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    
    # Read each row of data after the header
     for emp_row in csvreader:
         # Get First and Last Name from 2nd attribute
         Emp_Name = emp_row[1].split()
         # Get date of birth (3rd attribute)
         DOB = emp_row[2].split("-")
         DOB_str = DOB[1] + "/" + DOB[2] + "/" + DOB[0]
         # Get the last 3 characters of the SSN (4th attribute)
         SSN = "***-**-" + emp_row[3][-3:]
         # Translate State (5th attribute) into an abbreviation
         State_Abb = us_state_abbrev[emp_row[4]]

         # Now write to the output file
         csvwriter.writerow([emp_row[0],Emp_Name[0],Emp_Name[1],DOB_str,SSN,State_Abb])
