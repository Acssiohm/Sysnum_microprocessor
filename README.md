# Sysnum_microprocessor
The netlist encoding of a microprocessor made in group for a digital systems course  

Adressage mémoire sur 32 bits  
Base ISA : RISC-V 32 bits  
Granularité mémoire : 1 octet   
32 registres de 32 bits  
le code et la mémoire du processus partagent des espaces d'adressage séparés (architecture de Harvard)

Extensions possibles :
- Multiplicateur
- Pipelining
- Bit shift
N.B. Write tests with gobbolt.org

# Compilation & Simulation
Une fois les bons chemins relatifs mis à jour (cf. plus bas) vous pouvez:
- compiler un circuit circuit.py avec :
`make circuit`
- lancer la simulation du dernier ciruit compilé avec :
`make sim`
- et donc si vous voulez compiler puis simuler circuit.py :
`make circuit sim`

Pour que cela fonctionne, il faut évidemment qu'il connaisse les chemins vers votre carotte.py et votre simulateur. 
Par défaut, les chemins sont correct pour le cas où vous n'avez pas modifié le dossier du simulateur et que vous y avez placé ce projet de sorte à avoir ces dossiers dans un même répertoire :
- carotte.py
- Sysnum_microprocessor
- tp1
Si ce n'est pas le cas, vous pouvez regarder les 3 premières lignes du fichier Makefile et les mettre à jour. 
