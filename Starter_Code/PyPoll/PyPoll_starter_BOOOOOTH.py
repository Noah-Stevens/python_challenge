# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

filepath = "Resources/election_data.csv"

# Define variables to track the election data
total_votes = 0
vote_dict = {}

# Code ripped 3.2.8
with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        total_votes += 1

        # Track votes
        candidate = row[2]
        if candidate in vote_dict.keys():
            vote_dict[candidate] += 1 # add one to the value
        else:
            vote_dict[candidate] = 1 # initialize with one vote

# Generate the output summary
print(vote_dict)
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

# Print the output
print(output)
