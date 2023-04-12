#!/usr/bin/env python3
"""Use marker scores and mapping positions to create corresponding positions
between the VCFs

Usage:
    <program> input_scores window_size output_correspondence

Where window_size is the number of neighbor SNPs to consider on each side.
"""

# Modules
from scipy.stats import pearsonr
import sys

# Functions
def keep_snp(past, now, future):

    # Score of current locus
    if float(now[0]) > 0.5:
        return True

    else:
        # Organize infos for past, now, and future into pandas dataframe
        infos = [x for x in past + [now] + future]

        # Keep only SNPs in same chromosome
        chromosome = now[2]
        infos = [x for x in infos if x[2] == chromosome]

        if len(infos) < 2 * window_size:
            return False

        # Skip if closest neighbours are too far (span more than 5Kbp by SNP in window_size)
        # Don't use info of too sparse markers
        left_pos = infos[0][4]
        right_pos = infos[1][4]

        if (int(right_pos) - int(left_pos)) > (2 * window_size * 5000):
            return False

        # Compute useful neighbourhood metrix
        scores = [float(x[0]) for x in infos]
        average = round(sum(scores) / len(scores), 2)

        if average < 0.4:
            return False

        num_negative = len([x for x in scores if x <= 0.0])

        if num_negative > window_size / 2:
            return False

        # Is Pearson coef for scores close to 1?
        try:
            pos1 = [int(x[4]) for x in infos]
            pos2 = [int(x[6]) for x in infos]
            pearson = abs(pearsonr(pos1, pos2)[0])
        except:
            pearson = 0.0

        if pearson >= 0.99:
            return True

# Parsing user input
try:
    input_scores = sys.argv[1]
    window_size = int(sys.argv[2])
    output_correspondence = sys.argv[3]
    num_cpus = int(sys.argv[4])
except:
    print(__doc__)
    sys.exit(1)

# Read input_scores into 3 compartments past, now, future
past = []
now = None
future = []

file_num = int(input_scores.strip().split("/")[1].split(".")[1])

with open(input_scores, "rt") as infile:
    with open(output_correspondence, "wt") as outfile:
        for line in infile:

            # Header
            if line.startswith("Score"):
                outfile.write(line)
                continue

            #Score, Penalties, QueryScaffold, QueryName, QueryPos, TargetChrom, TargetPos
            l = line.strip().split("\t")

            # Get first info line
            if not now:

                if file_num == 0:
                    now = l

                    # Fill future list
                    while len(future) < window_size:
                        l = infile.readline().strip().split("\t")
                        future.append(l)

                else:
                    past.append(l)

                    while len(past) < window_size:
                        l = infile.readline().strip().split("\t")
                        past.append(l)

                    now = infile.readline().strip().split("\t")

                    while len(future) < window_size:
                        l = infile.readline().strip().split("\t")
                        future.append(l)

            # Slide past, now, and future one step forward
            else:
                past.append(now)
                now = future.pop(0)
                future.append(l)

                if len(past) > window_size:
                    past.pop(0)

            # Evaluate SNPs
            if keep_snp(past, now, future):
                outfile.write("\t".join(now) + "\n")

        # Treat last SNPs of the file
        if file_num == num_cpus - 1:
            while future:
                past.append(now)
                now = future.pop(0)

                if len(past) > window_size:
                    past.pop(0)

                # Evaluate SNPs
                if keep_snp(past, now, future):
                    outfile.write("\t".join(l) + "\n")

