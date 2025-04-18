TEAM = xrucekk00_xfigurf00_xkucikm00_xseryra00

.PHONY: all depend run clean doc pack stddev

all: depend

depend:
	sudo apt install python3-pyqt6

run: depend
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

stddev:
	python3 profiling.py < ../profiling/Test_files/10num.txt
	python3 profiling.py < ../profiling/Test_files/100num.txt
	python3 profiling.py < ../profiling/Test_files/1000num.txt
	python3 profiling.py < ../profiling/Test_files/10000num.txt
	python3 profiling.py < ../profiling/Test_files/100000num.txt
	python3 profiling.py < ../profiling/Test_files/1000000num.txt
	python3 profiling.py < ../profiling/Test_files/10000000num.txt
