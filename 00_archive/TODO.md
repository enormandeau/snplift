# Things to do before publication

## Needs fixing
- Report all position correspondances with score (code and value)
- NNNNs in fasta sequences. Ignore them? Be more lenient for soft clipping when NNNNs
- Need more than 2 columns, bed files won't work
- Multiple SNPs at the same position (keep only best one or flush both if same score)
- If hit reverse strand, modify alleles (A/G -> T/C)
- Produce new SNP id in column 3
- Try harder to report an accurate new position

## Validation script (Crash explicitly)
- Input files can be found
- Dependencies are met
- Scaffold names in old genome are the same as those in the input_file
- Scaffold name formats are OK in all input files
- Bump to v1.0.0

## Revise MS
* Add references (give to Maxime)
- Publish on bioRxiv
- Submit to Bioinformatics - Application Notes

## Future improvements
- Make faster by splitting after mapping?
- Add optional FastANI run to assess nucleotide distance between the genomes
- In collinearity exploration, add percentage after num bases
- Install deps in a conda environment `requirements.txt` file
