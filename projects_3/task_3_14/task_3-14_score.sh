#!/bin/bash
awk '$2 > 80 {print $1}' students.txt
printf "\n"
awk '$2 < 70 {print $1}' students.txt
printf "\n"
awk 'NR == 1 {print $0}' students.txt
