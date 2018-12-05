#set modules
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
total_votes = 0
total_khan = 0
total_correy = 0
total_li = 0
total_otooley = 0
election_csv_path = os.path.join('election_data.csv')

#CSV module
with open(election_csv_path, newline="") as csvfile:

	# CSV reader specifies delimiter
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    election_csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csv_reader:
   		total_votes += 1
   		if row[2] == "Khan":
   			total_khan += 1
   		if row[2] == "Correy":
   			total_correy += 1
   		if row[2] == "Li":
   			total_li += 1
   		if row[2] == "O'Tooley":
   			total_otooley += 1
total = [total_khan, total_correy, total_li, total_otooley]
winner = max(total)
print(f"Total votes: {total_votes}")
print(f"Khan:{(total_khan) / (total_votes)} ({total_khan})")
print(f"Correy:{(total_correy) / (total_votes)} ({total_correy})")
print(f"Li:{(total_li) / (total_votes)} ({total_li})")
print(f"O'Tooley:{(total_otooley) / (total_votes)} ({total_otooley})")			
if max(total) == total_khan:	
	print(f'Winner: Khan')
if max(total) == total_correy:	
	print(f'Winner: Correy')
if max(total) == total_li:	
	print(f'Winner: Li')
if max(total) == total_otooley:	
	print(f"Winner: O'Tooley")
#f = open("Poll_Analysis.txt", "wt")
#f.write(f'Poll_Analysis\n')