# SNPLift

Lift over SNP postions from a VCF to match a new reference genome

Developed by [Eric Normandeau](https://github.com/enormandeau) in
[Louis Bernatchez](http://www.bio.ulaval.ca/louisbernatchez/presentation.htm)'s
laboratory.

Please see the licence information at the end of this file.

# TODO
- Config file
- Test dataset
  - Sister repo on github with 1st chromosomes from Davoud's 2 genmes
- Doc
- Run SNPLift on its result to try to get back the original
  - See if you still lose some alignments
  - Check that you recover the original positions

## Description

**SNPLift** takes a VCF with locus positions matching a genome and lifts over
these positions so they match a new reference genome. The goal of the procedure
is to rapidly be able to leverage the new genome without having to re-align all
the sample reads and then call and filter the loci. In the process, a
proportion of the loci are inevitably lost. Ideally, the proper way of
getting the good positions for the loci would be to proceed to the
re-alignment.

## Installation

To use **SNPLift**, you will need a local copy of its repository. Different
releases can be [found here](https://github.com/enormandeau/SNPLift/releases).
It is recommended to always use the latest release or even the developpment
version. You can either download an archive of the latest release at the above
link or get the latest commit (recommended) with the following git command:

```
git clone https://github.com/enormandeau/SNPLift
```

## Dependencies

To run **SNPLift**, you will also need to have the following programs installed
on your computer.

- **SNPLift** will only work on GNU Linux or OSX
- bash 4+
- bwa
- samtools
- python 3.5+ (you can use miniconda3 to install python)
- R 3+ (ubuntu/mint: `sudo apt-get install r-base-core`)
- [gnu parallel](https://www.gnu.org/software/parallel/)
- *TODO* etc.

## Preparation

- Install dependencies
- Download a copy of the **SNPLift** repository (see **Installation** above)
- *TODO* etc.

## Overview of SNPLift steps

During the analyses, the following steps are performed:

- Visualize collinearity of the two genomes
- Index new genome
- Get original coordinates
- Extract flanking sequences around SNPs (100bp on each side)
- Map reads with bwa (keep best hit)
- Get new coordinates
- Filters based on alignment
  - *TODO* Detail filters
- Save some bad alignments if they are locally collinear
- Update coordinates
- Update VCF

## Running
### Prepare genomes
### Validate scaffold names
### Run

## Results

## License

CC share-alike

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">SNPLift</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Eric Normandeau</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/enormandeau/SNPLift" rel="dct:source">https://github.com/enormandeau/SNPLift</a>.
