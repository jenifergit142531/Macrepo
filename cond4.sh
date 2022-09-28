#!/bin/bash

echo "Enter your lottery number "
read lucky

if [ $lucky -eq 100 ];
then
echo "You won third price of Rs.500"
elif [ $lucky -eq 1001 ];
then
echo "You won second prize of Rs.2000"
elif [ $lucky -eq 999 ];
then
echo "You won first prize in lottery!!!!congratulations"
else
echo "Sorry,better luck next time"
fi

