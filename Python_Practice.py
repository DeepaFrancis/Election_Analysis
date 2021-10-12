print("Hello world")


counties = ("Arapahoe","Denver","Jefferson")
voting_data = (1212, 122323,4353454)

"""
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})"""

print(counties)
print(voting_data)


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")


"""for county in any : counties()
   
Print("\n")


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print("\n")
for county, voters in counties_dict.items():
    print(county, voters)
"""

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

"""candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)"""

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


