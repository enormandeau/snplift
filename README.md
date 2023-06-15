# SNPLift v1.0.0

## Lift over SNP positions to match a new reference genome.

SNPLift takes a tab-delimited file, for example a VCF, with locus positions
from a given genome and lifts over these positions so they match a new
reference genome. The goal is to rapidly leverage the availability of new
genomes without having to re-align all the sample reads and then call and
filter the loci again.

In the process, a small proportion of the loci are inevitably lost. However,
the transferred proportion is very high for genomes with low duplication
content and when both genome versions are fairly similar. For example, our test
run on real data gives a 99.63% transfers rate.

**NOTE**: Although SNPLift was designed primarily for VCFs containing SNP data,
any input file in which the two first columns contain chromosome names and
positions can be used. Lines beginning with a hash sign (`#`) are simply
transferred to the output file without modification and any column beyond the
first two are also left unchanged (there is an option to update SNP IDs in the
config file). As such, SNPLift will work with any marker type or even bed
files, as long as the two first columns contain chromosome and position
information and that there are other columns with informations to transfer.

**WARNING**: For local regions that differ between the two assemblies, a small
proportion of the SNPs (from 0.5 to 1% in our tests) will end up with an
approximate position. Further work will be done to improve this, but ultimately
the only way to guaranty that all the positions on the new genome are correct
is to re-align the reads and call the genotypes again.

See licence information at the end of this file.

## Citation

If you use SNPLift, please cite the following paper:

[https://www.biorxiv.org/content/10.1101/2023.06.13.544861v1](https://www.biorxiv.org/content/10.1101/2023.06.13.544861v1)

## Benchmark

When transferring millions of positions, once the genome is indexed, SNPLift
will typically transfer between 0.5 and 1 million positions per minute. For
example, 50M *Zea mays* SNPs were transferred in 53m53s, or about 0.98 million
SNPs transfered per minute. For datasets with less than 1M positions, using 1
to 10 CPUs is recommended. Above that, run time will decrease up to 40 CPUs,
but the overall efficiency is also reduced. Overall, using 10 CPUs is always a
good choice and values above 20 CPUs will be more wasteful of ressources, even
on large datasets. See article in the **Citation** section above for more
benchmark details.

SNP datasets and genomes used to benchmark SNPLift program can be found on Dryad:
[https://doi.org/10.5061/dryad.h9w0vt4nx](https://doi.org/10.5061/dryad.h9w0vt4nx)

## Installation

To use SNPLift, you will need a local copy of its repository. Different
releases can be [found here](https://github.com/enormandeau/SNPLift/tags)
under the `Tags` tab. It is recommended to always use the latest release or
even the development version. You can either download an archive of the latest
release at the above link or get the latest commit (recommended) with the
following git command:

```
git clone https://github.com/enormandeau/snplift
```

## Dependencies

To run SNPLift, you will need to have the following programs installed. To
facilitate installation, an effort has made to use only easy-to-install
programs, as well as avoid non standard libraries for Python and R code.
Only scipy is required for Python.

- SNPLift will only work on GNU Linux or OSX
- python 3.5+ and scipy
- R 3+ (ubuntu/mint: `sudo apt-get install r-base-core`)
- bash 4+
- [gnu parallel](https://www.gnu.org/software/parallel/)
- git (to clone this repository and the test dataset)
- bwa
- samtools
- minimap2 (optional, to visualize the collinearity of the two genomes)
- miniasm (optional, using minidot to visualize the collinearity of the two genomes)

## Running on test dataset

Before trying SNPLift on your data, we suggest running it on the prepared test
dataset. This will confirm that you have all the required dependencies.

The test dataset consists in the first chromosome from two different genome
assemblies from *Medicago truncatula* and a VCF with SNPs found in the first
chromosome of the reference genome. The VCF contains the genotypes of 10
samples for 190,443 SNPs. The test takes about 1m20s on 10 Xeon processors from
2016. About 1m is used to index the old genome for alignment with bwa. The rest
of the steps take about 18s.

You can run the full SNPLift test with:

```
./01_scripts/util/run_test.sh
```

## Preparation

- Install dependencies
- Download a copy of the SNPLift repository (see **Installation** above)
- Make sure that the chromosome names used in the file (eg: VCF) match EXACTLY
  those found in the `old_genome.fasta` file before any space character.
- Modify `02_infos/snplift_config.sh`

## Overview of SNPLift steps

During the analyses, the following steps are performed in this order:

- *Optional*: Visualize collinearity of the two genomes (slow, using minimap)
- Index new genome (can be skipped if already indexed)
- Get original coordinates
- Extract flanking sequences around SNPs from the old genome
- Map reads with bwa to new genome
- Extract features from alignments
- *Optional* (for debugging purposed): Visualize alignment features
- Filters based on alignment features
- Save some bad alignments if they are locally collinear with good ones
- Update coordinates
- Update input file (eg: VCF)

When using multiple CPUs, some of these steps are run on parallel.

## Running

Once SNPLift is installed and the dependencies are met, you need to do the
following:

1. Prepare your input files
1. Modify the config file
1. Launch SNPLift with:

```
time ./snplift 02_infos/snplift_config.sh
```

## Results

The output of SNPLift is a file (eg: VCF) in which the positions for which a
good alignment was found are transferred to the coordinates of a new reference
genome.

Optionally, if `CHECK_COLLINEARITY` is set to `1`, a dot plot collinearity
figure in .eps and .pdf formats is produced.

Optionally, if `SKIP_VISUALIZATION` is set to `0`, a figure showing some of the
features used for filtering the alignments is produced. This is used for
debugging purposes.

Some additinal parameter in the config file permit to do final corrections to
VCF files.

## Limitations

SNPLift works well when the two genome versions are more similar differences.
As the differences between the orthologous sequences increase, the proportion
of SNPs that can be transferred decreases. Whole or partial genome duplication
will also have an impact on the capacity to transfer SNPs between assemblies.

For SNPs with position within 300bp of scaffold ends (or the value of
WINDOW_LENGTH in the configuration file), the reported position in the new file
(eg: VCF) can be slightly off.

In our tests, about 1% of the transfered positions were not exact (see
reference in the Citation section).

## License

CC share-alike

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">SNPLift</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">[Eric Normandeau](https://github.com/enormandeau)</span> is licensed under a  
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
