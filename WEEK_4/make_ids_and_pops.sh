#!/bin/bash
echo $@
echo $1
echo $2
for bc in $@; do
	cut -f 3 -d "," $bc | grep "_" &> $bc.ids.txt
	cut -f 3 -d "," $bc | grep "_" | cut -f 1,2 -d "_" &> $bc.pops.txt
done
