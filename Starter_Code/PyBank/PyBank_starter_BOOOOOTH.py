# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

filepath = "Resources/budget_data.csv"
file_to_output = "analysis/budget_analysis_BOOOOOOOTH.txt"  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

last_month_profit = 0
curr_month_profit = 0
total_change = 0

max_change = 0
max_month = ""
min_change = 0
min_month = ""

# Code ripped 3.2.8
with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        total_months += 1
        total_net += int(row[1])

        # check if first row - skip first row
        if total_months == 1:
            last_month_profit = int(row[1])
        else:
            # get change
            curr_month_profit = int(row[1])
            change = curr_month_profit - last_month_profit
            total_change += change

            # reset
            last_month_profit = curr_month_profit

            # See if the Change is a new "Max" change
            if change > max_change:
                max_change = change
                max_month = row[0]

            # See if the Change is a new "Min" change
            if change < min_change:
                min_change = change
                min_month = row[0]

# Generate the output summary
avg_change = total_change / (total_months - 1)

output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})
"""

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
