#!/bin/bash
# Validate collinearity of the two genomes

# Global variables
NEW_GENOME="$1"
OLD_GENOME="$2"
NCPUS="$3"
FOLDER="05_collinearity"

# Align genomes with minimap
minimap2 -t"$NCPUS" -x asm10 -o "$FOLDER"/correspondence.paf "$NEW_GENOME" "$OLD_GENOME"

# Plot collinearity with minidot
minidot -m 1000 -i 0.5 -s 10000 -w 1000 -f 11 "$FOLDER"/correspondence.paf > "$FOLDER"/collinearity.eps && epstopdf "$FOLDER"/collinearity.eps

# Assess what proportion of genome is collinear sections
echo
echo "SNPLift: Number of bases in collinear sections:"
sort -V "$FOLDER"/correspondence.paf | cut -f 3-4 | awk '{print $2-$1}' | awk '$1>100000' | total
