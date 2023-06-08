# Things to do before publication

## Validation script (Crash explicitly)
- Input files can be found
- Dependencies are met
- Scaffold names in old genome are the same as those in the input_file
- Scaffold name formats are OK in all input files
- Bump to v1.0.0

# Future improvements
- Use only center portion around SNP and find best marker position (sliding window)
- Make faster by splitting after mapping?
- In collinearity exploration, add percentage after num bases
- Install deps from a `requirements.txt` file
- Could we cheat the program by adding FAKE SNPs on each side of real ones to confirm
  more of those that get discarded? Once there, should we strive to build a one-to-one
  correspondence for all the positions?
