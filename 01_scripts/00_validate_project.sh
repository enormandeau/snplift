#!/bin/bash
# Validate project before launching SNPLift

# Global variables
source $1

# Expected old genome exists
if ! [ -e "$OLD_GENOME" ]
then
    echo -e "\n"SNPLift ERROR: Old genome \("$OLD_GENOME"\) not found
    exit 1

else
    echo "- Old genome found"

fi

# Expected new genome exists
if ! [ -e "$NEW_GENOME" ]
then
    echo -e "\n"SNPLift ERROR: New genome \("$NEW_GENOME"\) not found
    exit 1

else
    echo "- New genome found"

fi

# Expected input variant file exists
if ! [ -e "$INPUT_FILE" ]
then
    echo -e "\n"SNPLift ERROR: Input file \("$INPUT_FILE"\) not found
    exit 1

else
    echo "- Input file found"

fi

# Chromosome/scaffold names in variant file are found in old genome
grep -v "^#" "$INPUT_FILE" | cut -f 1 | uniq | sort -Vu > seq_names_input.txt
grep "^>" "$OLD_GENOME" | cut -c 2- | cut -d " " -f 1 > seq_names_old_genome.txt
./01_scripts/util/validate_sequence_names.py seq_names_input.txt seq_names_old_genome.txt

# Function to compare version numbers
vercomp () {
    if [[ $1 == $2 ]]
    then
        return 0
    fi

    local IFS=.
    local i ver1=($1) ver2=($2)

    # fill empty fields in ver1 with zeros
    for ((i=${#ver1[@]}; i<${#ver2[@]}; i++))
    do
        ver1[i]=0
    done

    for ((i=0; i<${#ver1[@]}; i++))
    do
        if [[ -z ${ver2[i]} ]]
        then
            # fill empty fields in ver2 with zeros
            ver2[i]=0
        fi
        if ((10#${ver1[i]} > 10#${ver2[i]}))
        then
            return 1
        fi
        if ((10#${ver1[i]} < 10#${ver2[i]}))
        then
            return 2
        fi
    done

    return 0
}

# Validate that python3 is installed and used
command -v python3 >/dev/null 2>&1 ||
    {
        echo -e "\n"SNPLift ERROR: python3 is not installed
        echo
        exit 1;
    }

# Confirm that python3 version is high enough
python3_needed="3.5.0"
python3_version=$(python3 --version 2>&1 | head -1 | awk '{print $2}')

vercomp "$python3_version" "$python3_needed"

case $? in
    0)
        echo "- python3 is recent enough:"
        echo "    needed: $python3_needed""+; installed: $python3_version";;
    1)
        echo "- python3 is recent enough:"
        echo "    needed: $python3_needed""+; installed: $python3_version";;
    2)
        echo
        echo "/!\ WARNING /!\ "
        echo
        echo "python3 ($python3_version) is too old"
        echo "You need version $python3_needed""+ to run SNPLift"
        echo
        echo ">>> STOPPING SNPLift <<<"
        echo
        exit 1;;
esac

# validate scipy is available
command python -c "import scipy" >/dev/null 2>&1 ||
    {
        echo -e "\nSNPLift ERROR: scipy (Python module) is not installed"
        echo
        exit 1;
    }

# Validate that R is installed and used
command R -e "a=1" >/dev/null 2>&1 ||
    {
        echo -e "\n"SNPLift ERROR: R is not available
        echo
        exit 1;
    }

# Confirm that R version is high enough
R_needed="3.0.0"
R_version=$(R --version 2>&1 | head -1 | awk '{print $3}')

vercomp "$R_version" "$R_needed"

case $? in
    0)
        echo "- R is recent enough:"
        echo "    needed: $R_needed""+; installed: $R_version";;
    1)
        echo "- R is recent enough:"
        echo "    needed: $R_needed""+; installed: $R_version";;
    2)
        echo
        echo "/!\ WARNING /!\ "
        echo
        echo "R ($R_version) is too old"
        echo "You need version $R_needed""+ to run SNPLift"
        echo
        echo ">>> STOPPING SNPLift <<<"
        echo
        exit 1;;
esac

# Validate that parallel is installed and used
command -v parallel --version >/dev/null 2>&1 ||
    {
        echo -e "\n"SNPLift ERROR: parallel is not installed
        echo
        exit 1;
    }

# Confirm that parallel version is high enough
parallel_needed="20180101"
parallel_version=$(parallel --version 2>&1 | head -1 | awk '{print $3}')

vercomp "$parallel_version" "$parallel_needed"

case $? in
    0)
        echo "- parallel is recent enough:"
        echo "    needed: $parallel_needed""+; installed: $parallel_version";;
    1)
        echo "- parallel is recent enough:"
        echo "    needed: $parallel_needed""+; installed: $parallel_version";;
    2)
        echo
        echo "/!\ WARNING /!\ "
        echo
        echo "parallel ($parallel_version) is too old"
        echo "You need version $parallel_needed""+ to run SNPLift"
        echo
        echo ">>> STOPPING SNPLift <<<"
        echo
        exit 1;;
esac

# Validate that bash is installed and used
command -v bash >/dev/null 2>&1 ||
    {
        echo -e "\n"SNPLift ERROR: bash is not installed
        echo
        exit 1;
    }

# Confirm that bash version is high enough
bash_needed="4.0.0"
bash_version=$(bash --version 2>&1 | head -1 | awk '{print $4}' | cut -d "(" -f 1)

vercomp "$bash_version" "$bash_needed"

case $? in
    0)
        echo "- bash is recent enough:"
        echo "    needed: $bash_needed""+; installed: $bash_version";;
    1)
        echo "- bash is recent enough:"
        echo "    needed: $bash_needed""+; installed: $bash_version";;
    2)
        echo
        echo "/!\ WARNING /!\ "
        echo
        echo "bash ($bash_version) is too old"
        echo "You need version $bash_needed""+ to run SNPLift"
        echo
        echo ">>> STOPPING SNPLift <<<"
        echo
        exit 1;;
