# Amazon Best Sellers Data Analysis

A small data analysis project using Python and pandas to explore trends in an Amazon best sellers dataset. The goal is to practice data cleaning, transformation, and visualization.

---

## Project Overview

This dataset contains information about best-selling products (titles, authors, price, user ratings, category, etc.). This project performs:
- Data loading and cleaning with pandas
- Basic exploratory data analysis (distributions, group-bys)
- Simple visualizations (histograms, bar plots, scatter plots)
- Saving cleaned data or summary tables for later use

---

## Project Structure

- data/
    - amazon_bestsellers.csv      # raw dataset (keep out of source control if large)
- src/
    - main.py                     # main analysis script
- requirements.txt                # dependency list
- README.md                       # this file
- .gitignore                      # files/folders to ignore
- LICENSE                         # license file

---

## Installation

1. Clone the repository:
   git clone https://github.com/YOURUSERNAME/amazon-bestsellers-analysis.git
   cd amazon-bestsellers-analysis

2. Create and activate a virtual environment:
   python -m venv venv
   On macOS / Linux:
     source venv/bin/activate
   On Windows (PowerShell):
     .\venv\Scripts\Activate.ps1
   On Windows (cmd.exe):
     .\venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

---

## Usage

Run the main script to run the analysis:
python src/main.py

If you use notebooks, open them after activating the venv.

---

## Notes

- If the dataset is large, consider not adding the full CSV to the repo. Instead add a smaller sample or provide a download link in this README.
- Freeze your environment when ready:
  pip freeze > requirements.txt

---

## License

This project is provided under the MIT License. See LICENSE for details.
