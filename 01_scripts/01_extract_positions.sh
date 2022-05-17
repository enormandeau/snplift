#!/bin/bash
# Extract two first columns from VCF

# Input
VCF=$1
OUTPUT=$2

# Extract
grep -v "^#" "$VCF" | cut -f -2 > "$OUTPUT"
