import csv
import os

csvpath = os.path.join('..','..', 'GitHub','UT-MCC-DATA-PT-01-2020-U-C','homework-instructions','03-Python','Instructions','PyPoll','Resources', 'election_data.csv')

with open(csvpath,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    list_dict_poll = []

    for row in csvreader:
        list_dict_poll.append({"Voter ID":row[0],"County":row[1],"Candidate":row[2]})


    list_of_candidates = []
    candidates = []
    for i,candidate_info in enumerate(list_dict_poll):
        candidates = candidate_info['Candidate']
        list_of_candidates.append(candidates)
    unique_candidates_list = set(list_of_candidates)


    total_votes = [0 for i in range(len(unique_candidates_list))]
    max_vote = 0

    for i, candidate in enumerate(list(unique_candidates_list)):
        for dict in list_dict_poll:
            if candidate == dict['Candidate']:
                total_votes[i] = total_votes[i]+1
                if total_votes[i] > max_vote:
                    max_vote = total_votes[i]
                    max_winner = candidate




    print(f'Election Results')
    print(f'Total Votes: {len(list_dict_poll)}')
    for i, candidate in enumerate(list(unique_candidates_list)):
        print(f'{list(unique_candidates_list)[i]}: {round(total_votes[i]/len(list_dict_poll),3)*100}% ({total_votes[i]})')

    print(f'Winner: {max_winner}')

    output_path = os.path.join("PyPoll_output.txt")
    with open (output_path,"w") as written_file:
        written_file.write("Election Results \n")
        written_file.write(f'Total Votes: {len(list_dict_poll)} \n')
        for i, candidate in enumerate(list(unique_candidates_list)):
            written_file.write(f'{list(unique_candidates_list)[i]}: {round(total_votes[i]/len(list_dict_poll),3)*100}% ({total_votes[i]})\n')
        written_file.write(f'Winner: {max_winner}')
