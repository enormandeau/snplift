# SNPLift v0.6.2

## Lift over SNP positions to match a new reference genome.

SNPLift takes a tab-delimited file, for example a VCF file, with locus
positions from a given genome and lifts over these positions so they match a
new reference genome. The goal of the procedure is to rapidly leverage the
availability of a new genome without having to re-align all the sample reads
and then call and filter the loci.

In the process, a proportion of the loci are inevitably lost. However, the
transferred proportion is very high for genomes with low duplication content and
when both genome versions are similar. Our test run on real data gives a 99.87%
transfers rate.

**NOTE**: Although SNPLift was designed primarily for VCFs containing SNP data,
any input file in which the two first columns contain chromosome names and
positions can be used. Lines beginning with a hash sign (`#`) are simply
transferred to the output file without modification and any column beyond the
first two are also left unchanged. As such, SNPLift will work with any marker
type or even bed file, as long as the two first columns contain chromosome and
position information and that there are other columns with informations to
transfer.

**WARNING**: In regions that differ between the two assemblies, a small
proportion of SNPs will end up with an approximate position. Ultimately, the
only way to guaranty that all the positions on the new genome are correct is to
re-align the reads and call the genotypes again.

See licence information at the end of this file.

## Citation

If you use SNPLift, please cite the following paper:

*TODO* Add bioRxiv link and update to v1.0.0

## Benchmark

When transferring millions of positions, once the genome is indexed, SNPLift
will typically transfer between 0.5 and 1 million positions per minute. For
example, 50M *Zea mays* SNPs were transferred in 53m06s. For datasets with less
than 1M positions, using 1 to 10 CPUs is recommended. Above that, run time will
decrease up to 40 CPUs, but the overall efficiency is also reduced. Overall,
using 10 CPUs is always a good choice and values above 20 CPUs will be quite
wasteful, even on large datasets. See article in the **Citation** section
above for more benchmark details.

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

During the analyses, the following steps are performed:

- *Optional*: Visualize collinearity of the two genomes
- Index new genome (can be skipped if already indexed)
- Get original coordinates
- Extract flanking sequences around SNPs from the old genome (100bp on each side)
- Map reads with bwa to new genome
- Extract features from alignments
- *Optional* (for debugging purposed): Visualize alignment features
- Filters based on alignment features
- Save some bad alignments if they are locally collinear with good ones
- Update coordinates
- Update input file (eg: VCF)

When using multiple CPUs, some of these steps are run on parallel on portions
of the dataset.

## Running

Once SNPLift is installed and the dependencies are met, you need to do the
following:

1. Prepare your input files input files
1. Modify the config file
1. Launch SNPLift:

```
time ./snplift 02_infos/snplift_config.sh
```

## Results

The output of SNPLift is a file (eg: VCF) in which the positions for which a
good alignment was found are transferred to the coordinates of a new reference
genome.

Optionaly, if `CORRECT_VCF` is set to `1`, column 3 of the VCF containing locus
IDs will be recomputed from columns 1 and 2, alleles for loci that map in
the reverse orientation in the new genome will be reverse complemented, and
only one locus will be retain if multiple loci map in the same position.

Optionally, if `CHECK_COLLINEARITY` is set to `1`, a collinearity figure in
.eps and .pdf formats is produced.

Optionally, if `SKIP_VISUALIZATION` is set to `0`, a figure showing some of the
features used for filtering the alignments is produced. This is used mainly for
debugging purposes.

## Limitations
SNPLift works well when the two genome versions are more similar differences.
As the differences between the orthologous sequences increase, the proportion
of SNPs that can be transferred will go down. Whole or partial genome
duplication will also have an impact on the capacity to transfer SNPs between
assemblies.

For SNPs with position within 100bp (or the value of WINDOW_LENGTH in the
configuration file), the reported position in the new file (eg: VCF) will be
slightly off.  Measures are taken to correct for this at the beginning of the
scaffolds and for alignments with some soft clipping but SNPs at the end of
scaffolds may be off by up to WINDOW_LENGTH nucleotides.

## License

CC share-alike

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">SNPLift</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">[Eric Normandeau](https://github.com/enormandeau)</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
