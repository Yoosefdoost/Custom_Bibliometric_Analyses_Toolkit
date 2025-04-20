
# 📚 Common Keywords Extractor

**Version:** 1.2.0  
**Author:** Arash Yoosefdoost  

## 🛠️ Overview

Common Keywords Extractor [from BibTeX] is a Python script for analyzing BibTeX files, extracting the most common keywords used across all entries, and sorting them from the most common. It is especially useful for academic researchers looking to identify major themes and trends in a collection of references.

## 🎯 Purpose

The tool helps summarize the thematic content of a bibliography by:
- Identifying frequent keywords
- Providing a clear overview of research topics
- Enabling trend analysis for literature reviews

## 🌟 Features

- Extracts keywords from BibTeX entries
- Cleans and standardizes keywords
- Generates two CSV files:
  - `Keyword_Count.csv` (unsorted)
  - `Keyword_Count_Sorted.csv` (sorted by frequency)

## 📥 Input

A BibTeX file named `INPUT.bib` containing `keywords` fields for each entry.

## 📤 Output

- `Keyword_Count.csv`: Raw list of all keywords and their counts
- `Keyword_Count_Sorted.csv`: Keywords sorted in descending order of frequency

## ⚙️ How It Works

1. Loads the BibTeX file using `bibtexparser`
2. Iterates through all entries with keywords
3. Splits keywords by semicolon, converts to lowercase, strips whitespace
4. Counts frequency using Python's `Counter`
5. Writes results to two CSV files

## 💻 Usage

1. Install the required package:
   ```bash
   pip install bibtexparser
   ```

2. Place your BibTeX file (`INPUT.bib`) in the same folder as the script.

3. Run the script:
   ```bash
   python "Common Keywords.py"
   ```

4. Check `Keyword_Count.csv` and `Keyword_Count_Sorted.csv` for results.

## 📦 Dependencies

- `bibtexparser`
- Standard Python libraries: `csv`, `collections`

## 🧠 Notes

- This script expects keywords to be semicolon-separated.
- Useful for literature review, meta-analysis, or bibliometric studies.