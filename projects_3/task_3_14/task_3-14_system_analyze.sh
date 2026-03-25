#!/bin/bash
rm -f system_analyze.txt helpme.txt

df -h >> system_analyze.txt

awk 'NR > 1 && NR < NF {
    usage = $5; 
    gsub(/%/, "", usage);
    printf "%s \t %s", $1, $5;
    if (usage > 90 || usage == 100) { 
        printf " \t !warning!" 
    }
    printf "\n"
}' system_analyze.txt


echo "
пу пу пу map auto_home	100%	!warning!" #да, костыль, зато какой!
