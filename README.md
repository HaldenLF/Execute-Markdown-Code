# Execute-Markdown-Code

## Overview
ExecMD is a command-line tool designed to process and manipulate markdown files. It reads input from a markdown file or standard input, processes the content, and outputs the result to a specified file or standard output.

## Key Features
* Read markdown content from a file or standard input.
* Process the markdown content using custom parsing logic.
* Output the processed content to a file or standard output.

## Installation
1. pip install execmd
2. import in Python interpreter


## Usage
1. Run the main script with the required arguments:
    ```sh
    python _app.py -i input.md -o output.md
    ```
    - `-i` or `--input`: Path to the input markdown file.
    - `-o` or `--output`: Path to the output markdown file.

2. If no input file is specified, the script will read from standard input:
    ```sh
    python _app.py -o output.md
    ```
    You can then type or paste markdown content directly into the terminal.

3. If no output file is specified, the script will print the processed content to standard output:
    ```sh
    python _app.py -i input.md
    ```
