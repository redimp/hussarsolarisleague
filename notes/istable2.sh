#!/bin/bash

TRIALS="Panther Spider Crab Griffin Dragon Grasshopper Stalker Zeus"

while read line
do
	[ "$line" == "" ] && continue
	chassis=`echo $line | cut -d',' -f1`
	weight=`echo $line | cut -d',' -f2`
	trial=0
	if echo $TRIALS | grep -q "$chassis"; then
		trial=1
	fi
	if [ "$weight" -ge 20 -a "$weight" -le 35 ]; then class="Light";
	elif [ "$weight" -ge 40 -a "$weight" -le 55 ]; then class="Medium";
	elif [ "$weight" -ge 60 -a "$weight" -le 75 ]; then class="Heavy";
	elif [ "$weight" -ge 80 -a "$weight" -le 100 ]; then class="Assault";
       	fi
	echo "INSERT INTO \"chassis\" (name, weight, class, trial_available) VALUES ('${chassis}',${weight},'${class}',${trial});"
done < IS\ Chassis.txt
