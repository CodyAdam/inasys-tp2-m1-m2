import numpy as np

def softmax(vector: np.array):
    """Apply softmax function to input vector with numerical stability
    Args:
        vector: np.array - input vector
    Returns:
        np.array - probability distribution after softmax
    """
    # Subtract max value for numerical stability
    shifted_vector = vector - np.max(vector)
    
    # Compute exponentials of shifted vector
    exp_vector = np.exp(shifted_vector)
    
    # Calculate sum of exponentials
    sum_exp = np.sum(exp_vector)
    
    # Calculate softmax probabilities
    return exp_vector / sum_exp

 

