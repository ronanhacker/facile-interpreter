for filename in ./*.java
do
    javac "$filename"
done

for i in $(seq 1 17);
do
    echo "=== ${bold}Test $i${normal} ==="
    echo ""
    java facile.java "Tests/Test$i.txt"
    echo ""
done