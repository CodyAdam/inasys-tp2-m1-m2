import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Union
from config import max_time, beta, gamma
import os

def sir(S: float, I: float, R: float, time: int, sir_values: List[Tuple[float, float, float]]) -> None:
    """
    Recursive implementation of SIR model
    Args:
        S: proportion of susceptible population
        I: proportion of infected population
        R: proportion of recovered population
        time: current simulation time
        sir_values: list to store simulation values
    """
    # Base case: if max time reached or no more infected
    if time >= max_time or I <= 0:
        return
    
    # Calculate changes using SIR equations
    dS = -beta * S * I
    dI = beta * S * I - gamma * I
    dR = gamma * I
    
    # Update values
    new_S = S + dS
    new_I = I + dI
    new_R = R + dR
    
    # Store new values
    sir_values.append((new_S, new_I, new_R))
    
    # Recursive call with updated values
    sir(new_S, new_I, new_R, time + 1, sir_values)

def visualize(time: np.array, sir_values: np.array) -> None:
    """
    Visualize SIR model evolution
    Args:
        time: array of time points
        sir_values: array of (S,I,R) values at each time point
    """
    plt.figure(figsize=(10, 6))
    
    # Plot each population
    plt.plot(time, sir_values[:, 0], 'b-', label='Susceptible')
    plt.plot(time, sir_values[:, 1], 'r-', label='Infected')
    plt.plot(time, sir_values[:, 2], 'g-', label='Recovered')
    
    # Add labels and title
    plt.xlabel('Time')
    plt.ylabel('Population Proportion')
    plt.title('SIR Model Evolution')
    plt.legend()
    plt.grid(True)
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Save the plot
    plt.savefig('data/sir_model.png')
    plt.show()