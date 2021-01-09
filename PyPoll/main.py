import os
import csv

csvpath=os.path.join('Resources', 'election_data_copy.csv')

total_votes=0
khan=0
correy=0
li=0
otooley=0

with open(csvpath, 'r', newline='') as file:
	csvreader=csv.reader(file)
	header=next(csvreader)

	for row in csvreader:
	#votes percandidate
		total_votes+=1
		if row[2]=='Khan':
			khan+=1
		elif row[2]=='Correy':
			correy+=1
		elif row[2]=='Li':
			li+=1
		elif row[2]=="O'Tooley":
			otooley+=1

#percents
khanperc=(khan/total_votes)*100
correyperc=(correy/total_votes)*100
liperc=(li/total_votes)*100
otooleyperc=(otooley/total_votes)*100

#dictionary for winner lists
candidates=['Khan','Correy','Li',"O'Tooley"]
votes=[khan,correy,li,otooley]

dictionary=dict(zip(candidates,votes))
key=max(dictionary, key=dictionary.get)

print(f'Results')
print(f'----------------------')
print(f'Total Votes: {total_votes}')
print(f'----------------------')
print(f'Khan: {khanperc:.2f}%, ({khan})')
print(f'Correy: {correyperc:.2f}%,({correy}) ')
print(f'Li: {liperc:.2f}%, ({li}) ')
print(f"O'Tooley: {otooleyperc:.2f}%, ({otooley})")
print(f'----------------------')
print(f'Winner: {key}')

outpath=os.path.join('Analysis','OutputAnalysis.txt')

with open(outpath, 'w') as file:
	file.write('Election Analysis')
	file.write('\n')
	file.write('----------------------')
	file.write('\n')
	file.write(f'Total Votes: {total_votes}')
	file.write('\n')
	file.write('----------------------')
	file.write('\n')
	file.write(f'Khan: {khanperc:.2f}%, ({khan})')
	file.write('\n')
	file.write(f'Correy: {correyperc:.2f}%,({correy}) ')
	file.write('\n')
	file.write(f'Li: {liperc:.2f}%, ({li}) ')
	file.write('\n')
	file.write('----------------------')
	file.write('\n')
	file.write(f'Winner: {key}')
	
