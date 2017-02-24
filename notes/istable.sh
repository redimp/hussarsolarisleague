#!/bin/bash

TRIALS="Panther Spider Crab Griffin Dragon Grasshopper Stalker Zeus"

while read line
do
	[ "$line" == "" ] && continue
	x=`echo $line | sed -e's#,#\</td\>\<td\>#'`
	chassis=`echo $line | cut -d',' -f1`
	if echo $TRIALS | grep -q "$chassis"; then
		echo "<tr><td>${x}</td><td><input type=\"checkbox\"></td><td><input type=\"checkbox\"></td></tr>"
	else
		echo "<tr><td>${x}</td><td><input type=\"checkbox\"></td><td>&nbsp;</td></tr>"
	fi
done < IS\ Chassis.txt
