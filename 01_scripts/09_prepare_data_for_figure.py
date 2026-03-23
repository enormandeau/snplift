#!/usr/bin/env python3
"""Prepare informations from 'transfered_positions.tsv' to produce figure of
the relative positions of transfered SNPs in both genomes.

Usage:
    <program> transfered_positions.tsv output_file
"""

# Modules
from collections import defaultdict
import sys

# Parsing user input
try:
    input_positions = sys.argv[1]
    output_file = sys.argv[2]
except:
    print(__doc__)
    sys.exit(1)

# Functions
def split_chr_name(chrom):
    parts = []
    current = []

    for c in chrom:
        cur_type = c.isnumeric()
 
        if not current:
            current.append(c)
            prev_type = cur_type

        else:
            if cur_type == prev_type:
                current.append(c)
            else:
                part = "".join(current)

                if prev_type:
                    part = int(part)

                parts.append(part)
                prev_type = cur_type
                current = [c]

    # Treat last element
    part = "".join(current)

    if prev_type:
        part = int(part)

    parts.append(part)

    return(parts)

# Collecting chr and position infos
positions = []

# Chromosome info contains: {split_chr_name: [name, max_pos]}
chr1_dict = dict() 
chr2_dict = dict()

# Parse file
with open(input_positions) as infile:
    for line in infile:
        l = line.strip().split("\t")
        if l[:2] == ["Score", "Penalties"]:
            continue

        chr1 = l[2]
        pos1 = int(l[4])
        chr2 = l[5]
        pos2 = int(l[6])
        positions.append([chr1, pos1, chr2, pos2])

        # Curate list 1 of chromosomes with split names for sorting and max position
        if not chr1 in chr1_dict:
            split_name = split_chr_name(chr1)
            chr1_dict[chr1] = [split_name, chr1, pos1]
        else:
            chr1_dict[chr1][2] = max(pos1, chr1_dict[chr1][2])

        # Curate list 2 of chromosomes with split names for sorting and max position
        if not chr2 in chr2_dict:
            split_name = split_chr_name(chr2)
            chr2_dict[chr2] = [split_name, chr2, pos2]
        else:
            chr2_dict[chr2][2] = max(pos2, chr2_dict[chr2][2])

# Order chromosomes
ordered1 = sorted(chr1_dict.values())
ordered2 = sorted(chr2_dict.values())

# Correct pos1 using cumulative position in ordered chromosomes
cumul = 0
corr1 = {}
for o in ordered1:
    corr1[o[1]] = cumul
    cumul += o[2] * 1.2

# Correct pos2 using cumulative position in ordered chromosomes
cumul = 0
corr2 = {}
for o in ordered2:
    corr2[o[1]] = cumul
    cumul += o[2] * 1.2

# Correct positions for figure and write to file
with open(output_file, "wt") as outfile:
    for p in positions:
        chr1, pos1, chr2, pos2 = p
        pos1 += corr1[chr1]
        pos2 += corr2[chr2]
        p = [chr1, str(pos1), chr2, str(pos2)]
        outfile.write("\t".join(p) + "\n")
