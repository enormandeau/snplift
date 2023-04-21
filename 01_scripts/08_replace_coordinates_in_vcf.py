#!/usr/bin/env python3
"""Replace coordinates in VCF with those from the second genome

Usage:
    <program> input_vcf input_correspondence unique_pos correct_id \
        id_column correct_alleles allele_columns output_vcf
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

    # Put multiple comma-separated alleles in the same order as before
    complement = [x for x in "".join(complement).split(",")][::-1]

    return ",".join(complement)[::-1]

# Parse user input
try:
    input_vcf = sys.argv[1]
    input_correspondence = sys.argv[2]
    unique_pos = sys.argv[3]
    correct_id = sys.argv[4]
    id_column = sys.argv[5]
    correct_alleles = sys.argv[6]
    allele_columns = sys.argv[7]
    output_vcf = sys.argv[8]
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

            # Reverse complement alleles
            if correct_alleles and int(reverse):
                for column in [int(x)-1 for x in allele_columns.strip().split(",")]:
                    l[column] = reverse_complement(l[column])

            new_vcf.append(
                    ((l[0], int(l[1])), l)
                    )

        # Correct VCF
        viewed_positions = set()

        # Sort positions
        for l in sorted(new_vcf):
            new_line = l[1]

            # Correct locus IDs
            if correct_id:
                new_line[int(id_column)-1] = ":".join(new_line[:2])

            # Skip already treated positions
            if unique_pos:
                if new_line[2] in viewed_positions:
                    continue

                else:
                    viewed_positions.add(new_line[2])

            outfile.write("\t".join(new_line) + "\n")
