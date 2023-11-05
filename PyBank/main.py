import os
import csv

#point to csv path
csvpath = os.path.join('Resources', "budget_data.csv")
my_report = open(os.path.join('Analysis', "budget_anaylsis.txt"),"w")

#initialize values
months = 0
total = 0
total_ch = 0
pre_rev = 0
inc = ["",0]
dec = ["",0]

#read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # read header
    csv_header = next(csvreader)
    # loop through data
    for row in csvreader:
        rev = int(row[1])
        months += 1
        total += rev

        ch = rev - pre_rev
        if pre_rev == 0:
            ch = 0

        total_ch += ch

        if ch > inc[1]:
            inc[0] = row[0]
            inc[1] = ch

        if ch < dec[1]:
            dec[0] = row[0]
            dec[1] = ch  

        pre_rev = rev


       
            
output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months - 1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''

print(output)
my_report.write(output)


            



