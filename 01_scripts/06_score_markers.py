#!/usr/bin/env python3
"""Score markers based on different criteria (listed below)

Usage:
    <program> input_features output_scores

Criteria and quality penalty (as a fraction of 1):
    Flag > 2000: -1.0
    Quality < 10: -0.5
    dd$SuppAlignMinDiff < 4: -0.8
    dd$NumDiff > 0.05 * len(sequence): -0.3
    dd$Softclip > 0.25 * len(sequence): -0.2
    (dd$Match + dd$Softclip) < 0.9 * len(sequence): -0.3
    (dd$Softclip - 0.05 * len(sequence)) / (dd$NumNs + 1) <= 1.1: -0.5
"""

# Modules
import sys

# Add to parameters if needed
expected_length = 200

# Parse user input
try:
    input_features = sys.argv[1]
    output_scores = sys.argv[2]
except:
    print(__doc__)
    sys.exit(1)

# Score away!
with open(input_features, "rt") as infile:
    with open(output_scores, "wt") as outfile:
        for line in infile:
            l = line.strip().split("\t")

            if line.startswith("QueryName"):
                #header = l[:]
                header =  ["QueryScaffold", "QueryName", "QueryPos", "TargetChrom", "TargetPos"]
                header.insert(0, "Penalties")
                header.insert(0, "Score")
                outfile.write("\t".join(header) + "\n")
                continue

            QueryName, QueryPos, MappingFlag, TargetChrom, TargetPos, MappingQuality, Cigar, Deletion, Hardclip, Insertion, Match, Softclip, Sequence, SequenceLength, Complexity, NumNs, NumDiff, AlignmentScore, SuboptimalScore, NumSuppAlign, SuppAlignMinDiff = l

            # Apply penalties
            score = 1.0
            penalties = []
            query_scaffold = QueryName.split(";")[0]

            if len(Sequence) < (expected_length / 2):
                penalties.append("L")
                score -= 1.0

            if int(MappingFlag) > 2000:
                # Remove these altogether
                #penalties.append("F")
                #score -= 1.1 
                continue

            if int(MappingQuality) < 10:
                penalties.append("Q")

                if int(MappingQuality) < 5:
                    score -= 1.0
                else:
                    score -= 0.6

            if int(SuppAlignMinDiff) <= 5:
                penalties.append("+")
                score -= (0.5 + (0.4 - int(SuppAlignMinDiff) / 10))

            if int(NumDiff) > 0.05 * len(Sequence):
                penalties.append("D")
                score -= 0.3

            if int(Softclip) > 0.25 * len(Sequence):
                penalties.append("s")
                score -= 0.2

            if (int(Match) + int(Softclip)) < 0.9 * len(Sequence):
                penalties.append("P")
                score -= 0.3

            if ((int(Softclip) - 0.05 * len(Sequence)) / (int(NumDiff) + 1)) > 1.1:
                penalties.append("S")
                score -= 0.5


            if not penalties:
                penalties.append(".")

            outfile.write("\t".join([str(round(score, 2)), "".join(penalties)] +
                [query_scaffold, QueryName, QueryPos, TargetChrom, TargetPos]) + "\n")
