#!/bin/bash

# Input files
export OLD_GENOME="03_genomes/old_genome.fasta"
export NEW_GENOME="03_genomes/new_genome.fasta"

# Output files
export INPUT_FILE="04_input_vcf/old.vcf"
export OUTPUT_FILE="new.vcf"

# Skipping genome indexing
export SKIP_INDEXING=1      # Save time if genome already indexed with 'bwa index' [0, 1].

# Skip exploring features
export SKIP_VISUALIZATION=1 # Avoid creating a plot to explore features. These are used
                            #   for debugging [0, 1].

# Checking for collinearity between both genome versions
export CHECK_COLLINEARITY=0 # Increases runtime by 5+ times. Align genomes and produce a
                            #   collinearity comparison figure [0, 1].

# Parameters
export NCPUS=10             # Number of cores to use (around 10 and maximum 20 is recommended)
                            #   For less than 100K SNPs, 1 to 4 cores is a good choice
                            #   For less than 1M SNPs, 10 cores is a good choice
                            #   Above this, 20 cores is going to be slightly faster

export WINDOW_LENGTH=300    # Sequence size kept on both sides of each SNP. For highly contiguous
                            #   genomes, 300 leads to more positions being tranfered. For more
                            #   fragmented genomes, using 200 or even 100 may produce better results.

export NUM_NEIGHBOURS=20    # Number of neighbour SNPs to consider when trying to salvage
                            #   more dubious SNPs using local correlations of positions

# Do final corrections to VCF file. You may need
export UNIQUE_POS=1         # Keep only the first locus encountered for each position
export CORRECT_ID=1         # Recompute the ID column from columns 1 and 2
export ID_COLUMN=3          # ID column number
export CORRECT_ALLELES=1    # Reverse complement alleles when new genome region is inversed
export ALLELE_COLUMNS=4,5   # Columns of alleles to reverse complement
