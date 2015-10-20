#! /bin/bash
# run the daemon component of the software
# if ran with a currently running daemon dont relaunch
# check if redshiftRunner is running, if not launch it, this results in a infinte loop
if [ -f /usr/bin/redshiftRunner ]; then
	while ! pgrep -xc redshiftRunner;do
		redshiftRunner	
	done; 
fi;

