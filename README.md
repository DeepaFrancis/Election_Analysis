# Election_Analysis

## Project Overview

A Colorado Board of Elections employee Tom has given th following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received the votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of election based on popular vote.

## Resources
- Data source:election_results.csv
- Software: Python 3.7.6, VS code

## Summary
The analysis of Election shows that:
-There are 369,711 votes cast in the election.
- The candicates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
 - The candidate results were:
      - Charles Casper Stockham received 23% of the votes and 85,213 number of votes
      - Diana DeGette received 73.8% of the votes and 272,893 number of votes
      - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes

-Winner of the Election was Diana DeGette, who received 73.8% of the votes and 272,893 number of votes.

## Challenge Overview
The election commission has requested some additional data to complete the audit.
  - The voter turnout for each county
  - The percentage of votes from each county out of the total count
  - The county with the highest turnout
  
  ![image](https://user-images.githubusercontent.com/89530570/137610454-ab258d87-2f47-4487-bcee-bfc97ebaf7fd.png)
 

## Challenge Summary
The Election commissions requested additional data to complete the audit is obtained.
County Votes:
Jefferson:10.5% (38,855)
Denver:82.8% (306,055)
Arapahoe:6.7% (24,801)

Largest County  Turnout:Denver

This script can be modified for any election. Core data for the archive are state, county and district level election returns for all recent state and federal elections in the United States. The code can be modified to calculate the state or district level election returns. If we have the CSV files for State or district level election results, the code can be modified for finding those results.

Ref: https://guides.library.harvard.edu/c.php?g=310717&p=2072692
