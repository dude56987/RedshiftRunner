help:
	echo 'Run "sudo make install" to install the program'
	echo 'Run "sudo make run" to run the program'
	echo 'Run "sudo make uninstall" to uninstall the program'
install: build
	sudo gdebi --non-interactive redshiftRunner_UNSTABLE.deb
run:
	python redshiftRunner.py
uninstall:
	sudo apt-get purge redshiftRunner
build: 
	sudo make build-deb;
build-deb:
	# make directories
	mkdir -p debian/DEBIAN
	mkdir -p debian/usr/bin
	mkdir -p debian/usr/share/applications
	mkdir -p debian/etc/xdg/autostart
	mkdir -p ./debian/usr/share/pixmaps/
	# copy over launcher so it will show in the menu
	cp redshiftRunner.desktop ./debian/usr/share/applications/redshiftRunner.desktop
	# copy over launcher to autostart on user login
	cp redshiftRunner.desktop ./debian/etc/xdg/autostart/redshiftRunner.desktop
	# copy icon to system
	cp redshift.svg ./debian/usr/share/pixmaps/redshift.svg
	# copy over executables
	cp redshiftRunner.py ./debian/usr/bin/redshiftRunner
	cp redshiftRunnerGTK.py ./debian/usr/bin/redshiftRunnerGTK
	cp redshiftRunner_daemon.sh ./debian/usr/bin/redshiftRunner_daemon
	# make the scripts executable
	chmod +x ./debian/usr/bin/redshiftRunner
	chmod +x ./debian/usr/bin/redshiftRunnerGTK
	chmod +x ./debian/usr/bin/redshiftRunner_daemon
	# create the md5sums file
	find ./debian/ -type f -print0 | xargs -0 md5sum > ./debian/DEBIAN/md5sums
	# cut filenames of extra junk
	sed -i.bak 's/\.\/debian\///g' ./debian/DEBIAN/md5sums
	sed -i.bak 's/\\n*DEBIAN*\\n//g' ./debian/DEBIAN/md5sums
	sed -i.bak 's/\\n*DEBIAN*//g' ./debian/DEBIAN/md5sums
	rm -v ./debian/DEBIAN/md5sums.bak
	# figure out the package size
	du -sx --exclude DEBIAN ./debian/ > Installed-Size.txt
	# copy over package data
	cp -rv .debdata/. debian/DEBIAN/
	# fix permissions in package
	chmod -Rv 775 debian/DEBIAN/
	chmod -Rv ugo+r debian/
	chmod -Rv go-w debian/
	chmod -Rv u+w debian/
	# build the package
	dpkg-deb --build debian
	cp -v debian.deb redshiftRunner_UNSTABLE.deb
	rm -v debian.deb
	rm -rv debian
