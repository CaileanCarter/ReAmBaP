from sys import argv

"""
Remove ambiguous base pairs in FASTA files. 
Ideal for tools like Snippy which don't respond well to ambigious base pairs.
Replaces 'R', 'Y', 'W', 'S', 'M', 'K', 'H', 'B', 'D', 'V' with 'N'.

Takes input FASTA file as first positional argument.
Output file as second positional argument.

Author: Cailean Carter
Date modified: 12/03/2021
Affiliation: Quadram Institute
Email: cailean.carter@quadram.ac.uk

"""

def main(in_file: str, out_file: str):
    bases = ['R', 'Y', 'W', 'S', 'M', 'K', 'H', 'B', 'D', 'V']
    valid_base = 'N'

    with open(in_file, 'r') as inf, open(out_file, 'w') as outf:
        outf.write(inf.readlines()[0])
        for line in inf.readlines()[1:]:
            line = line.replace(bases, valid_base)
            outf.write(line)


if __name__ == "__main__":
    if len(argv) == 3:
        main(argv[1], argv[2])
    elif len(argv) > 3:
        raise ValueError("Too many arguments provided, expected 2.")
    else:
        raise ValueError("Too few arguments provided, expected 2")