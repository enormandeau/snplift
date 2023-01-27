#!/usr/bin/env python3
"""Renain on average 1/denominator SNP

Usage:
    <program> input_vcf denominator output_vcf

Note:
    denominator can be a float or an int
"""

# Modules
from random import random
import sys

# Parse user input
try:
    input_vcf = sys.argv[1]
    denominator = float(sys.argv[2])
    output_vcf = sys.argv[3]
except:
    print(__doc__)
    sys.exit(1)

with open(input_vcf) as infile:
    with open(output_vcf, "wt") as outfile:
        for line in infile:

            if line.startswith("#"):
                outfile.write(line)

            elif random() < 1.0/denominator:
                outfile.write(line)
