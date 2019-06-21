# PyPoll
# Import the necessary dependencies for os.path.join()
import os
import csv

## CHECK VARIABLES *******
NumVoters = 0

Revenue = 0
Change = 0
SumChange = 0
Grt_Inc_Dec = ["", 0, "", 0]

# Specify path and file name
# in_filepath = "/C/Rice/Data_Analytics/RICEHOU201906DATA1/HW/03-Python/Instructions/PyPoll/Resources/" ???
csv_file = os.path.join("", "election_data.csv")
# print(csv_file)

# Read in the CSV file
with open(csv_file, newline='') as in_csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(in_csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        NumVoters += 1
        
        Revenue += int(row[1])
        if NumMonths > 1:
            Change = int(row[1]) - Change
            if Change > int(Grt_Inc_Dec[1]):
                Grt_Inc_Dec[0] = row[0]
                Grt_Inc_Dec[1] = Change
            elif Change < int(Grt_Inc_Dec[3]):
                Grt_Inc_Dec[2] = row[0]
                Grt_Inc_Dec[3] = Change

            SumChange += Change
        Change = int(row[1])  

# Specify the file to write to
csv_file = os.path.join("", "PyBank.out")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csv_file, 'w', newline='') as out_csvfile:
    # new line is NOT working ???

    print("Financial Analysis")
    out_csvfile.write("Financial Analysis")
    print("----------------------------")
    out_csvfile.write("----------------------------")
    out_line = "Total Months: {:d}".format(NumMonths)
    print(out_line)
    out_csvfile.write(out_line)
    out_line = "Total: ${:1,d}".format(Revenue)
    print(out_line)
    out_csvfile.write(out_line)
    out_line = "Average Change: ${:1,.2f}".format(SumChange/(NumMonths - 1))
    print(out_line)
    out_csvfile.write(out_line)
    out_line = "Greatest Increase in Profits:{} (${:1,.0f})".format(Grt_Inc_Dec[0],Grt_Inc_Dec[1])
    print(out_line)
    out_csvfile.write(out_line)
    out_line = "Greatest Decrease in Profits: {} (${:1,.0f})".format(Grt_Inc_Dec[2],Grt_Inc_Dec[3])
    print(out_line)
    out_csvfile.write(out_line)