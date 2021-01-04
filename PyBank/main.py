#dependencies
import os
import csv
#set file path
cvspath = os.path.join('Resources','budget_data_copy.csv')
#care
total_months = []
net_profit_loss = []
monthly_profit_change =[]



#open the file
with open(cvspath, 'r', newline='') as file:
	#read the file
	csvreader=csv.reader(file)
	header=next(csvreader)

	for row in csvreader:
		month=row[0]
		total_months.append(month)
		profit_loss=int(row[1])
		net_profit_loss.append(profit_loss)

	for i in range(len(net_profit_loss)-1):
		monthly_profit_change.append(net_profit_loss[i+1]-net_profit_loss[i])

max_increase_profits=max(monthly_profit_change)
max_decrease_losses=min(monthly_profit_change)
max_increase_month=monthly_profit_change.index(max(monthly_profit_change))+1
max_decrease_month=monthly_profit_change.index(min(monthly_profit_change))+1


print(f'Total Months: {len(total_months)}')
print(f'Net P/L: ${sum(net_profit_loss)}')
print(f'Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}')
print(f'Greatest Profit Increase: {total_months[max_increase_month]}(${str(max_increase_profits)})')
print(f'Greatest Profit Decrease: {total_months[max_decrease_month]}(${str(max_decrease_losses)})')

outpath = os.path.join('Analysis','OutputAnalysis.txt')

with open(outpath,'w') as file:
	file.write('Financial Analysis')
	file.write('\n')
	file.write('-------------------')
	file.write('\n')
	file.write(f'Total Months: {len(total_months)}')
	file.write('\n')
	file.write(f'Net P/L: ${sum(net_profit_loss)}')
	file.write('\n')
	file.write(f'Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}')
	file.write('\n')
	file.write(f'Greatest Profit Increase: {total_months[max_increase_month]}(${str(max_increase_profits)})')
	file.write('\n')
	file.write(f'Greatest Profit Decrease: {total_months[max_decrease_month]}(${str(max_decrease_losses)})')