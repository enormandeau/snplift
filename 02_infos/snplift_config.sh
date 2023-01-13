#!/bin/bash

# Input files
export OLD_GENOME="03_genomes/old_genome.fasta"
export NEW_GENOME="03_genomes/new_genome.fasta"

# Output files
export OLD_VCF="04_input_vcf/old.vcf"
export NEW_VCF="new.vcf"

# Skiping steps
export SKIP_COLLINEARITY=1  # Skip alignment of both genomes and visual collinearity comparison [0, 1]
export SKIP_INDEXING=1      # Skip indexing the genome if it is already indexed with `bwa index` [0, 1]

# Parameters
export NCPUS=10             # Number of cores to use for mapping steps (miniconda2, bwa mem)
export WINDOW_LENGTH=100    # If you modify this value, also modify 06_score_markers.py
export NUM_NEIGHBOURS=10    # Number of neigbour SNPs to consider when trying to recuperate
                            #   more dubious SNPs using local correlations of positions
