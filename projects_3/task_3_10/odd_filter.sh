#!/bin/zsh

for i in {1..20}; do
        if [ $i -eq 15 ]; then
                echo "Я устал, Босс..."
                break
        fi

	if [ $((i % 2)) -ne 0 ]; then
		echo $i
		continue
	fi
done
	
