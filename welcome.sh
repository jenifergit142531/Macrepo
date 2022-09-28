#!/bin/bash

function greeting()
{
str="hello $name"
echo $str
}

echo "Enter the name "
read name

val=$(greeting)
echo " Return value of the function is $val"
