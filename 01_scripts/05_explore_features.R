# Explore extracted features to help score the alignments
# Facultative:
#   The default values used by the pipeline should transfer well to different projects

# Cleanup
rm(list=ls())

# Libraries
library(data.table)
library(scales)

# Load data
d = fread("06_liftover/positions.features")

# Subset columns
dd = d[, c("QueryName", "MappingFlag", "MappingQuality", "Match", "Softclip", "NumNs", "NumDiff", "NumSuppAlign", "SuppAlignMinDiff")]

# Explore subsets
subset = dd[dd$MappingFlag < 2000,
            -c("QueryName", "MappingFlag")]

# Filters below use values that remove almost nothing (except MappingFlags above 2000)
# Modify these values to visualize the effect of changing the filters.
# NOTE: This is for visual exploration only. Modify `02_infos/snplift_config.sh` to
# actually modify SNPLift's behaviour

subset = dd[dd$MappingFlag < 2000 &
              dd$MappingQuality >= 0 &  # Suggested: 10
              (dd$Match + dd$Softclip) >= 0 &  # Suggested: 90% of sequence length
              dd$NumDiff <= 200 &  # Suggested: 5-10% of sequence length
              (dd$Softclip - 10) / (dd$NumNs + 1) <= 99999999 &  # Suggested: 1.5
              dd$Softclip <= 200 &  # Suggested: 25% of sequence length
              dd$SuppAlignMinDiff >= 0,  # Suggested 2% of sequence length
              -c("QueryName", "MappingFlag")]

# Plot variables of interest
set.seed(123)
subset.random = subset[sample(nrow(subset), min(nrow(subset), 10000))]

png("positions.features.png", width=1000, height=1000)
plot(subset.random, col="#00000011", pch=19)
dev.off()
