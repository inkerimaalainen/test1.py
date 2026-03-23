#!/bin/bash
read -p "Введите свою массу(в кг): " m
read -p "Введите свой рост(в м): " h
bmi=$(awk "BEGIN {printf \"%.2f\", $m / ($h * $h)}")

echo "Ваш индекс массы тела: $bmi"
