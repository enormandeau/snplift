#!/usr/bin/env python3
"""Use marker scores and mapping positions to create corresponding positions
between the VCFs

Usage:
    <program> input_scores window_size output_correspondence

Where window_size is the number of neighbor SNPs to consider on each side.
"""

# Modules
from scipy.stats import pearsonr
import pandas as pd
import sys

# Parsing user input
try:
    input_scores = sys.argv[1]
    window_size = int(sys.argv[2])
    output_correspondence = sys.argv[3]
except:
    print(__doc__)
    sys.exit(1)

# Read input_scores into 3 compartments past, now, future
past = []
now = None
future = []

with open(input_scores, "rt") as infile:
    with open(output_correspondence, "wt") as outfile:
        for line in infile:

            # Header
            if line.startswith("Score"):
                outfile.write(line)
                continue

            #Detail of columns (index and value):
            # 0      1          2              3          4         5            6
            #Score, Penalties, QueryScaffold, QueryName, QueryPos, TargetChrom, TargetPos
            l = line.strip().split("\t")

            # Get first info line
            if not now:
                now = l

                # Fill future list
                while len(future) < window_size:
                    future.append(infile.readline().strip().split("\t"))

            # Slide past, now, and future one step forward
            else:
                past.append(now)
                now = future.pop(0)
                future.append(l)

                if len(past) > window_size:
                    past.pop(0)

            # Evaluate SNPs
            keep = False

            # Score of current locus
            if float(now[0]) > 0.5:
                keep = True

            else:
                # Organize infos for past, now, and future into pandas dataframe
                infos = [x for x in past + [now] + future]
                infos_df = pd.DataFrame(infos, columns=["Score", "Flags", "Chr1", "LocusName", "Pos1", "Chr2", "Pos2"])
                infos_df["Pos1"] = infos_df["Pos1"].astype("int64")
                infos_df["Pos2"] = infos_df["Pos2"].astype("int64")

                # Compute useful neighbourhood metrix
                scores = [float(x[0]) for x in infos]
                average = round(sum(scores) / len(scores), 2)
                num_negative = len([x for x in scores if x <= 0.0])

                if average < 0.2:
                    continue
                
                if num_negative > window_size / 2:
                    continue

                # Is Pearson coef for scores close to 1?
                try:
                    pearson = abs(pearsonr(infos_df["Pos1"], infos_df["Pos2"])[0])
                except:
                    pearson = 0.0

                if pearson >= 0.99:
                    keep = True

            # Locus is good and should be kept
            if keep:
                outfile.write(line)
