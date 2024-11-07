
# Import
import csv
import os

# Load CSV File
filepath = "Resources/election_data.csv"


# Variables to track Total Votes and Candidates
voteTotal = 0  # Will be used to count total votes
candidateDict = {} # Will make a list of candidates

# Variables for finding winner
winnerCandidate = ""
votesLead = 0

# Make function to create percentages
def percentageCandidate(candidateVote, voteTotal):
    return (candidateVote / voteTotal) * 100

# Open and read the CSV
with open(filepath) as voter_info:
    reader = csv.reader(voter_info)
    # Skip the header row
    header = next(reader)

   # Transfer Data Row in CSV to Python
    for row in reader:
        voteTotal += 1 # Counts the row of the CSV, which is each voter
        candidate = row[2] # Returns candidate voted for in row 3 of CSV

        # Need to make vote for each candidate keep track and count
        if candidate in candidateDict: # Check: Candidate already has votes?
            candidateDict[candidate] += 1 # Add vote to candidate if they do
        else:
            candidateDict[candidate] = 1 # Otherwise, add candidate to be tracked

# Find Percentage of votes for each candidate
for candidate in candidateDict: # Find each candidate in the list
    # Find amount of votes per candidate
    candidateVote = candidateDict[candidate] 
    # Shows percentage of votes for candidate
    votePercentage = percentageCandidate(candidateVote, voteTotal)

    # Find the Winner from previous found data, such as votes per candidate
    if candidateVote > votesLead: # Check if candidate is higher than current leader
        votesLead = candidateVote # If so, replace the lead vote count with candidate's
        winnerCandidate = candidate # Also, replace the name with the new leading Candidate

# Print analysis of election results
output = f"""Election Results
-------------------------
Total Votes: {voteTotal}
-------------------------
{candidate}: {votePercentage:.3f}% ({candidateDict["Charles Casper Stockham"]})
{candidate}: {votePercentage:.3f}% ({candidateDict["Diana DeGette"]})
{candidate}: {votePercentage:.3f}% ({candidateDict["Charles Casper Stockham"]})
-------------------------
Winner: {winnerCandidate}
-------------------------"""

# Print the output
print(output)

# Filepath for output text summary
outputFile = "analysis/election_data_noah.csv"

# Write the results to a text file
with open(outputFile, "w") as txt_file:
    txt_file.write(output)