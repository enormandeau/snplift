#!/bin/bash
# From VCF, extract two first columns with chromosomes and positions

# Global variables
VCF="$1"
NUM_LINES="$2"
NCPUS="$3"

# Extract
./01_scripts/util/split_positions.py "$VCF" "$NUM_LINES" "$NCPUS" "$NUM_NEIGHBOURS"
