#!/bin/bash
# From VCF, extract two first columns with chromosomes and positions

# Global variables
VCF="$1"
SPLIT_BY="$2"

# Extract
grep -v "^#" "$VCF" | cut -f -2 | split -l "$SPLIT_BY" -a 2 -d - 06_liftover/positions.

# Rename
ls -1 06_liftover/positions.* | grep -P "\.\d{2,}" |
    while read i
    do
        mv "$i" "$i".ids
    done
