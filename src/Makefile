TEAM = xrucekk00_xfigurf00_xkucikm00_xseryra00
NAME = sudo_apt_install_calculator
INSTFLG = -m 0755

.PHONY: all depend run clean doc pack stddev install

all: depend

depend:
	sudo apt install python3-pyqt6.sip

run:
	python3 calculator_GUI.py

clean:
	-cd ../ && rm -r doc
	-cd ../../ && rm -r $(TEAM)
	-cd ../installer && rm -r usr *.buildinfo *.changes *.deb

doc: Doxyfile
	doxygen $^

pack:
	cd ../../ && mkdir $(TEAM)
	cd ../../$(TEAM) && mkdir repo && cp -a ../IVS-Calculator/* ./repo
	cd ../../$(TEAM) && cp -a ../IVS-Calculator/installer ./
	make doc
	cd ../../$(TEAM) && cp -a ../IVS-Calculator/doc ./
	cd ../../ && zip -r $(TEAM).zip ./$(TEAM)

install:
	mkdir -p ../installer/usr/share/$(NAME)
	mkdir -p ../installer/usr/share/applications
	mkdir -p ../installer/usr/share/pixmaps
	mkdir -p ../installer/usr/bin
	install $(INSTFLG) math_library.py ../installer/usr/share/$(NAME)
	install $(INSTFLG) sudo_apt_install_calculator.desktop ../installer/usr/share/applications
	install $(INSTFLG) saicalculator.xpm ../installer/usr/share/pixmaps
	install $(INSTFLG) calculator_GUI.py ../installer/usr/bin/
	install $(INSTFLG) saicalculator ../installer/usr/bin/
	cd ../installer/sudo.apt.install.calculator-1.0 && dpkg-buildpackage -rfakeroot -uc -b

stddev: 
	python3 profiling.py < ../profiling/Test_files/10num.txt
	python3 profiling.py < ../profiling/Test_files/100num.txt
	python3 profiling.py < ../profiling/Test_files/1000num.txt
	python3 profiling.py < ../profiling/Test_files/10000num.txt
	python3 profiling.py < ../profiling/Test_files/100000num.txt
	python3 profiling.py < ../profiling/Test_files/1000000num.txt