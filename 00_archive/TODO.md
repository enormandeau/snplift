# Things to do before publication
* Replace the split command so we don't loose SNPs at the file edges
- Bump to v0.3.0 Running.Popsicle

## Benchmark
- Test on a variety of genomes / vcfs
  - Same genome with VCFs of different sizes
  - Collect genome-size, VCF-size, runtime
  - Build a regression model with gsize and vsize + interaction
  - Estimate runtime as a function
    - `runtime = ag + bv + cgv + d`
    - Maybe we can ignore some of these terms
- Suggest dividing by 10 and multiplying by their test runtime
- Report time and RAM needed

## Documentation
- Improve format using doc from barque, GAWN and stacks workflow
- Add species name for the test dataset
- Confirm all the dependencies
- Explicitly describe VCF format (3 first columns)
- Describe behaviour (eg: write lines with `#` without treatment)
- Bump to v0.3.0 Careful Mango

## Validation script
* Make snplift crash if one program crashes
- Input files can be found
- Scaffold names in old genome are the same as those in the VCF
- Scaffold name formats are OK in all input files
- Bump to v0.4.0 Jumping Squash

# Test for v1.0.0
- Test on new Linux computer / MacOS
- Bump to v1.0.0 Mindful Peach

## Revise MS
- Modify MS to reflect changes
- Tell Davoud it is his turn
- Publish on bioRxiv
- Submit somewhere

## Future improvements
- Copy config file to log folder for each run
- Use FastANI to assess nucleotide distance between the genomes
  - Correlate to proportion of SNPs transferred
- In collinearity exploration, add percentage after num bases
- Install deps in a conda environment `requirements.txt` file

## Version name ideas
Blushing.Pepper Elastic.Jujube Exuberant.Pear Flying.Carrot Refreshing.Tea
Scalding.Coffee Shiny.Zucchini Spicy.Soup Spiny.Artichoke
Squishy.Squid Sticky.Jam Sturdy.Beetroot Tangy.Miso
