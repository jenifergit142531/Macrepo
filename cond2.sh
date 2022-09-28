#!/bin/bash
echo "Enter the username :"
read username
echo "Enter the password :"
read password

if [[ ($username == "jeni" && $password == "secret" )]];
then
echo "Valid user"
else
echo "Invalid user"
fi
