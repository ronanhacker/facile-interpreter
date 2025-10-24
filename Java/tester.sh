for filename in ./*.java
do
    javac "$filename"
done

errorsstill=0
numtests=$(ls ../Tests | wc -l)
let "numtests = $numtests + 1"

for i in $(seq 1 $numtests);
do
    echo "=== ${bold}Test $i${normal} ==="
    echo ""
    java facile.java "../Tests/Test$i.txt" 
    errorsinfile=$(java facile.java "../Tests/Test$i.txt" | grep -c 'ERROR.')
    let "errorsstill = $errorsstill + $errorsinfile"
    echo ""
done

if [ $errorsstill -gt 1 ]; then
    echo "There are $errorsstill tests that still return 'ERROR.'"
elif [ $errorsstill -eq 1 ]; then
    echo "There is 1 test that still returns 'Error.'"
else
    echo "No tests still return 'Error!'"
fi