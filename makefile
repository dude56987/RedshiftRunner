install:
	#cp cron /etc/cron.d/redshiftRunner
	cp redshiftRunner.py /usr/bin/redshiftRunner
	cp redshiftRunnerGTK.py /usr/bin/redshiftRunnerGTK
	cp redshiftRunner_daemon.sh /usr/bin/redshiftRunner_daemon
	# copy over launcher
	cp redshiftRunner.desktop /usr/share/applications/redshiftRunner.desktop
	# copy over launcher to put in menu
	cp redshiftRunner.desktop /etc/xdg/autostart/redshiftRunner.desktop
	# make the scripts executable
	chmod +x /usr/bin/redshiftRunner
	chmod +x /usr/bin/redshiftRunnerGTK
	chmod +x /usr/bin/redshiftRunner_daemon
