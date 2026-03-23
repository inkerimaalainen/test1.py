#!/bin/zsh

for i in {1..10}; do
	touch "test$i.txt"
	echo "done"
	sleep 0.1
done

while [ $i -gt 0 ]; do
	echo $i
	rm "test$i.txt"
	$((i-=1))
	sleep 0.1
done
