# VCF update reference
ReCoordVCF
VCFupdate
Pupdate
UpdateCoord
ReCoordinate

# WARNING !
Some SNPs pass the filters but are lost at the very last step. I suspect their
positions are not correct in my files (reverse comp?)

# Method
- Validate genome collinearity with global alignment (minimap)
- Extract flanking sequences around SNPs (100bp on each side)
- Get original coordinates
- Map reads with bwa (keep best hit)
- Get new coordinates
- Filters based on alignment (detail them)
- Recuperate bad alignments if locally collinear
- Update coordinates
- Update VCF
