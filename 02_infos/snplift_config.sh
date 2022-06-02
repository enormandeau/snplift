#!/bin/bash

# Input files
export OLD_GENOME="03_genomes/genome_old.fasta"
export NEW_GENOME="03_genomes/genome_new.fasta"

# Output files
export OLD_VCF="04_input_vcf/old.vcf"
export NEW_VCF="new.vcf"

export WINDOW_LENGTH=100 # If you modify this value, also modify 06_score_markers.py
export NUM_NEIGHBOURS=10
