# Version name ideas

Blushing.Pepper Elastic.Jujube Exuberant.Pear Flying.Carrot Refreshing.Tea
Running.Popsicle Scalding.Coffee Shiny.Zucchini Spicy.Soup Spiny.Artichoke
Squishy.Squid Sticky.Jam Sturdy.Beetroot Tangy.Miso

# Things to do before publication

- In numbers of reported SNPs, correct .sam and .features (they have too many)
* Make snplift crash if one program crashes
- In collinearity exploration, add percentage after num bases

## Benchmark
- Test on a variety of genomes / vcfs
  - Same genome with VCFs of different sizes
  - Collect genome-size, VCF-size, runtime
  - Build a regression model with gsize and vsize + interaction
  - Estimate runtime as a function
    - `runtime = ag + bv + cgv + d`
    - Maybe we can ignore some of these terms
- Suggest dividing by 10 and multiplying by their test runtime
- Run SNPLift on its result to try to get back the original (test dataset)
  - Check that you recover the original positions
- Test on new Linux computer / MacOS

## Revise MS
- Modify to reflect changes
- Tell Davoud it is his turn

## Documentation
- Improve format using doc from barque, GAWN and stacks workflow
- Add species name for the test dataset
- Confirm all the dependencies
- Explicitly describe VCF format (3 first columns)
- Describe behaviour (eg: write lines with `#` without treatment)
- Bump to v0.3.0 Careful Mango

## Validation script
- Input files can be found
- Scaffold names in old genome are the same as those in the VCF
- Scaffold name formats are OK in all input files
- Bump to v0.4.0 Jumping Squash

## Publish
- Bump to v1.0.0 Mindful Peach
- Publish on bioRxiv
- Submit somewhere

# Maybe
- Check nucleotide distance of genomes using first chromosome
  - Correlate to proportion of SNPs transferred
- Install with `conda create -n snplift -c bioconda snplift`
- Or use a conda environment `requirements.txt` file
- Or install dependencies and clone
