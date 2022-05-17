#!/bin/bash
# Run the full pipeline

# Global variables
OLD_GENOME="03_genomes/genome_old.fasta"
NEW_GENOME="03_genomes/genome_new.fasta"

OLD_VCF="04_input_vcf/old.vcf"
NEW_VCF="new.vcf"

WINDOW_LENGTH=100 # If you modify this value, also modify 06_score_markers.py
NUM_NEIGHBOURS=10

# TODO rename chromosomes to remove anything after a space
# TODO Validate that all the have unique names in each of the genomes

# Check collinearity
echo "SNPTransfer: Assessing collinearity of the two genomes"
time ./02_collinearity/01_collinearity.sh "$NEW_GENOME" "$OLD_GENOME"

# SNPTransfer
## Index new genome if needed
echo -e "\nSNPTransfer: Indexing new genome"
time bwa index "$NEW_GENOME"

## Get original coordinates
echo -e "\nSNPTransfer: Extracting positions from old VCF"
time ./01_scripts/01_extract_positions.sh "$OLD_VCF" positions.ids

## Extract flanking sequences around SNPs (100bp on each side)
echo -e "\nSNPTransfer: Extracting flanking sequences around SNPs in old genome"
time ./01_scripts/02_fasta_extract_flanking_regions.py "$OLD_GENOME" positions.ids "$WINDOW_LENGTH" positions.fasta

## Map reads with bwa (keep best hit)
echo -e "\nSNPTransfer: Mapping flanking sequences on new genome"
time ./01_scripts/03_map_reads.sh "$NEW_GENOME" positions.fasta

## Get new coordinates
echo -e "\nSNPTransfer: Extract useful features from alignments"
time ./01_scripts/04_extract_features_from_alignments.py positions.sam positions.features

## Score markers based on alignments (detail them)
echo -e "\nSNPTransfer: Score markers based on extracted features"
time ./01_scripts/06_score_markers.py positions.features positions.scores

## Write good loci and recuperate bad alignments if locally collinear
echo -e "\nSNPTransfer: Getting coordinates of transferable SNPs"
time ./01_scripts/07_correspondence.py positions.scores "$NUM_NEIGHBOURS" positions.corr

## Update VCF
echo -e "\nSNPTransfer: Writing new VCF with updated coordinates"
time ./01_scripts/08_replace_coordinates_in_vcf.py "$OLD_VCF" positions.corr "$NEW_VCF"

echo -e "\nSNPTransfer: Number of SNPs at each step -"; ls "$OLD_VCF" -1tr positions.* new.vcf | grep -v fasta | parallel -k wc -l

echo -e "\nSNPTransfer: Run completed"
