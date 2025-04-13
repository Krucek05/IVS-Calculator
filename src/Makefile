TEAM = xrucekk00_xfigurf00_xkucikm00_xseryra00

.PHONY: all depend run clean doc

all:

depend:
	pip3 install pyqt6

run:
	python3 calculator_GUI.py

clean:
	-cd ../ && rm -r doc
	-cd ../../ && rm -r $(TEAM)

doc: Doxyfile
	doxygen $^

pack:
	cd ../../ && mkdir $(TEAM)
	cd ../../$(TEAM) && mkdir repo && cp -a ../IVS-Calculator/* ./repo
	cd ../../$(TEAM) && cp -a ../IVS-Calculator/installer ./
	make doc
	cd ../../$(TEAM) && cp -a ../IVS-Calculator/doc ./
	cd ../../ && zip -r $(TEAM).zip ./$(TEAM)

