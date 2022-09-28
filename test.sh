#!/bin/bash
echo "enter the value of a"
read a
echo "enter the value of b"
read b
if test "$a" = "$b"
then
echo " a is equal to b"
else
echo "a is not equal to b"
fi
