# Ideas for future improvements

## Position improvements
- Consider using soft and hard masking info at start of alignments to correct
  positions at start of chromosomes.
- Use only center portion around SNP and find best marker position (sliding window)

## Possibily maybe
- Make faster by splitting after mapping
- Install deps from a `requirements.txt` file
- In collinearity exploration, add percentage after number of collinear bases
- Could we cheat the program by adding FAKE SNPs on each side of real ones to help
  assess the collinearity of difficult regions? Especially with small datasets?
