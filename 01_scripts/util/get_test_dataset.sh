#!/bin/bash
# Get test dataset from github and prepare it for a snplift run

rm -rf snplift_test_dataset 2>/dev/null
git clone git@github.com:enormandeau/snplift_test_dataset
gunzip -c snplift_test_dataset/genome_new.fasta.gz > 03_genomes/genome_new.fasta
gunzip -c snplift_test_dataset/genome_old.fasta.gz > 03_genomes/genome_old.fasta
gunzip -c snplift_test_dataset/old.vcf.gz > 04_input_vcf/old.vcf
