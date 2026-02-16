#!/usr/bin/env python3
"""Get informative features from sam file

Usage:
    <program> input_sam window_length output_file
"""

# Modules
from collections import defaultdict
from re import findall
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

def get_correction(cigar):
    """Given a cigar string, return the position correction for this alignment
    for the central nucleotide position
    """
    insertion_length = 0
    deletion_length = 0

    chunks = findall('[0-9]+[A-Z]', cigar)
    total_length = sum([int(x[:-1]) for x in chunks if x[-1] != "D"])
    half_length = (total_length - 1) / 2
    length_so_far = 0

    for c in chunks:
        l, k = int(c[:-1]), c[-1]
        length_so_far += l
        if k == "D":
            deletion_length += l
        elif k == "I":
            insertion_length += l

        if length_so_far > half_length:
            break

    return 0 - insertion_length + deletion_length

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

            ## Correct position at start of contig
            #if query_pos <= window_length:
            #    target_offset = (len(sequence) // 2) - query_pos
            #else:
            #    target_offset = len(sequence) // 2

            target_pos += window_length

            num_Ns = sequence.count("N")
            num_diff = int(l[11].split(":")[2])
            alignment_score = int(l[13].split(":")[2])
            suboptimal_score = int(l[14].split(":")[2])
            has_xa = "XA:" in line
            num_xa = 0 if not has_xa else l[15].count(";")
            xa_min_diff = 35 if not has_xa else min([int(x.split(",")[-1]) for x in l[15].strip(";").split(";")])

            # Correct target_pos based on cigar string
            target_pos += get_correction(cigar)

            # Export results 
            outline = [query_name, query_pos, flag, target_chrom, target_pos,
                    quality, cigar, D, H, I, M, S, sequence, len(sequence), complexity, num_Ns,
                    num_diff, alignment_score, suboptimal_score, int(num_xa), xa_min_diff]

            outfile.write("\t".join([str(x) for x in outline]) + "\n")
