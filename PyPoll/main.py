
#You will be given a set of poll data called election_data.csv. 
#The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
#Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won

import os
import csv

#Importing cvs file
csvpath = os.path.join("Resources", "election_data.csv")

#Inicialize varibles
total_votes=0
candidate_votes={}
percent = {}
candidates = []
votes = []
winner_votes = 0
winner = ""

#read cvs file
with open(csvpath, encoding='UTF-8') as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    header=next(election_data)
    
    for rows in election_data:
        total_votes+=1
        #Counting votes per candidate iterating in column 2 (Candidate)
        candidate=rows[2]
        if candidate in candidate_votes:
            candidate_votes[candidate]+=1
        else:
            candidate_votes[candidate]=1

#Append results into corresponding lists
for candidate in candidate_votes:
    candidates.append(candidate)
    votes.append(candidate_votes[candidate])

#Calculatinf percentange for each candidate
for i in range(len(candidates)):
    candidate = candidates[i]
    vote_count = votes[i]
    percent[candidate] = (vote_count / total_votes) * 100

    #Comparing to find higher number of votes for the winner
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = candidate


#Printting all results im terminal
print ("Election results")
print(f"Total votes: {total_votes}")
print ( "___________________________________________")
print (f'Percentage per candidate: {percent} ')
print ( "___________________________________________")
print (f'Votes per candidate{candidate_votes}')
print ( "___________________________________________")
print (f'Winner: {winner}')

#Saving into a text file
analysis_output = []
analysis_output.append("Election results")
analysis_output.append(f"Total Votes: {total_votes}")
analysis_output.append("___________________________________________")
analysis_output.append("Percentage per candidate:")
for candidate in percent:
    analysis_output.append(f"{candidate}: {percent[candidate]:.2f}%")
analysis_output.append("___________________________________________")
analysis_output.append("Votes per candidate:")
for candidate in candidate_votes:
    analysis_output.append(f"{candidate}: {candidate_votes[candidate]}")
analysis_output.append("___________________________________________")
analysis_output.append(f"Winner: {winner}")


output_path = os.path.join("Analysis", "PyPoll_analysis.txt")

with open(output_path, 'w') as txtfile:
    for line in analysis_output:
        txtfile.write(line + '\n')
