
# Imports
import csv
import os

# Load CSV file
filepath = "PyBank/Resources/budget_data.csv"  

# Define variables to track the financial data
# Months
totalMonths = 0

# Net total amount of profit/losses for whole period
totalNet = 0

# Changes in profit/losses for whole period, and average
previousProfitLoss = None
changeProfit = 0
averageProfit = 0

# Greatest increase in profits (date and amount) for whole period
greatestMax = 0
greatestMaxMonth = ""

# Greatest decrease in profits (date and amount) for whole period
greatestMin = 0
greatestMinMonth = ""

# Open and read the csv
with open(filepath) as financial_data:
    reader = csv.reader(financial_data)
    # Skip the header row
    header = next(reader)

    # Transfer Data Row in CSV to Python
    for row in reader:
        monthCount = row[0]
        profitLoss = int(row[1])

        # Allow each variable totals to count as data is processed
        totalMonths += 1
        totalNet += profitLoss

         # Calculate difference between months and total the change (will use for average later)
        if previousProfitLoss is not None:
            change = profitLoss - previousProfitLoss
            changeProfit += change
            
            # Find the greatest increase in profit between months
            if change > greatestMax:
                greatestMax = change
                greatestMonth = monthCount

            # Find the greatest decrease in profit between months
            if change < greatestMin:
                greatestMin = change
                greatestMinMonth = monthCount

        # Will loop through to next row and be used as previous month to compare profit/loss
        previousProfitLoss = profitLoss

# Calculate the average net change across the months
averageProfit = float(changeProfit / (totalMonths - 1))

# Generate the output summary (Borrowed From Professor's ChatGPT Version)
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${totalNet}\n"
    f"Average Change: ${averageProfit:.2f}\n"
    f"Greatest Increase in Profits: {greatestMonth} (${greatestMax})\n"
    f"Greatest Decrease in Profits: {greatestMinMonth} (${greatestMin})\n"
)

# Print the output
print(output)

#Where output will be made to
output_file = "PyBank/analysis/budget_analysis_noah.txt"  

# Write the results to a text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
