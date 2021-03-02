# the data that we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

import time
import os
import csv

#   assign a variable for the file to load and the path.
file_to_load = os.path.join("~Resources", "election_results.csv")

#   assign a variable to save the file to a path.
file_to_save = os.path.join("~Resources", "election_analysis.txt")
total_votes = 0
candidate_votes = 0

candidates_options = list()
candidates_votes = dict()

#
#   open file

#   Python has a way to read and write to a file without needing to use the open() and
#   close() functions every time.
#   We simply replace the open() function with the 'with' statement.
#   The with statement opens the file and ensures proper acquisition or release of any data
#   without having to close the file, to ensure that the data isn't lost or corrupted.
start_time = time.time()

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #   bypass headers
    headers = next(file_reader)

    for row in file_reader:
        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in (candidates_options):
            #   Add it to the list of candidates.
            candidates_options.append(candidate_name)
            #   tally initial vode
            candidates_votes[candidate_name] = 0
        candidates_votes[candidate_name] += 1
        total_votes += 1
#   checking vote tally
# verif = 0
# for value in candidates_votes.values():
#     verif += int(value)
# print(verif)

#   Determine the percentage of votes each candidate got
winning_candidate = ""
winning_count = 0
winning_percentage = 0
for candidate_name in candidates_votes:
    #   get the candidate's vote
    a_candidate_votes = candidates_votes[candidate_name]
    #   percentage of votes received by the candidate
    percent_of_votes = (float(a_candidate_votes)/float(total_votes))*100
    #   print the results: candidate name and percentage of votes
    print(f'{candidate_name}: received {round(percent_of_votes)}% of the vote.')

#   To do:
#   print out the winning candidate, vote count and percentage to terminal.
    print(f'{candidate_name}: {percent_of_votes:1f}% ({a_candidate_votes:,})\n')
#   Determine the winning candidate
    if(a_candidate_votes > winning_count) and (percent_of_votes > winning_percentage):
        winning_candidate = candidate_name
        winning_count = a_candidate_votes
        winning_percentage = percent_of_votes
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
print(winning_candidate_summary)

# print(total_votes)
# print(candidates_votes)
# print(candidates_options)
# print(f'file closed -> {election_data.closed}')

print("--- %s seconds ---" % (time.time() - start_time))
