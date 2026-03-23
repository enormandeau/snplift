#!/usr/bin/env Rscript

# Parse user input
rm(list=ls())
args = commandArgs(trailingOnly=TRUE)
input_file = args[1]
output_file = paste0(input_file, ".png")

# Load data
data = read.table(input_file)

# Create plot
png(width=1150, height=1150)

plot(data[,2], data[,4],
     pch=19,
     col="darkred",
     cex=0.4,
     main=paste0("Corresponding positions of ", nrow(data), " transfered SNP"),
     xlab="Position in genome 1",
     ylab="Position in genome 2")

dev.off()
