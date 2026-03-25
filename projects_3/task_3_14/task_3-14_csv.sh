#!/bin/bash
sed -i ''  's/,/ /g' data.csv
echo "Ассортимент: "
awk '{print $2}' data.csv
printf '\n'
echo "Буржуйские: "
awk '$3 > 20 {print $2}' data.csv
printf '\n'
echo "Общая стоимость: "
awk '{sum += $3} END {print sum}' data.csv
