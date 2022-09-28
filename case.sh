#!/bin/bash

echo "Enter the lottery number"
read lucky
case $lucky in
100)
echo "You got third prize";;
1001)
echo "You got second prize";;
999)
echo "Congratulations!!! you won first price in lottery";;
*)
echo "Sorry,Better luck next time";;
esac
