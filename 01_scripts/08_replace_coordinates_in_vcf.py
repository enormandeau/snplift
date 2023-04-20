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

def reverse_complement(seq):
    complement = []
    comp = dict(zip(list("ACGTacgtN"), list("TGCAtgcaN")))

    for n in seq:
        try:
            complement.append(comp[n])
        except:
            complement.append(n)

    return "".join(complement)[::-1]

# Parse user input
try:
    input_vcf = sys.argv[1]
    input_correspondence = sys.argv[2]
    correct_vcf = sys.argv[3]
    output_vcf = sys.argv[4]
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
        corr[l[2]][l[4]] = (l[5], l[6], l[-1])

# Change VCF
new_vcf = []

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
                new_chrom, new_pos, reverse = corr[chrom][pos]
            except:
                continue

            l[0] = new_chrom
            l[1] = new_pos

            # TODO Reverse complement alleles
            if reverse:
                l[3] = reverse_complement(l[3])
                l[4] = reverse_complement(l[4])

            new_vcf.append(
                    ((l[0], int(l[1])), l)
                    )

        viewed_positions = set()

        for l in sorted(new_vcf):
            new_line = l[1]

            if correct_vcf:
                new_line[2] = ":".join(new_line[:2])

                if new_line[2] in viewed_positions:
                    continue

                else:
                    viewed_positions.add(new_line[2])

            outfile.write("\t".join(new_line) + "\n")
