from config import (max_time, S0, I0, R0, gamma, beta) 
from sir import sir, visualize

import numpy as np

def main():
    # List for save results
    sir_values = [(S0, I0, R0)]

    # Launch the simulation
    sir(S0, I0, R0, 0, sir_values)

    #Generate len(sir_values) time
    time = np.arange(len(sir_values))

    #convert sir_values  into array
    sir_values = np.array(sir_values)

    #Draw the results
    visualize(time, sir_values)



if __name__=="__main__":
    main()