esac

# Validate that bwa is installed and used
command -v bwa >/dev/null 2>&1 ||
    {
        echo -e "\n"SNPLift ERROR: bwa is not installed
        echo
        exit 1;
    }

# Confirm that bwa version is high enough
bwa_needed="0.7.0"
bwa_version=$(bwa 2>&1 | grep Version | awk '{print $2}')

vercomp "$bwa_version" "$bwa_needed"

case $? in
    0)
        echo "- bwa is recent enough:"
        echo "    needed: $bwa_needed""+; installed: $bwa_version";;
    1)
        echo "- bwa is recent enough:"
        echo "    needed: $bwa_needed""+; installed: $bwa_version";;
    2)
        echo
        echo "/!\ WARNING /!\ "
        echo
        echo "bwa ($bwa_version) is too old"
        echo "You need version $bwa_needed""+ to run SNPLift"
        echo
        echo ">>> STOPPING SNPLift <<<"
        echo
        exit 1;;
esac

# Validate that samtools is installed and used
command -v samtools >/dev/null 2>&1 ||
    {
        echo -e "\n"SNPLift ERROR: samtools is not installed
        echo
        exit 1;
    }

# Confirm that samtools version is high enough
samtools_needed="1.10"
samtools_version=$(samtools version 2>&1 | head -1 | awk '{print $2}')

vercomp "$samtools_version" "$samtools_needed"

case $? in
    0)
        echo "- samtools is recent enough:"
        echo "    needed: $samtools_needed""+; installed: $samtools_version";;
    1)
        echo "- samtools is recent enough:"
        echo "    needed: $samtools_needed""+; installed: $samtools_version";;
    2)
        echo
        echo "/!\ WARNING /!\ "
        echo
        echo "samtools ($samtools_version) is too old"
        echo "You need version $samtools_needed""+ to run SNPLift"
        echo
        echo ">>> STOPPING SNPLift <<<"
        echo
        exit 1;;
esac
