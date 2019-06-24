# Import the necessary dependencies for os.path.join()
import os
import csv

Revenue = 0
NumMonths = 0
Change = 0
SumChange = 0
Grt_Inc_Dec = ["", 0, "", 0]

# Specify path and file name
# csv_file = os.path.join(".", "budget_data.csv")
csv_file = os.path.join(os.sep, "Rice", "Data_Analytics", "RICEHOU201906DATA1", "HW", 
    "03-Python", "Instructions", "PyPoll", "Resources", "election_data.csv")

# Read in the CSV file
with open(csv_file, newline='') as in_csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(in_csvfile, delimiter=',')

    # Skip the header
    next(csvreader, None)

    # Read each row of data after the header
    for row in csvreader:
        # Calculate the number of months
        NumMonths += 1
        # Calculate the total of profit/losses
        Revenue += int(row[1])
        # In the first month there is NO change in value, therefore, no calculation
        if NumMonths > 1:
            # Calculate the change from the previous month
            Change = int(row[1]) - Change
            # Verify if the decrease/increase has been larger than previous months'
            if Change > int(Grt_Inc_Dec[1]):
                Grt_Inc_Dec[0] = row[0]
                Grt_Inc_Dec[1] = Change
            elif Change < int(Grt_Inc_Dec[3]):
                Grt_Inc_Dec[2] = row[0]
                Grt_Inc_Dec[3] = Change
            
            # Require this calculation to provide "Average  Change" 
            SumChange += Change
        # Store this month's change to calculate the change in the next iteration
        Change = int(row[1])  

# Specify the file to write to
csv_file = os.path.join(".", "PyBank.out")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csv_file, 'w', newline='') as out_csvfile:
    
    # First we print on screen then we write to the file
    print("Financial Analysis")
    out_csvfile.write("Financial Analysis\n")
    print("----------------------------")
    out_csvfile.write("----------------------------\n")
    out_line = "Total Months: {:d}\n".format(NumMonths)
    print(out_line)
    out_csvfile.write(out_line)
    out_line = "Total: ${:1,d}\n".format(Revenue)
    print(out_line)
    out_csvfile.write(out_line)
    out_line = "Average Change: ${:1,.2f}\n".format(SumChange/(NumMonths - 1))
    print(out_line)
    out_csvfile.write(out_line)
    out_line = "Greatest Increase in Profits:{} (${:1,.0f})\n".format(Grt_Inc_Dec[0],Grt_Inc_Dec[1])
    print(out_line)
    out_csvfile.write(out_line)
    out_line = "Greatest Decrease in Profits: {} (${:1,.0f})\n".format(Grt_Inc_Dec[2],Grt_Inc_Dec[3])
    print(out_line)
    out_csvfile.write(out_line)
