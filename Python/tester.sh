#!/bin/bash

errorsstill=0
numtests=$(ls ../tests | wc -l)
let "numtests = $numtests + 1"

for i in $(seq 1 $numtests);
do
    echo "=== ${bold}Test $i${normal} ==="
    echo ""
    python3 Facile.py "../Tests/Test$i.txt" 
    errorsinfile=$(python3 Facile.py "../Tests/Test$i.txt" | grep -c 'ERROR.')
    let "errorsstill = $errorsstill + $errorsinfile"
    echo ""
done

if [ $errorsstill -gt 1 ]; then
    echo "There are $errorsstill tests that still return 'ERROR.'"
elif [ $errorsstill -eq 1 ]; then
    echo "There is 1 test that still returns 'ERROR.'"
else
    echo "No tests still return 'ERROR!'"
fi