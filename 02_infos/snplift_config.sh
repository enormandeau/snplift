#!/bin/bash

# Global variables
OLD_GENOME="03_genomes/genome_old.fasta"
NEW_GENOME="03_genomes/genome_new.fasta"

OLD_VCF="04_input_vcf/old.vcf"
NEW_VCF="new.vcf"

WINDOW_LENGTH=100 # If you modify this value, also modify 06_score_markers.py
NUM_NEIGHBOURS=10
