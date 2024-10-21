#!/bin/bash
read -p "enter 1st no:" num1
read -p "enter 2nd no:" num2
read -p "enter 3rd no:" num3
smallest=$num1
if [ $num2 -lt $smallest ];then
    smallest=$num2
fi

if [ $num3 -lt $smallest ];then
    smallest=$num3
fi

echo "the smallest  no is :$smallest"


