Let's implement Exercise 2 (Engine002) step by step. Let's implement each function according to the requirements.

1. First, let's implement the features function to generate word embeddings:

```python:TP2/engine002/attention/features.py
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
```

2. Let's implement the query matrix function:

```python:TP2/engine002/attention/requêtes.py
import numpy as np

def requêtes(dim_wq: tuple, F: np.array):
    """Calculate query matrix Q = W_q @ F^T"""
    # Generate random weight matrix W_q
    W_q = np.random.rand(*dim_wq)
    
    # Calculate Q = W_q @ F^T
    Q = W_q @ F.T
    
    return Q
```

3. Implement the key matrix function:

```python:TP2/engine002/attention/clés.py
import numpy as np

def clés(dim_wk: tuple, F: np.array):
    """Calculate key matrix K = W_k @ F^T"""
    # Generate random weight matrix W_k
    W_k = np.random.rand(*dim_wk)
    
    # Calculate K = W_k @ F^T
    K = W_k @ F.T
    
    return K
```

4. Implement the value matrix function:

```python:TP2/engine002/attention/valeurs.py
import numpy as np

def valeurs(dim_wv: tuple, F: np.array):
    """Calculate value matrix V = W_v @ F^T"""
    # Generate random weight matrix W_v
    W_v = np.random.rand(*dim_wv)
    
    # Calculate V = W_v @ F^T
    V = W_v @ F.T
    
    return V
```

5. Implement the similarity calculation:

```python:TP2/engine002/attention/similarité.py
import numpy as np

def similarité(K: np.array, Q: np.array):
    """Calculate similarity matrix K^T @ Q"""
    # Calculate dot product K^T @ Q
    return K.T @ Q
```

6. Implement the normalization function:

```python:TP2/engine002/attention/norm.py
import numpy as np

def norm(d_k: int, similarité: np.array):
    """Normalize similarity matrix by sqrt(d_k)"""
    return similarité / np.sqrt(d_k)
```

7. Implement the softmax function:

```python:TP2/engine002/utils/utils.py
import numpy as np

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
```

8. Finally, implement the attention weight matrix:

```python:TP2/engine002/attention/attention_weight_matrix.py
import numpy as np

def A(a_x1: np.array, a_x2: np.array, a_x3: np.array, a_x4: np.array):
    """Create attention weight matrix by stacking attention vectors"""
    # Stack attention vectors vertically
    return np.vstack((a_x1, a_x2, a_x3, a_x4))
```

The main file is already correctly structured (lines 1-59 in main.py).

We run the simulation with:
```bash
cd TP2/engine002
python main.py
```

### Explanation of the Implementation:

1. **Word Embedding (Features)**:
   - Creates 4 random vectors for each word
   - Uses np.vstack to combine them into matrix F
   - Dimension: (4,6) matrix

2. **Query Matrix (Q)**:
   - Creates random weight matrix W_q (3,6)
   - Multiplies W_q with F^T to get Q
   - Dimension: (3,4) matrix

3. **Key Matrix (K)**:
   - Similar to Q, but with different weights W_k
   - Dimension: (3,4) matrix

4. **Value Matrix (V)**:
   - Uses W_v of dimension (4,6)
   - Dimension: (4,4) matrix

5. **Similarity Calculation**:
   - Computes K^T @ Q for attention scores
   - Dimension: (4,4) matrix

6. **Normalization**:
   - Scales by 1/√(d_k) to prevent gradient issues
   - d_k = 3 (dimension of key vectors)

7. **Softmax**:
   - Converts scores to probability distribution
   - Uses exponential normalization

8. **Attention Matrix**:
   - Combines all softmax outputs
   - Final attention weight matrix

This implementation creates a complete self-attention mechanism for the given sentence "je suis très malade", following the transformer architecture principles.