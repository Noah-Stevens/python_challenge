# -*- coding: UTF-8 -*-
"""PyBank Financial Analysis Script."""

import csv
import os

# File paths
filepath = "Resources/budget_data.csv"
output_file = "analysis/budget_analysis_Booth.txt"

# Initialize financial data variables
total_months = 0
total_net = 0
previous_profit = None
total_change = 0

max_change = float('-inf')
max_month = ""
min_change = float('inf')
min_month = ""

# Read the CSV file and process data
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip header row

    for row in csvreader:
        month, profit = row[0], int(row[1])
        total_months += 1
        total_net += profit

        # Calculate monthly change if it's not the first row
        if previous_profit is not None:
            change = profit - previous_profit
            total_change += change

            # Update max and min change
            if change > max_change:
                max_change, max_month = change, month
            if change < min_change:
                min_change, min_month = change, month

        previous_profit = profit

# Calculate average change, handling division by zero if necessary
avg_change = total_change / (total_months - 1) if total_months > 1 else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {max_month} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_change})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
