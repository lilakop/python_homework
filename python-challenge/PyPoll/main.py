import os
import csv
from operator import itemgetter

csvpath = ("/Users/lilitakopyan/PythonStuff/python-challenge/PyPoll/election_data.csv")


votes = 0
winner_votes = 0
total_candidates = 0
candidate_options = []
candidate_votes = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        votes = votes + 1
        total_candidates = row[2]        

        if row[2] not in candidate_options:
            candidate_options.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
    
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {votes}") 
    print(f"-------------------------")
    for candidate in candidate_votes:
        print(candidate + " " + str(round((candidate_votes[candidate]/votes)*100,4)) + "%" + " (" + str(candidate_votes[candidate]) + ")") 


winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

print(f"-------------------------")
print(f"Winner: "+ str(winner[0]))
print(f"-------------------------")

with open("/Users/lilitakopyan/PythonStuff/python-challenge/PyPoll/output.txt",mode="w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: "+ str(votes))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    for candidate in candidate_votes:
        txt_file.write(candidate + " " + str(round((candidate_votes[candidate]/votes)*100,4)) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    
    