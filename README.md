# SNPLift v0.4.0

Lift over SNP postions from a VCF to match a new reference genome.

## Description

SNPLift takes a VCF with locus positions from a given genome and lifts over
these positions so they match a new reference genome. The goal of the procedure
is to rapidly leverage the availability of a new genome without having to
re-align all the sample reads and then call and filter the loci.

In the process, a proportion of the loci are inevitably lost. However, the
transfered proportion is very high for genomes with low duplication content and
when both genome versions are similar. Our test run on real data gives a 99.58%
tranfers rate.

**WARNING** Ultimately, the only way to guaranty that all the positions on the
new genome are correct is to re-align the reads and call the genotypes again.

See licence information at the end of this file.

## Benchmark
*TODO* And give examples of transfer rates for different genomes

## Installation

To use SNPLift, you will need a local copy of its repository. Different
releases can be [found here](https://github.com/enormandeau/SNPLift/releases).
It is recommended to always use the latest release or even the developpment
version. You can either download an archive of the latest release at the above
link or get the latest commit (recommended) with the following git command:

```
git clone https://github.com/enormandeau/snplift
```

## Dependencies

To run SNPLift, you will need to have the following programs installed.

- SNPLift will only work on GNU Linux or OSX
- python 3.5+
- R 3+ (ubuntu/mint: `sudo apt-get install r-base-core`)
- bash 4+
- [gnu parallel](https://www.gnu.org/software/parallel/)
- git (to clone this repository and the test dataset)
- bwa
- samtools
- minimap2 (to visualize the collinearity of the two genomes)
- miniasm (for minidot, to visualize the collinearity of the two genomes)

## Running on test dataset
Before trying SNPLift on your data, we suggest running it on the prepared test
dataset. This will confirm that you have all the required dependencies.

The test dataset consists in the first chromosome from two different genome
assembles from *<SPECIES>* and a VCF with SNPs found in the first chromosome of
the reference genome. The VCF contains the genotypes of 10 samples for 190,443
SNPs. The test takes about 6m20s on 10 Xeon processors from 2020. About 5m10s are
spent aligning the two genomes with minimap2 to visualize collinearity of
the two versions and 30s to index the old genome for alignment with bwa.
The rest of the steps take the remaining 40s.

For this test run, based on real data, 99.57% of the SNPs are transfered.

You can run the full SNPlift test with:
```
./01_scripts/util/run_test.sh
```

## Preparation

- Install dependencies
- Download a copy of the SNPLift repository (see **Installation** above)
- Make sure that the chromosome names used in the VCF match EXACTLY those found
  in the `old_genome.fasta` file before any space character.

## Overview of SNPLift steps

During the analyses, the following steps are performed:

- Visualize collinearity of the two genomes
  - *TODO* report proportion of bases in collinear sections instead of number of bases
- Index new genome
- Get original coordinates
- Extract flanking sequences around SNPs (100bp on each side)
- Map reads with bwa
- Extract features from alignments
- Visualize alignment features
- Filters based on features
  - *TODO* Detail filters
- Recuperate some bad alignments if they are locally collinear with good ones
- Update coordinates
- Update VCF

## Running

### Run
Once SNPlift is installed and the dependencies are met and that your input and
config files are prepared, launch SNPLift with:

```
time ./snplift 02_infos/snplift_config.sh
```

## Results
*TODO*

## Limitations
SNPLift works well when the two genome versions are more similar differences.
As the differences between the orthologous sequences increase, the proportion
of SNPs that can be transfered will go down. Whole or partial genome
duplication will also have an impact on the capacity to transfer SNPs between
assemblies.

For SNPs with position within 100bp (or the value of WINDOW_LENGTH in the
configuration file), the reported position in the new VCF will be slightly off.
Measures are taken to correct for this at the beginning of the scaffolds and
for alignments with some soft cliping but SNPs at the end of scaffolds may be
off by up to WINDOW_LENGTH nucleotides.

## License

CC share-alike

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">SNPLift</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">[Eric Normandeau](https://github.com/enormandeau)</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/enormandeau/SNPLift" rel="dct:source">https://github.com/enormandeau/SNPLift</a>.
