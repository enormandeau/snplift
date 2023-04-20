#!/usr/bin/env python3
"""Score markers based on different criteria (listed below)

Usage:
    <program> input_features output_scores
"""

# Modules
import sys

# Parse user input
try:
    input_features = sys.argv[1]
    output_scores = sys.argv[2]
    window_size = int(sys.argv[3])
except:
    print(__doc__)
    sys.exit(1)

expected_length = 2 * window_size

# Score away!
with open(input_features, "rt") as infile:
    with open(output_scores, "wt") as outfile:
        for line in infile:
            l = line.strip().split("\t")

            if line.startswith("QueryName"):
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

            # Alignment too short
            if len(Sequence) < (expected_length / 2):
                penalties.append("L")
                score -= 1.0

            # Supplementary alignments
            if int(MappingFlag) > 2000:
                # Remove these altogether
                continue

            # Mapping quality
            if int(MappingQuality) < 10:
                penalties.append("Q")

                if int(MappingQuality) < 5:
                    score -= 0.8
                else:
                    score -= 0.4

            # Number of differences over best supplementary alignment
            if int(SuppAlignMinDiff) <= 5:
                penalties.append("+")
                score -= (0.5 + (0.4 - int(SuppAlignMinDiff) / 10))

            # More than 5% difference to reference genome
            if int(NumDiff) > 0.05 * len(Sequence):

                # More than 10% difference to reference genome
                if int(NumDiff) > 0.10 * len(Sequence):
                    penalties.append("D")
                    score -= 0.5

                else:
                    penalties.append("d")
                    score -= 0.2

            # Maximum 10% softclip that are not Ns
            if (int(Softclip) - int(NumNs)) > 0.10 * len(Sequence):

                # Maximum 20% softclip that are not Ns
                if (int(Softclip) - int(NumNs)) > 0.10 * len(Sequence):
                    penalties.append("S")
                    score -= 0.5

                else:
                    penalties.append("s")
                    score -= 0.2

            # Match plus softclip and Ns are not at least 90% of sequence
            if (int(Match) + int(Softclip) + int(NumNs)) < 0.9 * len(Sequence):

                # Match plus softclip and Ns are not at least 80% of sequence
                if (int(Match) + int(Softclip) + int(NumNs)) < 0.8 * len(Sequence):
                    penalties.append("p")
                    score -= 0.3

                else:
                    penalties.append("P")
                    score -= 0.5

            if not penalties:
                penalties.append(".")

            outfile.write("\t".join([str(round(score, 2)), "".join(penalties)] +
                [query_scaffold, QueryName, QueryPos, TargetChrom, TargetPos]) + "\n")
