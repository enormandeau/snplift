#!/bin/bash

echo -e "SNPlift: Removing intermediate files"
./01_scripts/util/cleanup_intermediate_files.sh

./01_scripts/util/get_test_dataset.sh

time ./snplift 02_infos/test_config.sh
