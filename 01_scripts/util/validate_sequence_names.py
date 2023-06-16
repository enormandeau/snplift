#!/usr/bin/env python3
"""Validate that all sequence names from input file are present in old_genome

Usage:
    <program> names_input names_genome
"""

# Modules
import sys

# Parse user input
try:
    names_input = sys.argv[1]
    names_genome = sys.argv[2]
except:
    print(__doc__)
    sys.exit(1)

# Check presence
list_input = [x.strip() for x in open(names_input).readlines()]
set_genome = set([x.strip() for x in open(names_genome).readlines()])
not_found = []

for name in list_input:
    if name not in set_genome:
        not_found.append(name)

# Report any missing names and exit with an error
if not_found:
    print("\nSNPLift ERROR: Some sequence names from the input file were not found in the old_genome:")

    for n in not_found:
        print(f"  {n}")

    print()
    sys.exit(1)
