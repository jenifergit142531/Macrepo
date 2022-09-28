#!/bin/bash

echo "enter the number"
read n
for (( i=0; i<n; i++ ))
do
echo "counting : $i"
done




valid=true
count=1
while [ $valid ]
do
echo $count
if [ $count -eq 5 ];
then
break
fi
((count++))
done'
