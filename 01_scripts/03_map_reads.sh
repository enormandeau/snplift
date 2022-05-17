#!/bin/bash
# Map flanking regions to new genome

# Global variables
GENOME="$1"
POSITIONS="$2"

bwa mem -t 20 "$GENOME" "$POSITIONS" > positions.sam
