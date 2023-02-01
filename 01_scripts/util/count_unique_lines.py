#!/usr/bin/env python3
"""Return number of unique lines from stdin

Usage:
    <program>
"""

# Modules
import sys

# Count
unique = set()
for line in sys.stdin:
    unique.add(line)

print(len(unique))
