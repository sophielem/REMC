# REMC: Replica exchange Monte Carlo algorithm

The *ab initio* protein folding problem consists of predicting protein tertiary structure from a given amino acid sequence by minimizing an energy function. 


Here is implemented the Replica Exchange Monte Carlo(REMC) method using a lattice for the protein, the hydrophobic polar model  and another dimension, temperature. This algorithm maintains several replicates of the conformation in different temperature. A random walk is realized by a transition of neighbouring temperature. This project allow to solve HP protein folding problem in 2D.

## Install and execute
To install it, first install all the requiered module with correct version with this command:
```
pip install -r requirements.txt
```

Then, it's possible to run the programm with these commands:
```
./main.py -s <seq> -e <x> -m <move>
./main.py -s <seq> -e <x> -m <move> [-p <nb_steps>] [-t <temp>] [-r <nb_rep>]
```
You enter the sequence in HP model, the minimal energy to reach and the move to do:
- VSHD
- PULLMOVES
- MIXE

With the first, the number of steps is 500, the minimal temperature is 160 and the number of replica is 5, otherwise it's possible to configure them with the second command.

## Running the test
For this example, the number of steps, the minimal temperature and the number of replica are set to default and the sequence given is the first sequence of the standard benchmark.
```
./main.py -s hphpphhphpphphhpphph -e 9 -m MIXE
```
Then, the best energy is displayed in the terminal, with the exectuion time. For each replica, a figure is created with matplotlib 3D, saved in the directory *results* and displayed to the screen. 
![exemple_result](https://github.com/sophielem/REMC/blob/remc_dev/results/conformation0.png "Example result")

## Authors

Sophie LEMATRE
