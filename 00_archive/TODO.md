# TODO

## Validation script (Crash explicitly)
- Input files can be found
- Dependencies are met
- Scaffold names in old genome are the same as those in the input file
- Scaffold name formats are OK in all input files

# Future improvements
- Make faster by splitting after mapping?
- Install deps from a `requirements.txt` file
- In collinearity exploration, add percentage after number of collinear bases
- Use only center portion around SNP and find best marker position (sliding window)
- Could we cheat the program by adding FAKE SNPs on each side of real ones to confirm
  more of those that get discarded, especially for smaller datasets?
