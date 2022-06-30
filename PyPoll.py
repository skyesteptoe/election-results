# Add our dependencies
import csv

import os 

#Assign a variable for the file to load and the path.

file_to_load = 'C:/Users/sstewart4/OneDrive - University of California, Davis/Desktop/Bootcamp/W3_Python/Resources/election_results.csv'


# Assign a variable to save the file to a path
file_to_save = 'C:/Users/sstewart4/OneDrive - University of California, Davis/Desktop/Bootcamp/W3_Python/Analysis/election_analysis.txt'

with open(file_to_load) as election_data:

     file_reader = csv.reader(election_data)
 # Read and print the header row.
     headers = next(file_reader)

     print(headers)



