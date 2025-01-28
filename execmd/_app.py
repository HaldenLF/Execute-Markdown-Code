import argparse
from execmd import parse_text
import sys


def app():
    # Command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-h', '--help', type=str, help='options')
    parser.add_argument('-i', '--input', type=str, help='input markdown file')
    parser.add_argument('-o', '--output', type=str, help='output markdown file')
    args = parser.parse_args()
    
    path_in = args.input
    path_out = args.output
    
    # If not input file was given 
    # read from stdin
    if path_in is None:
        md_in = ''
        for line in sys.stdin:
            md_in += line
    # read from file
    else:
        with open(path_in) as fd:
            md_in = fd.read()
    
    md_out = parse_text(md_in)
    
    # if no output file was given 
    # write to stdout
    if path_out is None:
        print(md_out)
    # write to output file
    else:
        with open(path_out, 'w') as fd:
            fd.write(md_out)    