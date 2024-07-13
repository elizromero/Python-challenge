# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

import os
import csv

#Importing cvs file
csvpath = os.path.join("Resources", "budget_data.csv")

#Inicialize varibles
total_months=0
total=0
accumulative_change=0
gr_inc=0
gr_dec=0
prev_line=0

##Date variables as strings
date_inc=''
date_dec=''

#read cvs file
with open(csvpath, encoding='UTF-8') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")
    #Skipping header
    header=next(budget_data)

    for rows in budget_data:
        profit=int(rows[1]) #Indicates column for profit
        total_months+=1 #Counting rows, equal to the total months
        total+=profit #Summarizing profit values every time
        
        if total_months>1: #Starting in second line to compare changes
            change=profit-prev_line #comparing actual line vs previous line
            accumulative_change=accumulative_change+change #summarizing changes between each profit value. This is for av calculation
            if change>gr_inc: #Every time change is greater, it will be saved in the varible gr_inc along with the date of that row
                gr_inc=change
                date_inc=rows[0]
            if change<gr_dec: #Every time change is greater (negative) it will be saved in the varible gr_dec along with the date of that row
                gr_dec=change
                date_dec=rows[0]

        prev_line=profit #Save the current profit value to compare it in the next loop
        
av_change=accumulative_change/(total_months-1) #Formula to calculate average
                
#Printting all results
print ("Financial Analysis")
print ( "___________________________________________")
print (f'Total Months: {total_months} ')
print (f'Total: ${total}')
print (f'Average Change: ${av_change}')
print (f'Greatest Increase in Profits: ${gr_inc} it is on {date_inc}')
print (f'Greatest Decrease in Profits: ${gr_dec} it is on {date_dec}')

#Saving into a text file
analysis_output = [
    "Financial Analysis",
    "___________________________________________",
    f'Total Months: {total_months}',
    f'Total: ${total}',
    f'Average Change: ${av_change}',
    f'Greatest Increase in Profits: ${gr_inc} on {date_inc}',
    f'Greatest Decrease in Profits: ${gr_dec} on {date_dec}'
]

output_path = os.path.join("Analysis", "PyBank_analysis.txt")

with open(output_path, 'w') as txtfile:
    for line in analysis_output:
        txtfile.write(line + '\n')
