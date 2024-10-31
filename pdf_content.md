The document titled **"TP N°2: Introduction à la programmation en langage Python"** is a technical tutorial aimed at guiding students through various exercises related to Python programming, focusing on topics such as numerical computation, data visualization, and object-oriented programming. Below is a detailed extraction of the text content, along with ultra-detailed descriptions of the images to ensure full comprehension.

---

## **Préliminaire:**

The files you will modify are available on GitHub.

1. To retrieve them, you need to install Git (https://git-scm.com/downloads).
2. Depending on your system, proceed with the installation of the distribution.
3. Then, in the terminal, run: `git clone https://github.com/EDJINEDJA/TP2.git`.
4. For engine004, I assume you are ready to explore the world of engineering. Organize your code and solve the problem.

---

## **Exercice 1: Engine001 - Module Numpy et Matplotlib (animation)**

In this exercise, we will use the animation submodule of Matplotlib.

The function to animate is:

$$
f(x, t) = e^{-(x - 3t)^2} \sin(4\pi(x - t))
$$

This function models a patient's heart rate over time $$t$$.

1. Write a Python program that visualizes and animates $$f(x,t)$$ in the interval $$x \in [0,10]$$ for $$t \in [0,3]$$.
2. Save the output as a `.gif` file using the `animation.save` instruction.

---

## **Exercice 2: Engine002 - Numpy (self-attention)**

The "self-attention" mechanism is used by large language models to generate coherent text.

### **1. Word Embedding**

Word embedding is a technique used in natural language processing to represent words from a text as numerical vectors. This allows computers to perform algebraic operations on these vectors to deduce meanings or relationships.

We will embed the sentence P1: *"je suis très malade"*.

1. Use the Numpy module (`randint`) to generate 4 vectors ($$X_1$$, $$X_2$$, $$X_3$$, $$X_4$$), each of dimension (1,6), corresponding to the words "je", "suis", "très", and "malade".
2. Concatenate these vectors using `np.vstack` to form the feature matrix $$F$$.

#### **Image Description:**
- **Figure 1** shows a diagram of self-attention mechanisms where input words are transformed into vectors and processed through multiple steps.
  
- **Figure 2** shows a table with four columns representing feature vectors for each word:
  
  | x₁ | x₂ | x₃ | x₄ |
  |----|----|----|----|
  | 2  | 0  | 0  | 2  |
  | 0  | 1  | 0  | 0  |
  | 0  | 2  | 1  | 0  |
  | 0  | 0  | 1  | 1  |
  
### **2. Creation of Query Matrix (Q)**

To calculate the query matrix $$(q_1, q_2, q_3, q_4)$$ associated with $$(X_1, X_2, X_3, X_4)$$, perform a dot product between a randomly generated matrix $$W_Q$$ (with `numpy.random.rand`) of dimension (3,6) and the feature matrix $$F$$ of dimension (6,4).

#### **Image Description:**
- **Figure 3** illustrates how queries are formed from feature vectors by multiplying them with weights.

### **3. Creation of Key Matrix (K)**

To calculate the key matrix $$(k_1, k_2, k_3, k_4)$$, perform a dot product between a randomly generated matrix $$W_K$$ (with `numpy.random.rand`) of dimension (3,6) and the feature matrix $$F$$.

#### **Image Description:**
- **Figure 4** shows how keys are created similarly to queries by multiplying feature vectors with another set of weights.

### **4. Creation of Value Matrix (V)**

To calculate the value matrix $$(v_1, v_2, v_3, v_4)$$, perform a dot product between a randomly generated matrix $$W_V$$ (with `numpy.random.rand`) of dimension (4,6) and the feature matrix $$F$$.

### **5. Cosine Similarity Calculation**

To calculate cosine similarity for each key-query pair, perform a dot product between matrices $$K$$ and $$Q$$.

#### **Image Description:**
- **Figure 5** shows cosine similarity being computed between keys and queries.

### **6. Normalization**

When calculating dot products between each pair of vectors $$k$$ and $$q$$, variance may leak depending on the dimension of $$k$$. To avoid this issue, normalize the resulting matrix from multiplying $$K$$ and $$Q$$ by dividing each value by $$\sqrt{d_k}$$, where $$d_k =3$$.

### **7. Definition of Softmax Function**

The softmax function transforms a vector of real numbers into a probability distribution:

$$
\sigma(\mathbf{z})_{i} = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$

Define a softmax function that takes as input a vector of K numbers and returns a probability distribution over these K choices.

#### **Image Description:**
- **Figure 6** illustrates how normalization is applied before softmax.

### **8. Calculation of Weighted Attention Matrix (A)**

For each vector $$K^T \cdot q_j$$, apply your softmax function. Use `np.vstack` to construct matrix $$A$$.

#### **Image Description:**
- **Figure 7** shows how attention weights are calculated after applying softmax on key-query products.

---

## **Exercice 3: Engine003 - Virus Propagation in Population (SIR Model)**

The SIR model is used to simulate disease propagation in a population by dividing it into three compartments:
- S (Susceptible): People who can contract the disease.
- I (Infected): People who have contracted the disease and can transmit it.
- R (Recovered): People who have recovered and are immune.

The variations in populations S, I, and R over time are modeled using this system of equations:

$$
\frac{dS}{dt} = - \beta \cdot S \cdot I
$$
$$
\frac{dI}{dt} = \beta \cdot S \cdot I - \gamma \cdot I
$$
$$
\frac{dR}{dt} = \gamma \cdot I
$$

Parameters:
- Transmission rate ($$\beta$$): e.g., $$0.3$$
- Recovery rate ($$\gamma$$): e.g., $$0.1$$
- Initial proportions ($$S_0 =0.99,\ I_0 =0.01,\ R_0 =0.0)$$
- Maximum simulation time: e.g., `109`

Tasks:
1. Create a recursive function that updates values for S, I, and R at each call using these equations until either maximum time or zero infected population is reached.
2. Use Matplotlib to plot how populations S, I, and R evolve over time.

---

## **Exercice 4: Engine004 - Object-Oriented Programming (OOP)**

You have been recruited as an AI engineer to automate hospital processes using robots during health crises.

### **1. Collaborative Robots**

All robots are collaborative robots (**RobotC**) with these characteristics:
- Private attribute `Id` (integer).
- Public attribute `category` (string).
- Public attribute `orientation` (integer representing directions like NORD=1 or EST=2).
- Public boolean attribute `status` indicating if it's operational.
- Attribute `position` defined by class Point with coordinates x,y,z in space.

The Point class has methods:
- `set_xyz(self,x,y,z)` initializes robot's coordinates.
- `deplace(self,\ dx,\ dy,\ dz,\theta)` moves robot in space with rotation around Z-axis followed by translation.

All RobotC robots share methods like constructors (`Constructor(Id:int,Catégorie:str)`), status checks (`getStatus()`), orientation management (`setOrientation()`), etc.

Tasks:
- Instantiate RobotC class with an array of four robots.
  
### **2. Mobile Collaborative Robots**

Mobile collaborative robots (**RobotCMobile**) have additional methods like:
- `avancer()` moves robot based on its orientation:
    - East increases x-coordinate,
    - West decreases x-coordinate,
    - North increases y-coordinate,
    - South decreases y-coordinate.

### **3. Surveillance Robots**

Surveillance robots exchange information about their orientation using method `sendOrientation()`.

### **4. Reception Robots**

Reception robots greet visitors (`accueillir(visiteur:str)`), guide them (`indiqueChemin(destination:str)`), or schedule appointments (`prendreRendezVous(details:str)`).

### **5. Surgical Assistance Robots**

Surgical assistance robots help teams by preparing instruments (`preparerInstrument(instrument:str)`), following operations (`suivreOperation()`), or assisting surgeons (`assisterChirurgien()`).

### **6. Cleaning Robots**

Cleaning robots maintain hospital cleanliness with methods like:
- `nettoyerZone(zone:str)`
- `decontaminer()`
