# Import the necessary dependencies for os.path.join() and csv files
import os
# Import regular expression module
import re

# Specify path and file name for input and output
in_file = os.path.join(".", "analyze_paragrah.txt")


# Read in the file
with open(in_file, 'r') as infile:

    # Store all of the text inside a variable
     paragraph = infile.read()

