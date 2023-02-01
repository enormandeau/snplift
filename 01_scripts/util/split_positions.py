#!/usr/bin/env python3
"""Split positions from a VCF into num_cpus files.

Each file contains some lines from the end of the previous file
and the beginning of the next file.

Usage:
    <program> input_vcf num_lines ncpus num_neighbours
"""

# Modules
import sys
import os

# Parse user input
try:
    input_vcf = sys.argv[1]
    num_lines = int(sys.argv[2])
    ncpus = int(sys.argv[3])
    num_neighbours = int(sys.argv[4])
except:
    print(__doc__)

# Open output handles
folder = "06_liftover"
stub = "positions."
end = ".ids"

handles = {}

for i in range(ncpus):
    handles[i] = open(os.path.join(folder, stub + str(i).zfill(2) + end), "wt")

# Iterate over VCF and write positions in appropriate files
line_num = 0
lines_per_file = 1 + num_lines // ncpus

with open(input_vcf) as infile:
    for line in infile:
        if line.startswith("#"):
            continue

        l = line.strip().split("\t")
        out_line = "\t".join(l[:2]) + "\n"

        # Write line to proper file
        output_num = line_num // lines_per_file
        handles[output_num].write(out_line)

        # Add first `num_neighbours` lines to previous file
        output_num_prev = (line_num - num_neighbours) // lines_per_file
        if output_num_prev >= 0 and output_num_prev == output_num - 1:
            handles[output_num_prev].write(out_line)

        # Add last `num_neighbours` lines to next file
        output_num_next = (line_num + num_neighbours) // lines_per_file
        if output_num_next < ncpus and output_num_next == output_num + 1:
            handles[output_num_next].write(out_line)

        line_num += 1
