# TODO

## Things to do before publication

- Config file
  - Add parameters for the filters
- Validation script
  - Input files can be found
  - Scaffold names in old genome are the same as those in the VCF
  - Scaffolds have unique names in each genomes
- Doc
  - Compare with barque, gawn and stacks workflow for sections
  - Add species name for the test dataset
  - List all the dependencies
  - Explicitely describe VCF format (3 first columns)

## Testing before publication
- Run a real test
  - Realign and call SNPs on new genome
  - Compare with SNPLift
- Give time estimate based on the genome size, number of SNPs, and number of samples
- Run SNPLift on its result to try to get back the original (test dataset)
  - See if you still lose some alignments
  - Check that you recover the original positions

## Maybe
- Check nucleotide distance of genomes using first chromosome
