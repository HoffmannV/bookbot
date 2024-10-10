# bookbot

This is a simple command-line interface (CLI) tool for counting words and alphanumeric characters in a given text. You can provide an input file and optionally specify an output file to save the results. If no output file is specified, the report is printed to the console.
Features

    Count the number of words in the input text.
    Count the number of alphanumeric characters.
    Optionally provide input and output files for processing.
    If no output file is provided, the result will be displayed in the terminal.

Usage

The tool accepts the following arguments:

    -i or --ifile: (Optional) Path to the input file containing the text.
    -o or --ofile: (Optional) Path to the output file where the report will be saved.

Command Syntax

bash

python wordcount.py [-i INPUT_FILE] [-o OUTPUT_FILE]

Example Usage

    Provide both input and output files:

bash

python wordcount.py -i input.txt -o output.txt

    Provide only an input file and print the result to the console:

bash

python wordcount.py --ifile input.txt

    Print the result from direct text input (without files):

bash

python wordcount.py "This is some example text."

Argument Breakdown:

    -i or --ifile: Path to the input file.
    -o or --ofile: (Optional) Path to the output file. If not provided, the result will be printed in the terminal.

Installation

    Clone the repository:

bash

git clone https://github.com/yourusername/word-alphanumeric-counter.git
cd word-alphanumeric-counter

    Run the tool using Python:

bash

python wordcount.py -i input.txt -o output.txt

Requirements

    Python 3.x

Example Output

If you run the tool with an input file, the output will be a report containing:

    The number of words in the input text.
    The number of alphanumeric characters.
