# Import the necessary dependencies for os.path.join() and csv files
import os
# Import regular expression module
import re

# Specify path and file name for input and output
in_file = os.path.join(".", "paragraph_2.txt")

# Initialize variables
Sentences = 0
new_sent = ""
Words = 0
new_word = ""
Letter_Count = 0

# Read in the file
with open(in_file, 'r') as infile:

    # Store all of the text inside a variable
     paragraph = infile.read()
     # Separate the paragraph in sentences. A sentence is finished by . ? or ! folowed by a space
     parag_list = re.split("(?<=[.!?]) *", paragraph)
       
     # Calculate how many sentences in the paragraph
     Sentences = len(parag_list) - 1
     
     # Process each sentence
     for sent in parag_list:
        # clean the paragraph from extra new lines
         new_sent = sent.strip("\n")
         # Separate this sentence into a list of words. Each word is separated by a space
         word_list = re.split("\s", new_sent)
         # Calculate the number of words in this sentence
         Words += len(word_list)
         
         # Process each word
         for word in word_list:
             # clean the word from all extra characters like , . () ! ? "
             new_word = word.strip("[(),.!?\"]")
             # Now calculate the lenght of the word (number of characters)
             Letter_Count += len(new_word)

# Initialize variables
Avg_Letter_Count = 0.0
Avg_Word_Count = 0.0

# Print results
print ("Paragraph Analysis")
print ("---------------")
print(f"Approximate Word Count: {Words}")
print(f"Approximate Sentence Count: {Sentences}")
print(f"Average Letter Count: {Letter_Count/Words}")
print(f"Average Sentence Length: {Words/Sentences}")
