# Import the necessary dependencies for os.path.join() and csv files
import os
# Import regular expression module
import re

# Specify path and file name for input and output
in_file = os.path.join(".", "analyze_paragrah.txt")

# Initialize variables
Sentences = 0
Words = 0
Letter_Count = 0
Avg_Letter_Count = 0.0
Avg_Word_Count = 0.0

# Read in the file
with open(in_file, 'r') as infile:

    # Store all of the text inside a variable
     paragraph = infile.read()
     parag_list = re.split("(?<=[.!?]) +", paragraph)

     Sentences = len(parag_list)
     for sent in parag_list:
         word_list = re.split("\s", sent)
         Words += len(word_list)
         for word in word_list:
             # Last character is a comma
             if (word[-1:] == ','):
                 Letter_Count += len(word)
             else:
                 Letter_Count += (len(word) -1)
                
             # print(str(Letter_Count))
         
print ("Paragraph Analysis")
print ("---------------")
print(f"Approximate Word Count: {Words}")
print(f"Approximate Sentence Count: {Sentences}")
print(f"Average Letter Count: {Letter_Count/Words}")
print(f"Average Sentence Length: {Words/Sentences}")

             
             


     
     

