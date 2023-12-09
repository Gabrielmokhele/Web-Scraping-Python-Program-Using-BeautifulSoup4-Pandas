# Web-Scraping-Python-Program-Using-BeautifulSoup4-Pandas
This is a web scrapping application used to analyze data from external sources on the web using beautiful soup and pandas.

## Overview

This Python script is designed to scrape data from an HTML table using BeautifulSoup for HTML parsing and Pandas for data manipulation. The targeted HTML file, 'stats SA.html,' contains a table from which data is extracted and stored in a CSV file named 'market.csv.'

## Prerequisites

- Python 3.
- BeautifulSoup
- Pandas

## Installation

Install the required libraries using the following commands:

```
pip install beautifulsoup4
pip install pandas
```

## Installation

- Place the HTML file, 'stats SA.html,' in the same directory as the Python script. or any html file from the web 
- Run the Python script, and it will extract the data from the HTML table and save it in a CSV file named 'market.csv.'

## Libraries Used

- BeautifulSoup: Used for parsing HTML content.
- Pandas: Used for creating and manipulating the DataFrame and exporting data to CSV.

## Steps to import csv file into excel for further analysis
- In Excel, navigate to the "Data" tab in the Excel ribbon at the top.
- Click on "Get Data" or "From Text/CSV" depending on the version used:
- A dialog box will appear. Navigate to the location where your CSV file is saved, select the file, and click "Import."
- Next, the Text Import Wizard will open. Choose the delimiter (usually it's a comma for CSV files) and click "Next."
- In the next step, you can format the columns as needed. Click "Finish" when you're done.
- Decide whether you want to load the data to an existing worksheet or a new worksheet. Click "OK."
- Review the imported data in Excel. You might need to make adjustments, such as formatting cells or column headers.

Once you are satisfied with the imported data, You can begin with the analysis in excel make the necessary changes, adding data and field validations, create graphs pivot tables from the graph or use power BI for a visual dashboard


## Additional notes 
Suppose you would like to scrape data directly from a specific website without saving html file, please see code below:
first you need to also import Requests
```
import requests
```
```
url = "https://www.statssa.gov.za/"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
table = doc.find("table")
print(doc.prettify())
```

## Author
Gabriel Mokhele
