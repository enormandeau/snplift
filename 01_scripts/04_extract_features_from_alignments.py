#!/usr/bin/env python3
"""Get informative features from sam file

Usage:
    <program> input_sam window_length output_file
"""

# Modules
from collections import defaultdict
import string
import gzip
import sys

# Functions
def parse_cigar_string(cigar):
    counts = defaultdict(int)
    n = []
    l = "X"

    for c in cigar:
        if c in string.digits:
            n.append(c)
        elif c in string.ascii_uppercase:
            num = int("".join(n))
            n = []
            counts[c] += num
    
    return (counts["D"], counts["H"], counts["I"], counts["M"], counts["S"])

# Parsing user input:
try:
    input_sam = sys.argv[1]
    window_length = int(sys.argv[2])
    output_file = sys.argv[3]
except:
    print(__doc__)
    sys.exit(1)

# Parse sam file
with open(output_file, "wt") as outfile:
    # Write header
    outfile.write("QueryName\tQueryPos\tMappingFlag\tTargetChrom\tTargetPos\tMappingQuality\tCigar\tDeletion\tHardclip\tInsertion\tMatch\tSoftclip\tSequence\tSequenceLength\tComplexity\tNumNs\tNumDiff\tAlignmentScore\tSuboptimalScore\tNumSuppAlign\tSuppAlignMinDiff\n")
    with open(input_sam) as infile:
        for line in infile:
            if line.startswith("@"):
                continue

            l = line.strip().split("\t")

            # Interesting features
            query_name = l[0]
            query_pos = int(query_name.split(";")[1])

            flag = int(l[1])
            if flag == 4:
                continue

            target_chrom = l[2]
            target_pos = int(l[3])
            quality = int(l[4])

            cigar = l[5]
            D, H, I, M, S = parse_cigar_string(cigar)
     
            sequence = l[9]
            complexity = round(len(gzip.compress("".join(sequence[:]).encode())) / len(sequence), 3)

            # Correct position at start of contig
            if query_pos <= window_length:
                target_offset = (len(sequence) // 2) - query_pos
            else:
                target_offset = len(sequence) // 2

            target_pos += target_offset

            num_Ns = sequence.count("N")
            num_diff = int(l[11].split(":")[2])
            alignment_score = int(l[13].split(":")[2])
            suboptimal_score = int(l[14].split(":")[2])
            has_xa = "XA:" in line
            num_xa = 0 if not has_xa else l[15].count(";")
            xa_min_diff = 35 if not has_xa else min([int(x.split(",")[-1]) for x in l[15].strip(";").split(";")])

            # Export results 
            outline = [query_name, query_pos, flag, target_chrom, target_pos,
                    quality, cigar, D, H, I, M, S, sequence, len(sequence), complexity, num_Ns,
                    num_diff, alignment_score, suboptimal_score, int(num_xa), xa_min_diff]

            outfile.write("\t".join([str(x) for x in outline]) + "\n")
