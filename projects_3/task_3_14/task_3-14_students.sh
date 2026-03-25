#!/bin/bash
awk '{print $1}' students.txt
printf "\n"
awk '{print $2}' students.txt
printf "\n"
awk '{print NR, $1'} students.txt
