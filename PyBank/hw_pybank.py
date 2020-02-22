import csv
import os

csvpath = os.path.join('budget_data.csv')

with open(csvpath,'r') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    list_budget_dictionary = []

    for row in csvreader:
        list_budget_dictionary.append({"months":row[0],"amounts":row[1]})

total_amount = 0
total_changes = 0
max_amount = 0
min_amount = 0

for i,amount in enumerate(list_budget_dictionary):
    amount_eachmonth= float(amount['amounts'])
    total_amount = int(total_amount + amount_eachmonth)
    if i >0:
        current_change = amount_eachmonth - previous_amount
        total_changes = total_changes + current_change
        previous_amount = amount_eachmonth
    else:
        current_change = 0
        previous_amount = amount_eachmonth
    average_changes = round(total_changes/(len(list_budget_dictionary)-1),2)

    if current_change > max_amount:
        max_amount = int(current_change)
        max_month = amount['months']

    if current_change < min_amount:
        min_amount= int(current_change)
        min_month = amount['months']

print(f'Financial Analysis')
print(f'Total months: {len(list_budget_dictionary)}')
print(f'Total Profit/Loss Amount: ${total_amount}')
print(f'Average changes: ${average_changes}')
print(f'Greatest increase in Profits: {max_month} (${max_amount})')
print(f'Greatest decrease in Profits: {min_month} (${min_amount})')

output_path = os.path.join("PyBank_output.txt")
with open(output_path, "w") as written_file:
    written_file.write(f"Financial Analysis \n")
    written_file.write(f'Total months: {len(list_budget_dictionary)} \n')
    written_file.write(f'Total Profit/Loss Amount: ${total_amount} \n')
    written_file.write(f'Average change: ${average_changes} \n')
    written_file.write(f'Greatest increase in Profits:{max_month} (${max_amount}) \n')
    written_file.write(f'Greatest decrease in Profits:{min_month} (${min_amount})')