import csv
import os

# Total number of Votes cast

# A complete list of candicates who received votes

# The percentage of votes each candicate won

# Toatl number of votes each candidate won


# The winner of election based on popular votes




# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
    print(election_data)

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
outfile.close()