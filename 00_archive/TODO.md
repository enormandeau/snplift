# Things to do before publication

## Revise MS
- Publish on bioRxiv
- Submit somewhere

## Documentation
- Improve format using doc from barque, GAWN and stacks workflow
- Add species name for the test dataset
- Confirm all the dependencies
- Explicitly describe VCF format (3 first columns)
- Describe behaviour (eg: write lines with `#` without treatment)
- Bump to v0.5.0

## Validation script
- Input files can be found
- Scaffold names in old genome are the same as those in the VCF
- Scaffold name formats are OK in all input files
- Make snplift crash explicitely if one program crashes
- Bump to v0.6.0

# Test for v1.0.0
- Test on new Linux computer / MacOS
- Bump to v1.0.0

## Future improvements
- Use FastANI to assess nucleotide distance between the genomes
  - Correlate to proportion of SNPs transferred
- In collinearity exploration, add percentage after num bases
- Install deps in a conda environment `requirements.txt` file
