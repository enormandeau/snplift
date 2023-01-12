# Version name ideas

Sweet Cantlou, Funny Tofu, Flying Zuccini, Tired Potato, Refreshing Tea
Scalding Coffee, Hot Salad, Sturdy Beetroot, Extravagant Pepper, Drifting Artichoke
Sparkling Apple, Dual Pear, Electric Bean, Jumping Squash, Whispering Corn

# Things to do before publication
## Config file
- Option to skip collinearity viz
- Option to skip genome indexing
- Add parameters for the filters

## Validation script
- Input files can be found
- Scaffold names in old genome are the same as those in the VCF
- Scaffold name formats are OK in all input files

## Doc
- Improve format using doc from barque, gawn and stacks workflow
- Add species name for the test dataset
- Confirm all the dependencies
- Explicitely describe VCF format (3 first columns)
- Describe behaviour (eg: write lines with `#` without treatment)

## Benchmark
- Give time estimate based on genome size as well as number of SNPs and samples
- Give estimate in minutes AND as a factor compared to test run
- Run SNPLift on its result to try to get back the original (test dataset)
  - See if you still lose some alignments
    - We get 99.21% transfer
  - Check that you recover the original positions

## Test on new Linux computer / MacOS

# Maybe
- Check nucleotide distance of genomes using first chromosome
  - Correlate to proportion of SNPs transfered
- Install with `conda create -n snplift -c bioconda snplift`
- Or use a conda environment `requirements.txt` file
- Or install depencencies and clone
