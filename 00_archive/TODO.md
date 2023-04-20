# Things to do before publication

## Needs fixing
* Corrected VCF
  - Keep only one SNP per position
  - If hit reverse strand, modify alleles (A/G -> T/C)
  - Produce new SNP id in column 3
- Bump version

## Position accuracy
- Extract more accurate SNP positions
  - At ends of chromosomes (put info in the sequence name?)
    - Already have something for this? Only for chromosome starts?
  - When there are Ns
  - Other non-perfect matches
    - Use only center portion around SNP and find best position
      - Alternatively, do this for on the left then on the right of the SNP

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
