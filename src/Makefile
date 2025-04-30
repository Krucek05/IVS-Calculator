TEAM = xrucekk00_xfigurf00_xkucikm00_xseryra00
INSTFLG = -m 0755
NAME-VERSION = sudo.apt.install.calculator-1.0

.PHONY: all depend run clean doc pack stddev install create_debian create_dpkg test stddev

all: stddev depend

depend:
	sudo apt install python3-pyqt6

run:
	python3 calculator_GUI.py

clean:
	-cd ../ && rm -r doc
	-cd ../../ && rm -r $(TEAM)
	-cd ../installer && rm -r usr *.buildinfo *.changes *.deb $(NAME-VERSION)

doc: Doxyfile
	-cd ../ && rm -r doc
	doxygen $^

test:
	python3 -m unittest math_library_tests.py

pack: clean
	cd ../../ && mkdir $(TEAM)
	cd ../../$(TEAM) && mkdir repo && cp -a ../IVS-Calculator/* ./repo
	cd ../../$(TEAM) && cp -a ../IVS-Calculator/.git ./repo
	make install
	mkdir -p ../../$(TEAM)/installer
	cd ../../$(TEAM)/installer && cp -a ../../IVS-Calculator/installer/sudo.apt.install.calculator_1.0_amd64.deb ./
	make doc
	cd ../../$(TEAM) && cp -a ../IVS-Calculator/doc ./
	cd ../../ && zip -r $(TEAM).zip ./$(TEAM)

create_debian:
	-cd ../installer && rm -r $(NAME-VERSION)
	mkdir -p ../installer/$(NAME-VERSION)
	cd ../installer/$(NAME-VERSION) && dh_make -e ivs@vutbr.cz -n -s -y -c gpl3
	cd ../installer/$(NAME-VERSION)/debian && cp -a -f ../../../src/installer-config/control ./
	cd ../installer/$(NAME-VERSION)/debian && cp -a -f ../../../src/installer-config/copyright ./
	cd ../installer/$(NAME-VERSION)/debian && cp -a -f ../../../src/installer-config/install ./

create_dpkg:
	-cd ../installer && rm -r usr
	mkdir -p ../installer/usr/share/sudo_apt_install_calculator
	mkdir -p ../installer/usr/share/applications
	mkdir -p ../installer/usr/share/pixmaps
	mkdir -p ../installer/usr/bin
	install $(INSTFLG) math_library.py ../installer/usr/share/sudo_apt_install_calculator
	install $(INSTFLG) sudo_apt_install_calculator.desktop ../installer/usr/share/applications
	install $(INSTFLG) saicalculator.xpm ../installer/usr/share/pixmaps
	install $(INSTFLG) calculator_GUI.py ../installer/usr/share/sudo_apt_install_calculator/
	install $(INSTFLG) saicalculator ../installer/usr/bin/
	install $(INSTFLG) profiling.py ../installer/usr/share/sudo_apt_install_calculator/
	install $(INSTFLG) config.py ../installer/usr/share/sudo_apt_install_calculator/
	install $(INSTFLG) help.py ../installer/usr/share/sudo_apt_install_calculator/
	install $(INSTFLG) stddev ../installer/usr/bin/
	install $(INSTFLG) sairemove ../installer/usr/bin/
	cd ../installer/$(NAME-VERSION) && dpkg-buildpackage -rfakeroot -uc -b

install: create_debian create_dpkg

stddev:
	chmod +x stddev
	sudo apt install python3

stddev-test: 
	python3 profiling.py < ../profiling/Test_files/10num.txt
	python3 profiling.py < ../profiling/Test_files/100num.txt
	python3 profiling.py < ../profiling/Test_files/1000num.txt
	python3 profiling.py < ../profiling/Test_files/10000num.txt
	python3 profiling.py < ../profiling/Test_files/100000num.txt
	python3 profiling.py < ../profiling/Test_files/1000000num.txt