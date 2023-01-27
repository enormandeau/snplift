#!/bin/bash

# Input files
export OLD_GENOME="03_genomes/old_genome.fasta"
export NEW_GENOME="03_genomes/new_genome.fasta"

# Output files
export OLD_VCF="04_input_vcf/old.vcf"
export NEW_VCF="new.vcf"

# Skiping genome indexing
export SKIP_INDEXING=0      # Save time if genome already indexed with 'bwa index' [0, 1]

# Checking for collinearity between both genome versions
export CHECK_COLLINEARITY=0 # Increases runtime by ~5 times. Align genomes and produce a
                            #  collinearity comparison figure [0, 1]

# Parameters
export NCPUS=10             # Number of cores to use for mapping steps (miniconda2, bwa mem)
export WINDOW_LENGTH=100    # If you modify this value, also modify 06_score_markers.py
export NUM_NEIGHBOURS=10    # Number of neigbour SNPs to consider when trying to recuperate
                            #   more dubious SNPs using local correlations of positions
