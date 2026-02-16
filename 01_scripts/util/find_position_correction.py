#!/usr/bin/env python3
"""Explore effect of indels on central SNP prediction by SNPlift

Usage:
    <program> corr_file genome_file vcf_file
"""

# Modules
from collections import defaultdict
from re import findall
import gzip
import sys

# Classes
class Fasta(object):
    """Fasta object with name and sequence
    """

    def __init__(self, name, sequence):
        self.name = name.split(" ")[0]
        self.sequence = sequence

    def write_to_file(self, handle):
        handle.write(">" + self.name + "\n")
        handle.write(self.sequence + "\n")

    def __repr__(self):
        return self.name + " " + self.sequence[:31]

# Functions
def myopen(_file, mode="rt"):
    if _file.endswith(".gz"):
        return gzip.open(_file, mode=mode)

    else:
        return open(_file, mode=mode)

def fasta_iterator(input_file):
    """Takes a fasta file input_file and returns a fasta iterator
    """
    with myopen(input_file) as f:
        sequence = []
        name = ""
        begun = False

        for line in f:
            line = line.strip()

            if line.startswith(">"):
                if begun:
                    yield Fasta(name, "".join(sequence))

                name = line[1:]
                sequence = ""
                begun = True

            else:
                sequence += line

        if name != "":
            yield Fasta(name, "".join(sequence))

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

# Parsing user input
try:
    corr_file = sys.argv[1]
    genome_file = sys.argv[2]
    vcf_file = sys.argv[3]
except:
    print(__doc__)
    sys.exit(1)

# Read corr_file
corr = defaultdict(lambda: defaultdict(list))

with open(corr_file, "rt") as infile:
    for line in infile:
        if line.startswith("Score"):
            continue

        l = line.strip().split("\t")
        chrom1 = l[2]
        pos1 = int(l[4])
        chrom2 = l[5]
        pos2 = int(l[6])
        cigar = l[8]

        corr[chrom1][pos1] = [chrom2, pos2, cigar]

print("Done with corr file")

# Read vcf_file
vcf = defaultdict(lambda: defaultdict(list))

with open(vcf_file, "rt") as infile:
    for line in infile:
        if line.startswith("#"):
            continue

        l = line.strip().split("\t")
        chrom = l[0]
        pos = int(l[1])
        alleles = l[3:5]

        vcf[chrom][pos] = alleles

print("Done with VCF file")

# Load genome_file in memory
sequences = {x.name: x.sequence for x in fasta_iterator(genome_file)}
print("Done with genome file")

# Explore position correction
for chrom1 in corr:
    for pos1 in corr[chrom1]:
        chrom2, pos2, cigar = corr[chrom1][pos1]

        a = vcf[chrom2][pos2]

        if len(a[0]) == len(a[1]) and len(a[0]) == 1:
            alleles = vcf[chrom2][pos2]

            correction = get_correction(cigar)
            nuc = sequences[chrom2][pos2-1+correction].upper()
            region = sequences[chrom2][(pos2-1+correction-20):(pos2-1+correction+20)].upper()
            print(chrom1, pos1, chrom2, pos2, cigar, alleles, nuc, nuc in alleles, region)
