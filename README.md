# WrestlingBracket

A desktop application for managing wrestling team rosters and generating match brackets, built with Python and Tkinter.

## Overview

This application allows coaches or tournament organizers to:

- Upload a roster from a CSV file
- Manually enter wrestler data (Name, Weight Class, Record)
- View and edit the roster in an interactive table
- Automatically generate bracket listings grouped by weight class

## Features

- CSV upload for bulk data input
- Manual entry for quick additions
- Interactive table view of the roster
- Bracket generation grouped by weight class
- Easy-to-use tabbed interface

## Requirements

- Python 3.x
- tkinter (included with most Python installations)
- pandas for data handling

## Installation

1. Clone or download this repository.
2. Install required dependencies (if needed):

```bash
pip install pandas
```

## Running the Application

```bash
python outlineExample.py
```

## File Structure

```
outlineExample.py       # Main application script
```

## Usage

1. Open the app.
2. Use the Upload tab to import a CSV or manually add wrestlers.
3. Switch to the Format tab to generate and view brackets.
4. Brackets will be displayed in a popup window grouped by weight class.

## Notes

- The CSV file should include the following columns: Name, Weight Class, Record.
- Brackets are generated as text output for viewing or printing.
