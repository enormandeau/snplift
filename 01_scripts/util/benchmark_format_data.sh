#!/bin/bash
# Format benchmark data for reporting

for i in 99_logfiles/*.log
do
    grep -P "^Start|CPUs|Transferable|Positions|^user|^End" "$i" |
        perl -pe 's/\n/ /' |
        awk '{print $3,$9,$7,100*$9/$7,$6,$12}' |
        perl -pe 's/ +/\t/g' |
        perl -pe 's/\d+_//g'
done | ./01_scripts/util/benchmark_get_elapsed_time.py > benchmark_data.tsv
