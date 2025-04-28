TEAM = xrucekk00_xfigurf00_xkucikm00_xseryra00
INSTFLG = -m 0755
NAME-VERSION = sudo.apt.install.calculator-1.0

.PHONY: all depend run clean doc pack stddev install create_debian create_dpkg

all: depend

depend:
	sudo apt install python3-pyqt6

run:
	python3 calculator_GUI.py

clean:
	-cd ../ && rm -r doc
	-cd ../../ && rm -r $(TEAM)
	-cd ../installer && rm -r usr *.buildinfo *.changes *.deb $(NAME-VERSION)

doc: Doxyfile
	doxygen $^

pack:
	cd ../../ && mkdir $(TEAM)
	cd ../../$(TEAM) && mkdir repo && cp -a ../IVS-Calculator/* ./repo
	cd ../../$(TEAM) && cp -a ../IVS-Calculator/installer ./
	make doc
	cd ../../$(TEAM) && cp -a ../IVS-Calculator/doc ./
	cd ../../ && zip -r $(TEAM).zip ./$(TEAM)

create_debian:
	-cd ../installer && rm -r $(NAME-VERSION) 
	mkdir -p ../installer/$(NAME-VERSION)
	cd ../installer/$(NAME-VERSION) && dh_make -e ivs@vutbr.cz -n -s -y -c gpl3
	cd ../installer/$(NAME-VERSION)/debian && cp -a -f ../../installer-config/control ./
	cd ../installer/$(NAME-VERSION)/debian && cp -a -f ../../installer-config/copyright ./
	cd ../installer/$(NAME-VERSION)/debian && cp -a -f ../../installer-config/install ./

create_dpkg:
	-cd ../installer && rm -r usr
	mkdir -p ../installer/usr/share/sudo_apt_install_calculator
	mkdir -p ../installer/usr/share/applications
	mkdir -p ../installer/usr/share/pixmaps
	mkdir -p ../installer/usr/bin
	install $(INSTFLG) math_library.py ../installer/usr/share/sudo_apt_install_calculator
	install $(INSTFLG) sudo_apt_install_calculator.desktop ../installer/usr/share/applications
	install $(INSTFLG) saicalculator.xpm ../installer/usr/share/pixmaps
	install $(INSTFLG) calculator_GUI.py ../installer/usr/bin/
	install $(INSTFLG) saicalculator ../installer/usr/bin/
	install $(INSTFLG) profiling.py ../installer/usr/bin/
	install $(INSTFLG) saiprofile ../installer/usr/bin/
	cd ../installer/$(NAME-VERSION) && dpkg-buildpackage -rfakeroot -uc -b

install: create_debian create_dpkg

stddev: 
	python3 profiling.py < ../profiling/Test_files/10num.txt
	python3 profiling.py < ../profiling/Test_files/100num.txt
	python3 profiling.py < ../profiling/Test_files/1000num.txt
	python3 profiling.py < ../profiling/Test_files/10000num.txt
	python3 profiling.py < ../profiling/Test_files/100000num.txt
	python3 profiling.py < ../profiling/Test_files/1000000num.txt