# TODO

## Things to do before publication

- Config file
  - Add parameters for the filters

- Validation script
  - Input files can be found
  - Scaffold names in old genome are the same as those in the VCF

- Conda environment `requirements.txt` file

- Doc
  - Compare with barque, gawn and stacks workflow for sections
  - Add species name for the test dataset
  - List all the dependencies
  - Explicitely describe VCF format (3 first columns)

## Testing before publication
- Run a proper test
  - Realign and call SNPs on new genome
  - Compare with SNPLift
- Run SNPLift on its result to try to get back the original (test dataset)
  - See if you still lose some alignments
  - Check that you recover the original positions
- Give time estimate based on the genome size, number of SNPs, and number of samples

## Maybe
- Check nucleotide distance of genomes using first chromosome
  - Correlate to proportion of SNPs transfered
