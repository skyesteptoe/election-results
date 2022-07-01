# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = 'C:/Users/sstewart4/OneDrive - University of California, Davis/Desktop/Bootcamp/W3_Python/Resources/election_results.csv'
# Add a variable to save the file to a path.
file_to_save = 'C:/Users/sstewart4/OneDrive - University of California, Davis/Desktop/Bootcamp/W3_Python/Analysis/election_results.txt'

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
candidate_counties = []
candidate_vcounties = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_cvotes = 0
winning_cvote_percentage = 0
winning_county = "" 

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_vcounty = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in candidate_counties:


            # 4b: Add the existing county to the list of counties.
            candidate_counties.append(county_name)


            # 4c: Begin tracking the county's vote count.
            candidate_vcounties[county_name] = 0


        # 5: Add a vote to that county's vote count.
        candidate_vcounties[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in candidate_vcounties:

        # 6b: Retrieve the county vote count.
        cvotes = candidate_vcounties[county_name]

        # 6c: Calculate the percentage of votes for the county.
        cvote_percentage = float(cvotes)/ float(total_votes)*100

    # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
        print(county_results)

            # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

            # 6f: Write an if statement to determine the winning county and get its vote count.
        if (cvotes > winning_cvotes) and (cvote_percentage > winning_cvote_percentage):
            winning_cvotes = cvotes
            winning_cvote_percentage = cvote_percentage
            winning_county = county_name 

        # 7: Print the county with the largest turnout to the terminal.
            winning_county_summary = (
                f"-------------------------------\n"
                f"Largest County Turnout: {winning_county}\n"
                f"-------------------------------\n")
            print(winning_county_summary, end = "")

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
