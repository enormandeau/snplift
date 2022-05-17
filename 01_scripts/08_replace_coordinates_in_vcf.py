#!/usr/bin/env python3
"""Replace coordinates in VCF with those from the second genome

Usage:
    <program> input_vcf input_correspondence output_vcf
"""

# Modules
from collections import defaultdict
import gzip
import sys

# Defining functions
def myopen(_file, mode="rt"):
    if _file.endswith(".gz"):
        return gzip.open(_file, mode=mode)

    else:
        return open(_file, mode=mode)

# Parse user input
try:
    input_vcf = sys.argv[1]
    input_correspondence = sys.argv[2]
    output_vcf = sys.argv[3]
except:
    print(__doc__)
    sys.exit(1)

# Load correspondence
corr = defaultdict(dict)

with open(input_correspondence, "rt") as infile:
    for line in infile:

        if line.startswith("Score"):
            continue

        l = line.strip().split()
        corr[l[2]][l[4]] = (l[5], l[6])

# Change VCF
with myopen(input_vcf, "rt") as infile:
    with myopen(output_vcf, "wt") as outfile:
        for line in infile:
            if line.startswith("#"):
                outfile.write(line)
                continue

            l = line.strip().split()
            chrom = l[0]
            pos = l[1]

            try:
                new_chrom, new_pos = corr[chrom][pos]
            except:
                continue

            l[0] = new_chrom
            l[1] = new_pos

            outfile.write("\t".join(l) + "\n")
