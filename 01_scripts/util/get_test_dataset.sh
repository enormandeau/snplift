#!/bin/bash
# Get test dataset from github and prepare it for a snplift run

rm -rf snplift_test_dataset 2>/dev/null

echo -e "\nSNPlift: Cloning test data\n"
git clone git@github.com:enormandeau/snplift_test_dataset

echo -e "\nSNPlift: Extracting test data"
gunzip -c snplift_test_dataset/new_genome.fasta.gz > 03_genomes/new_genome.fasta
gunzip -c snplift_test_dataset/old_genome.fasta.gz > 03_genomes/old_genome.fasta
gunzip -c snplift_test_dataset/old.vcf.gz > 04_input_vcf/old.vcf

echo -e "\nSNPlift: Ready to launch analysis with:\n\n    ./snplift 02_infos/snplift_config.sh"
