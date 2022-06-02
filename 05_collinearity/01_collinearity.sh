#!/bin/bash
# Validate collinearity of the two genomes

# Global variables
NEW_GENOME="$1"
OLD_GENOME="$2"
FOLDER="05_collinearity"

# Align genomes with minimap
time minimap2 -t20 -x asm5 -o "$FOLDER"/correspondance.paf "$NEW_GENOME" "$OLD_GENOME"

# Plot collinearity with minidot
minidot "$FOLDER"/correspondance.paf > "$FOLDER"/out.eps && epstopdf "$FOLDER"/out.eps

# Assess what proportion of genome is collinear sections
echo "Number of bases in collinear sections:"
sort -V "$FOLDER"/correspondance.paf | cut -f 3-4 | awk '{print $2-$1}' | awk '$1>100000' | total
