#!/bin/bash
#Description
#To get the highest life expectancy across years

#usage: ./script.sh
echo "Input"
input=$1

#define an input varaible
#input=Data/ByCountry/Mexico.txt
#output=HighestLE2_Mexico.txt

#command to get highest life expectancy from Mexico.txt
cut -f1,3,4 $input | sort -nk4 | tail -n1
