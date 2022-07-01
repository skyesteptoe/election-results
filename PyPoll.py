# Add our dependencies
import csv

import os 

#Assign a variable for the file to load and the path.

file_to_load = 'C:/Users/sstewart4/OneDrive - University of California, Davis/Desktop/Bootcamp/W3_Python/Resources/election_results.csv'

# Assign a variable to save the file to a path
file_to_save = 'C:/Users/sstewart4/OneDrive - University of California, Davis/Desktop/Bootcamp/W3_Python/Analysis/election_analysis.txt'

#Initialize a total vote count.
total_votes = 0

# Declare candidate options variable.
candidate_options = []

#Declare the empty dictionary for candidate votes.
candidate_votes = {}

# Track the winning candidate, winning vote count, and winning percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.

with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)

     #Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file. 
    for row in file_reader:

        #Add to the total vote count.
        total_votes += 1

        #Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1
    
    #Save results to our text file.
    with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"--------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------\n")
        print(election_results, end="")
        #Save the final vote count to the text file.
        txt_file.write(election_results)

        #Determine the percentage of votes for each candidate by looping through the counts.
        #Iterate through the candidate list.

        for candidate_name in candidate_votes:
            #Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            
            
            # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            #Save the candidate results to our text file.
            txt_file.write(candidate_results)

            #Determine if votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):

            #If true then set winning_count = votes and winning_percent = #vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

        #Print the winning candidates' results to the terminal.
            
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

        #Print the winning candidate's info
        print(winning_candidate_summary)

        #Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)




