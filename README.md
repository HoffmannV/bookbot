
# bookbot

This is a simple command-line interface (CLI) tool for counting words and alphanumeric characters in a given text. You can provide an input file and optionally specify an output file to save the results. If no output file is specified, the report is printed to the console.

## Features

- Count the number of words in the input text.
- Count the number of alphanumeric characters.
- Optionally provide input and output files for processing.
- If no output file is provided, the result will be displayed in the terminal.

## Usage

The tool accepts the following arguments:

- `-i` or `--ifile`: (Optional) Path to the input file containing the text.
- `-o` or `--ofile`: (Optional) Path to the output file where the report will be saved.

### Command Syntax

```bash
python3 main.py [-i INPUT_FILE] [-o OUTPUT_FILE]
```

### Example Usage

1. **Provide both input and output files:**

```bash
python3 main.py -i input.txt -o output.txt
```

2. **Provide only an input file and print the result to the console:**

```bash
python3 main.py --ifile input.txt
```

### Argument Breakdown:

- `-i` or `--ifile`: Path to the input file.
- `-o` or `--ofile`: (Optional) Path to the output file. If not provided, the result will be printed in the terminal.

## Requirements

- Python 3.x

## Example Output

If you run the tool with an input file, the output will be a report containing:

- The number of words in the input text.
- The number of alphanumeric characters.

Example:

```
--- Begin report of books ---
77986 words found in the document\frankenstein

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
The 'o' character was found 25225 times
The 'i' character was found 24613 times
The 'n' character was found 24367 times
The 's' character was found 21155 times
The 'r' character was found 20818 times
The 'h' character was found 19725 times
The 'd' character was found 16863 times
The 'l' character was found 12739 times
The 'm' character was found 10604 times
The 'u' character was found 10407 times
The 'c' character was found 9243 times
The 'f' character was found 8731 times
The 'y' character was found 7914 times
The 'w' character was found 7638 times
The 'p' character was found 6121 times
The 'g' character was found 5974 times
The 'b' character was found 5026 times
The 'v' character was found 3833 times
The 'k' character was found 1755 times
The 'x' character was found 677 times
The 'j' character was found 504 times
The 'q' character was found 324 times
The 'z' character was found 243 times
--- End report ---
```
