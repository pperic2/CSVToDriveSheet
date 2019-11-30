# CSVtoSheetsHelper

CSVtoSheetsHelper is a set of python scripts to help create, manage, and update Google Sheets with CSV data.


## Prerequisites

Python 3+, which can be installed by running:

```bash
$ sudo apt-get install python3
```


A Google Sheets API Token, which can be obtained from [https://console.developers.google.com/](https://console.developers.google.com/).  The program expects a filename of: 'credentials.json', The 'credentials.json' file should be placed in the same folder as the UpdateCSV.py file.

Tested on Ubuntu 18.04.

## Installation

In a terminal, go to the directory where you want to save the file.


Download the program directly from GitHub, or by running the following in bash:
```bash
$ git clone https://github.com/pperic2/CSVToDriveSheet
```

## Usage

First, make sure you are in the correct directory, which is the AccessDriveSheets directory.

First, the program must have editor access to the Google Sheet it is trying to edit.  The easiest way to do this is to create a new sheet, by running:

```bash
python3 CreateGoogleSheet.py 
```

In a terminal, run one of these two options:

The first option opens up a graphical interface:

```bash
python3 UpdateCSV.py 
```

The second option skips the graphical interface, and is much quicker if you know the project name and Google Sheets URL.  It can also be easily and quickly repeatable:

```bash
python3 UpdateCSV.py -name my-project-name -sheetsurl https://docs.google.com/spreadsheets/d/your_sheets_url_here
```
my-project-name refers to the project name taken from epicollect, for example: https://five.epicollect.net/project/my-project-name/data

The Google Sheets URL refers to a Google Sheet that the program can edit. 

## Contributing
These scripts were made to simplify a common workflow of downloading CSV to Google Sheets, but it's quick and ugly.

Fork or pull request, suggestions welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)
