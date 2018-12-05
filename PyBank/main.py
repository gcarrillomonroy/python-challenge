#set modules
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
total_months = 0
total_net_amount = 0
average_change1 = []
initialvalue0 = 0
initialvalue1 = 0
initialvalue2 = 0
finalvalue = 0

budget_csv_path = os.path.join('budget_data.csv')

#CSV module
with open(budget_csv_path, newline="") as csvfile:

	# CSV reader specifies delimiter
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    budget_csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")



    # Read each row of data after the header
    for row in csv_reader:
        total_months += 1
        total_net_amount += int(row[1])
        initialvalue0 = int(row[1])
        #average_change1.append(initialvalue)
        if total_months > 1:
        	initialvalue2 = initialvalue0
        	average_change = (initialvalue2 - initialvalue1)
        	average_change1.append(average_change)
        	initialvalue1 = initialvalue2
        else:
        	initialvalue1 = initialvalue0
        	initialvalue0 = 0
        #average_change += int((range(initialvalue2,1)-range(initialvalue,1)))
        #initialvalue += 1
        #max_value = float(max(row[1]))
        #min_value = float(row[1])
			#if initialvalue > 0:
			#average_change1.append(valuemonth1-valuemonth0)
			#valuemonth0 = valuemonth1
			#initialvalue += 1
print(f"Total months: {total_months}")
print(f"Total:${total_net_amount}")
print(f": {(average_change1)}")
print(f'Avg:$ {sum(average_change1) / (total_months - 1)}')
print(f'Max:$ {max(average_change1)}')
print(f'Min:$ {min(average_change1)}')		        	

f = open("Financial_Analysis.txt", "wt")
f.write(f'Financial Analysis\n')

