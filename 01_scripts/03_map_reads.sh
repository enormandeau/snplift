#!/bin/bash
# Map flanking regions to new genome

# Global variables
GENOME="$1"
POSITIONS="$2"
NCPUS="$3"

bwa mem -t "$NCPUS" "$GENOME" "$POSITIONS"
