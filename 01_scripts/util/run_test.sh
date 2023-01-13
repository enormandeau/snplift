#!/bin/bash

echo -e "SNPlift: Removing intermediate files\n"
./01_scripts/util/cleanup_itermediate_files.sh

./01_scripts/util/get_test_dataset.sh

time ./snplift 02_infos/snplift_config.sh
