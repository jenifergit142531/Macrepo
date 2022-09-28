#!/bin/bash

filename="one.txt"
if test -e $filename
then
echo "file exist"
else
echo "file not available"
fi
