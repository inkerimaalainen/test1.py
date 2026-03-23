#!/bin/bash
#каюсь, вайбкодил, но, блин, какой код
printf "%-19s %7s %7s %7s %7s\n" "Файл" "A" "T" "G" "C"
for file in *.fasta; do
	if [[ -s "$file" ]]; then
		seq=$(grep -v "^>" "$file" | tr -d '\n' | tr '[:lower:]' '[:upper:]')
       		A=$(echo "$seq" | grep -o "A" | wc -l)
       		T=$(echo "$seq" | grep -o "T" | wc -l)
       		G=$(echo "$seq" | grep -o "G" | wc -l)
	        C=$(echo "$seq" | grep -o "C" | wc -l)
		printf "%-15s %7d %7d %7d %7d\n" "$file" "$A" "$T" "$G" "$C"
	fi
done

