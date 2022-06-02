# SNPLift

Lift over SNP postions from a VCF to match a new reference genome

Developed by [Eric Normandeau](https://github.com/enormandeau) in
[Louis Bernatchez](http://www.bio.ulaval.ca/louisbernatchez/presentation.htm)'s
laboratory.

Please see the licence information at the end of this file.

## Description

**SNPLift** takes a VCF with locus positions matching a genome and lifts over
these positions so they match a new reference genome. The goal of the procedure
is to rapidly be able to leverage the new genome without having to re-align all
the sample reads and then call and filter the loci. In the process, a
proportion of the loci are inevitably lost.

**WARNING** Ultimately, the only way to guaranty that all the positions on the
new genome are correct is to re-align the reads and call the genotypes again.

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
- git (to clone test dataset)
- bwa
- samtools
- minimap2 (to visualize the collinearity of the two genomes)
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

## Running on test dataset
The test dataset consists of two #### genome assembly versions and a VCF with
SNPs found in the first chromosome of the reference genome. The VCF contains
the genotypes of 10 samples for 190,443 SNPs. It runs in 10 minutes using 20
Xeon processors from 2020. About 7 minutes is spent aligning the two genomes
with minimap2 to visualize the collinearity of the two genomes and 1 minute to
index the old genome for alignment with bwa. The rest of the steps take the
remaining two minutes.

For this test run, based on real data, the percentage of transfered SNPs is 99.58%.

Get and prepare test dataset with:
```
./01_scripts/util/get_test_dataset.sh
```

Run snplift with:
```
time ./snplift 02_infos/snplift_config.sh
```

## Running
### Prepare genomes
### Validate scaffold names
### Estimation of run time
Based on:
- Genome size
- Number of SNPs
- Number of samples (prob not necessary)
- Time factor compared to the 10min needed for the test run

### Run

## Results

## License

CC share-alike

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">SNPLift</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Eric Normandeau</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/enormandeau/SNPLift" rel="dct:source">https://github.com/enormandeau/SNPLift</a>.
