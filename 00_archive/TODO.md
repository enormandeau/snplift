# Things to do before publication
* `07_orrespondance.py` does not use chr info
  - Too slow for small scaffolds
* Replace the split command we don't loose SNPs at the file edges
- Copy config file to log folder
- Use FastANI to assess inter-genome distance
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

## Later
- Run SNPLift on its result to try to get back the original (test dataset)
  - Check that you recover the original positions
- In collinearity exploration, add percentage after num bases
- Check nucleotide distance of genomes using first chromosome
  - Correlate to proportion of SNPs transferred
- Install with `conda create -n snplift -c bioconda snplift`
- Or use a conda environment `requirements.txt` file
- Or install dependencies and clone

## Version name ideas
Blushing.Pepper Elastic.Jujube Exuberant.Pear Flying.Carrot Refreshing.Tea
Scalding.Coffee Shiny.Zucchini Spicy.Soup Spiny.Artichoke
Squishy.Squid Sticky.Jam Sturdy.Beetroot Tangy.Miso
