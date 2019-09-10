#solution for PyBank challenge 

# Import required packages
import csv
import os

file_path= os.path.join("Resources","budget_data.csv")
file_to_output = os.path.join("Output", "budget_data_analysis.txt")

with open(file_path, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    headerrow=next(csvreader)
    #print(headerrow)

    #declaring variables for month count , total and profit/loss total
    month_count=1
    total=0
    pl_change_total=0

    #declare a dictionary to collect the Month name as 'key' and profit/loss change between two consecutive rows
    pl_change={}

    #store the first row of data in the variables before processing for change values
    pl_first=int(next(csvreader)[1])
    total+=pl_first
   
    # for loop to iterate through the csv file and collect the difference between two consecutive rows as change value
    for row in csvreader:
        if int(row[1]) != pl_first:
            pl_second=int(row[1])
            diff=pl_second-pl_first                     #calculate the difference
            pl_first=pl_second
            pl_change.update({row[0]:diff})             #append the key,value pair in dictionary
            pl_change_total+=diff
        month_count+=1                                  #increment the month count
        total+=int(row[1])
        average_change=round(pl_change_total/len(pl_change) ,2)  #calculate the average change
        greatest_increase=max(pl_change)
    
    maximum = max(pl_change, key=pl_change.get)     # Use 'max' for finding max value in the dictionary
    #print(maximum, pl_change[maximum])
    minimum = min(pl_change, key=pl_change.get)     # Use 'min' for finding min value in the dictionary
    #print(minimum, pl_change[minimum])
    
    # Generate Budget data Analysis Output
    output = (
        f"\nFinancial Analysis\n"
        f"-----------------\n"
        f"Total Months : {month_count}\n"
        f"Total : $ {total}\n"
        f"Average Change :$ {average_change}\n"
        f"Greatest Increase in Profits: {maximum} { pl_change[maximum]}\n"
        f"Greatest Decrease in Profits: {minimum} { pl_change[minimum]}")
    print(output)

    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
