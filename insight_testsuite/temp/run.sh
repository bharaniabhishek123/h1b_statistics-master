#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#

file1="./output/top_10_occupations.txt"

if [ -f $file1 ] ; then
    rm $file1
    echo "old output file $file1 deleted"
fi

file2="./output/top_10_states.txt"

if [ -f $file2 ] ; then
    rm $file2
    echo "old output file $file2 deleted"    
fi


echo "Running h1b_counting now..."
python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
echo "Finished executing h1b_counting, check output folder for results..."

