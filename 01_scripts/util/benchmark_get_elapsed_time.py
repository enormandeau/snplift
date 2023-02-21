#!/usr/bin/env python3
"""Add elapsed time to benchmark results from stdin

Usage:
    <program>
"""

# Modules
import sys

# Let's go
for line in sys.stdin:
    l = line.strip().split("\t")
    start, end = l[4:]

    start = [int(x) for x in [start[:2], start[2:4], start[4:]]]
    start = 3600 * start[0] + 60 * start[1] + start[2]

    end = [int(x) for x in [end[:2], end[2:4], end[4:]]]
    end = 3600 * end[0] + 60 * end[1] + end[2]

    duration = end - start
    if duration < 0:
        duration += 86400

    l.append(str(duration))

    print("\t".join(l))
