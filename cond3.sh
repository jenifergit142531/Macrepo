#!/bin/bash
echo " Enter your score"
read score

if [[ ($score -eq 15 || $score -eq 50)]]
then
echo "You won the game"
else
echo " you lost the game"
fi
