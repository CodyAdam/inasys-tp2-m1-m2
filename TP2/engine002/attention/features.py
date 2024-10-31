import numpy as np

def features(dim: tuple):
    """Generate random values for each word (je, suis, très, malade)"""
    # Generate 4 random vectors of dimension dim
    X1 = np.random.randint(0, 255, dim)  # "je"
    X2 = np.random.randint(0, 255, dim)  # "suis"
    X3 = np.random.randint(0, 255, dim)  # "très"
    X4 = np.random.randint(0, 255, dim)  # "malade"
    
    # Stack vectors vertically to create feature matrix F
    F = np.vstack((X1, X2, X3, X4))
    
    return F