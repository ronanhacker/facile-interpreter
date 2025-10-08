for filename in ./*.java
do
    javac "$filename"
done

for file in DemoPrograms/*
do
    echo "$file"
    java facile.java "$file"
done