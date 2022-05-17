# SNPTransfer

Transfer SNP postions in a VCF to match a new reference genome, without alignment

# Method
## Preparation
- Validate genome collinearity with global alignment (minimap)

## SNPTranfer
- Get original coordinates
- Extract flanking sequences around SNPs (100bp on each side)
- Map reads with bwa (keep best hit)
- Get new coordinates
- Filters based on alignment (detail them)
- Recuperate bad alignments if locally collinear
- Update coordinates
- Update VCF

## Test dataset

# TODO Licence
