#!/bin/bash
# Map flanking regions to new genome

time bwa mem -t 20 genome.fasta positions.fasta > positions.sam
