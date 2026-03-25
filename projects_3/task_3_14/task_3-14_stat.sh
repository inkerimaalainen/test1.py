x#!/bin/bash
echo "---------------------"
echo "Сумма баллов: "
awk '{sum += $2} END {print sum}' students.txt
echo "---------------------"
echo "Средний по больнице: "
awk '{sum += $2; n ++} END {print sum/n}' students.txt
echo "---------------------"
echo "Максимальный балл: "
awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt
echo "---------------------"
