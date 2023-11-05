import csv

data = csv.DictReader(open('Resources/election_data.csv'))
my_report = open('Analysis/voting_analysis.txt', 'w')

#initialize values
votes = 0
cands = {}
win_vote = 0

for row in data:
    #calc votes
    votes += 1

    cand = row['Candidate']

    if cand not in cands.keys():
        cands[cand] = 0

    #determine candidates
    cands[cand] += 1


output = f'''
Election Results
-------------------------
Total Votes: {votes:,}
-------------------------
'''

for cand in cands.keys():
    cand_votes = int(cands[cand])

    output += f'{cand}: {cand_votes/votes:.3f}% ({cand_votes})\n'
    
    #determine winner
    if cand_votes > win_vote:
        win_vote = cand_votes
        winner = cand
    
output += f'-------------------------\n'
output += f'Winner: {winner}'

print(output)
my_report.write(output)