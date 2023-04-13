# Things to do before publication

## Needs fixing
- Confirm all position from .scores files are in .corr (ie: not missing 1-2 at the interface)
- Report all position correspondances with score code and value
- Keep only one SNP per position
- For VCFs
  - If hit reverse strand, modify alleles (A/G -> T/C)
  - Produce new SNP id in column 3
- Try harder to extract accurate SNP positions from sam file

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
- Could we cheat the program by adding FAKE SNPs on each side of real ones to confirm
  more of those that get discarded? Once there, should we strive to build a one-to-one
  correspondence for all the positions?
- Make faster by splitting after mapping?
- Add optional FastANI run to assess nucleotide distance between the genomes
- In collinearity exploration, add percentage after num bases
- Install deps in a conda environment `requirements.txt` file
