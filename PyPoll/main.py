# Import the necessary dependencies for os.path.join()
import os
import csv

## CHECK VARIABLES
NumVoters = 0
Cand_List = {}
Candidate = ""

# Specify path and file name
# in_filepath = "/C/Rice/Data_Analytics/RICEHOU201906DATA1/HW/03-Python/Instructions/PyPoll/Resources/"
csv_file = os.path.join(".", "election_data.csv")

# Read in the CSV file
with open(csv_file, newline='') as in_csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(in_csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        NumVoters += 1
        Candidate = row[2]
        if Candidate in Cand_List:
            Cand_List[Candidate] += 1
        else:
            Cand_List[Candidate] = 1

Winner = ""
Win_Votes = 0

# Specify the file to write to
csv_file = os.path.join(".", "PyPoll.out")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csv_file, 'w', newline='') as out_csvfile:

    print("Election Result")
    out_csvfile.write("Election Result\n")
    print("----------------------------")
    out_csvfile.write("----------------------------\n")
    out_line = "Total Votes: {:1,d}\n".format(NumVoters)
    print(out_line)
    out_csvfile.write(out_line)
    print("----------------------------")
    out_csvfile.write("----------------------------\n")
    for cand, votes in Cand_List.items():
        out_line = "{}: {:1.3f}% ({:,d})\n".format(cand,(votes/NumVoters)*100,votes)
        print(out_line)
        out_csvfile.write(out_line)
        if votes > Win_Votes:
            Winner = cand
            Win_Votes = votes
    print("----------------------------")
    out_csvfile.write("----------------------------\n")
    out_line = "Winner: {}\n".format(Winner)
    print(out_line)
    out_csvfile.write(out_line)
    print("----------------------------")
    out_csvfile.write("----------------------------\n")    
