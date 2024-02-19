# Ising Model
Ising model is a mathematical model to used to understant Ferromagnetism an its phase transition to paramagnetic behavior above critical temperature. This model consists 
of a N fixed lattice sites arranged to form a n(n=1,2,3) dimensional array. Each of the lattice sites has a spin $S_i$ associated with it, which can take values +1 or -1.
The entire configuration of spin { $S_i$ } can be used to determine the energy of the system which is given by the hamiltonian:

![Alt text](Images/Screenshot%20from%202024-02-06%2017-21-36-modified.png)

Here $\epsilon_{ij}$ is the interaction energy between nearest neighbour spin and H is the external magnetic field. We can simplify the problem by considering an isotropic interaction with a constant $\epsilon$. The hamiltonian becomes:

![Alt text](Images/Screenshot%20from%202024-02-06%2017-21-57-modified.png)

Given the energy we can find all the thermodynamic variables by finding the partition function given by:

![Alt text](Images/Screenshot%20from%202024-02-06%2017-21-57-modified%20(1).png)

The following thermodynamic quantities are to be found to understand the phase transitions from ferromagnetic to paramagnetic transition:

![Alt text](Images/Screenshot%20from%202024-02-06%2017-21-57-modified%20(3).png)

# Phase Transitions

 The ferromagnetic to paramagnetic phase transition is a second order phase transition. When the temperature T
 approaches the Curie temperature T,the magnetization M(T),which is the order parameter of the transition, continuously goes to zero. Above Tc, the spins point in different directions and their magnetic fields are canceled. This disordered configuration is
caused by the random thermal movement of the spins. The higher the temperature, the more difficult it is for any orderly arrangement of spins to be maintained. 
But there is still interactions with the neighbours unlike a paramagnetic material. But when the temperature is lowered below critical temperature ( $T_c$ )the interactions become stronger then thermal 
fluctuations and the spins align
spontaneously. Instead of canceling each other out, the
individual magnetic fields are added, producing a macroscopic
magnetic field.
