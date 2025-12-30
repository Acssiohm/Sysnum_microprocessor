CAROTTE_PATH = ../carotte.py/carotte.py # Mettez le chemin relatif vers votre carotte.py 
PYTHON_INTERPRETER = python3 # Si ça marche pas chais vous, essayez avec "python" ou "py"
SIMULATOR = ./../tp1/netlist_simulator.byte # Mettez le chemin vers votre simulateur netlist

% : %.py
	$(PYTHON_INTERPRETER) $(CAROTTE_PATH) -o ./build/$@.net ./$@.py
	cp ./build/$@.net ./build/current.net 

sim : ./build/current.net
	$(SIMULATOR) ./build/current.net

