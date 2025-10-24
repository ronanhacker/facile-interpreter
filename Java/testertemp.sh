for filename in ./*.java
do
    javac "$filename"
done

errorsstill=0
for file in DemoPrograms/*
do
    echo "$file"
    java facile.java "$file"
    errorsinfile=$(java facile.java $file | grep -c 'ERROR.')
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