# Align genomes with minimap
time minimap2 -t60 -x asm5 -o correspondance3.paf genome_v4_chromosomes_only.fasta genome_v2_chromosomes_only.fasta 

# Plot collinearity with minidot
minidot correspondance3.paf > out3.eps && epstopdf out3.eps

# Assess what proportion of genome is collinear sections
sort -V correspondance3.paf | cut -f 3-4 | awk '{print $2-$1}' | awk '$1>100000' | total
