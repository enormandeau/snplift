#!/bin/bash
# From VCF, extract two first columns with chromosomes and positions

# Global variables
VCF="$1"
OUTPUT="$2"

# Extract
grep -v "^#" "$VCF" | cut -f -2 > "$OUTPUT"
