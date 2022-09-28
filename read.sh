#!/bin/bash

file="one.txt"
while read line;
do
echo $line
done < $file
echo "adding more content to the text file">>one.txt
echo "After appending the content"
cat one.txt

