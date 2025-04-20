# Tool Name: Common Keywords Extractor
# Ver.: 1.2.0
# by: Arash Yoosefdoost
# Description: Common Keywords Extractor is a Python script that analyzes BibTeX filse and extracts the most common keywords used across all entries and sort them from the most common. It is especially useful for academic researchers looking to identify major themes and trends in a collection of references.

import bibtexparser
import csv
from collections import Counter

# Open the BibTeX file and parse it with bibtexparser
with open('INPUT.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Create an empty list to store all keywords
keywords_all = []

# Loop through all articles in the BibTeX file
for entry in bib_database.entries:
    # Check if the article has keywords
    if 'keywords' in entry:
        # Split the keywords by semicolon and convert them to lowercase
        keywords = entry['keywords'].lower().split(';')
        # Remove leading and trailing whitespaces from each keyword
        keywords = [k.strip() for k in keywords]
        # Add the keywords to the list of all keywords
        keywords_all.extend(keywords)

# Remove duplicates from the list of all keywords
keywords_all = list(set(keywords_all))

# Count the frequency of each keyword in the BibTeX file
keyword_count = Counter()
for entry in bib_database.entries:
    if 'keywords' in entry:
        # Split the keywords by semicolon and convert them to lowercase
        keywords = entry['keywords'].lower().split(';')
        # Remove leading and trailing whitespaces from each keyword
        keywords = [k.strip() for k in keywords]
        # Update the keyword count
        keyword_count.update(keywords)

# Save the keyword count to a CSV file
with open('Keyword_Count.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Keyword', 'Count'])
    for keyword, count in keyword_count.items():
        writer.writerow([keyword, count])

# Sort the keyword count by frequency and save it to a CSV file
sorted_keyword_count = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)
with open('Keyword_Count_Sorted.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Keyword', 'Count'])
    for keyword, count in sorted_keyword_count:
        writer.writerow([keyword, count])
