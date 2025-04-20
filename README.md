# 📊 Custom Bibliometric Analyses Toolkit

**In a Nutshell**

Custom Bibliometric Analyses Toolkit is a modular and powerful workflow for conducting comprehensive **bibliometric and keyword analysis** using BibTeX references. This toolkit could facilitate a structured and reproducible bibliometric analysis, research reviews, and large-scale literature mapping. This lightweight Python-based toolkit consisting of three integrated modules: (1) Common Keywords Extractor, which parses a BibTeX file to identify and rank frequently occurring keywords across all entries; (2) Target Keywords Analyzer, which assesses the presence of user-defined thematic terms within the title, abstract, and keyword fields of each publication; and (3) Sankey Diagram Generator, which visualizes the relationships between articles and their associated thematic keywords using an interactive Sankey diagram. This toolkit enables both exploratory and targeted analysis of research trends, and is particularly suited for mapping domain-specific literature and preparing structured reviews. All components are open-source, modular, and operate on standard bibliographic formats exported from tools such as Zotero or Web of Science.

** How it works**

This toolkit integrates keyword extraction, targeted thematic mapping, and visual network representation of bibliographic records. Its modular system comprises three main tools, each serving a specific analytical function and designed to operate on BibTeX files commonly exported from reference management systems such as Zotero, EndNote, or Web of Science.

  Common Keywords Extractor: This module processes the input .bib file and extracts all keyword fields across entries. It then standardizes the terms (lowercasing, trimming whitespace, etc.) and computes term frequencies. The output consists of two CSV files: one listing all keywords and their counts, and another sorted in descending order of frequency. This step provides a quantitative overview of recurring topics and helps inform the selection of thematic keywords for further analysis.

  Target Keywords Analyzer: Based on a user-defined list of research themes or domain-specific terms, this module evaluates the presence of each term in the title, abstract, and keyword fields of each bibliographic record. The output includes two CSV files: (a) a full report listing each reference, formatted in APA style, along with binary indicators or counts for each target keyword; and (b) a matrix file representing references versus keywords, suitable for visualization. This component enables focused thematic profiling of literature collections and is especially useful for systematic reviews and meta-analyses.

  Sankey Diagram Generator: Using the matrix file generated in the previous step, this script produces an interactive Sankey diagram via the Plotly library. Each flow represents the association between a reference (source) and a target keyword, with optional color customization and configurable visual properties. The resulting diagram supports intuitive exploration of topical patterns and co-occurrence across the literature dataset.

Together, these tools enable a transparent and adaptable pipeline for bibliometric analysis that can be scaled to collections of varying size and complexity. All scripts are open-source and designed to run in any standard Python environment, requiring only lightweight dependencies (bibtexparser, csv, and plotly). The toolkit can be adapted for different fields of study by modifying the target keyword list and input bibliography, making it a valuable resource for both exploratory research and structured academic reviews.

---

## 🔗 Tools Included

1. **Common Keywords Extractor**
2. **Target Keywords Analyzer**
3. **Sankey Diagram Generator**

Each tool can run independently but is most effective when used as part of the pipeline.

---

## 🔄 Full Workflow

### 🔹 Step 1: Keyword Overview  
**Tool:** `Common Keywords Extractor.py`  
- **Input:** BibTeX file  
- **Output:** `Keyword_Count.csv`, `Keyword_Count_Sorted.csv`  
- **Purpose:** Lists all keywords by frequency. Use this to discover dominant themes or define a list of target keywords.

### 🔹 Step 2: Target Keyword Tracking  
**Tool:** `Target Keywords Analyzer.py`  
- **Input:** BibTeX file, predefined keywords  
- **Output:**  
  - `Target-Keywords_Analysis_[Full-Report].csv`  
  - `Target-Keywords_Analysis_[Sankey_Diagram_Data].csv`  
- **Purpose:** Tracks presence of specific keywords across title, abstract, and keyword fields.

### 🔹 Step 3: Visualization  
**Tool:** `Sankey Diagram Generator.py`  
- **Input:** `Target-Keywords_Analysis_[Sankey_Diagram_Data].csv`  
- **Output:** Interactive Sankey diagram  
- **Purpose:** Visualizes which papers map to which keywords, showing topic flows.

---

## 🧠 Example Use Case

1. Run `Common Keywords Extractor.py` to see recurring topics.
2. Choose the most important keywords.
3. Use `Target Keywords Analyzer.py` to trace how those keywords appear across references.
4. Visualize connections using `Sankey Diagram Generator.py`.

---

## 📦 Requirements

Install required packages using:
```bash
pip install bibtexparser plotly
```
