# Text Parser Tool

A simple Python tool for extracting names and dates of birth from a text file and exporting structured outputs.

## Features

- Reads unstructured text input
- Extracts names and dates of birth using regex
- Prints parsed data to the terminal
- Exports structured CSV data
- Generates a formatted TXT report
- Flags invalid lines

## Example Input

Robert Sanchez 18/11/1997  
Reece James 08/12/1999  
Levi Colwill 26/02/2003  
Chelsea Mascot

## Example Output

### Names

Robert Sanchez  
Reece James  
Levi Colwill  

### Dates of Birth

18/11/1997  
08/12/1999  
26/02/2003  

### Invalid Lines

Line 4: Chelsea Mascot

## How to Run

Run the script from the terminal:

```bash
py parser.py input.txt output.csv