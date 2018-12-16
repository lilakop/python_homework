import os
import csv

csvpath = ("/Users/lilitakopyan/PythonStuff/python-challenge/PyBank/budget_data.csv")

months = 0
net_amount = 0
net = []
changes = []
month_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        months = months + 1
        net_amount = int(net_amount) + int(row[1])
        net.append(int(row[1]))
        month_list.append(row[0])
    
    for i in range (months - 1):
        change = int(net[i+1] - net[i])
        changes.append(change)
        average = sum(changes)/(months - 1)
        max_profit = max(changes)
        min_profit = min(changes)

month_list.pop(0)
max_month = month_list[changes.index(max_profit)]
min_month = month_list[changes.index(min_profit)]
    
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${round(net_amount,2)}")
print(f"Average  Change: ${round(average,2)}")
print(f"Greatest Increase in Profits: {max_month} ${round(max_profit,2)}")
print(f"Greatest Decrease in Profits: {min_month} ${round(min_profit,2)}")

with open("/Users/lilitakopyan/PythonStuff/python-challenge/PyBank/output.txt",mode="w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Months: {months}")
    txt_file.write("\n")
    txt_file.write(f"Total: ${round(net_amount,2)}")
    txt_file.write("\n")
    txt_file.write(f"Average  Change: ${round(average,2)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits: {max_month} ${round(max_profit,2)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits: {min_month} ${round(min_profit,2)}")
    