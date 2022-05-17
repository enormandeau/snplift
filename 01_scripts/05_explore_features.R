# Explore extracted features to help score the alignments
# Facultative:
#   The default values used by the pipeline should transfer well to different projects

# Cleanup
rm(list=ls())

# Libraries
library(data.table)
library(scales)

# Load data
d = fread("../positions.features")

# Subset columns
dd = d[, c("QueryName", "MappingFlag", "MappingQuality", "Deletion", "Hardclip", "Insertion", "Match", "Softclip", "Complexity", "NumNs", "NumDiff", "AlignmentScore", "SuboptimalScore", "NumSuppAlign", "SuppAlignMinDiff")]

# Explore subsets
subset = dd[dd$MappingFlag < 2000,
            -c("QueryName", "MappingFlag", "Hardclip")]


subset = dd[dd$MappingFlag < 2000 &
              dd$MappingQuality >= 10 &
              (dd$Match + dd$Softclip) >= 180 & # Accept 10% de moins que la longueur de la séquence
              dd$NumDiff <= 10 &
              (dd$Softclip - 10) / (dd$NumNs + 1) <= 1.5 &
              dd$Softclip <= 50 &
              dd$SuppAlignMinDiff >= 4, 
              -c("QueryName", "MappingFlag", "Hardclip")]

# Plot variables of interest
set.seed(123)
subset.random = subset[sample(nrow(subset), 2000)]
plot(subset.random, col="#00000011", pch=19)
