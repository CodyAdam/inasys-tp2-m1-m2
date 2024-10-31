from attention import features
from attention import requêtes
from attention import clés
from attention import valeurs
from attention import similarité
from attention import norm
from utils import softmax
from attention import A

def main():
    #Features matrix
    F = features(dim=(1,6))

    #Query matrix
    Q = requêtes(dim_wq=(3,6), F=F)

    #Keys matrix
    K = clés(dim_wk=(3,6), F=F)

    #V matrix
    V = valeurs(dim_wv=(4,6), F=F)

    #dot product matrix
    sim = similarité(K,Q)

    #Scaled dot product matrix

    sim_norm = norm(d_k = 3, similarité=sim)

    # Attention vector of x_1
    a_x1 = sim_norm[:,0]

    # Attention vector of x_2
    a_x2 = sim_norm[:,1]

    # Attention vector of x_3
    a_x3 = sim_norm[:,2]

    # Attention vector of x_4
    a_x4 = sim_norm[:,3]

    # softmax apply on x_1
    as_x1 = softmax(a_x1)

    # softmax apply on x_2
    as_x2 = softmax(a_x2)

    # softmax apply on x_3
    as_x3 = softmax(a_x3)

    # softmax apply on x_4
    as_x4 = softmax(a_x4)

    Attention = A(as_x1, as_x2 , as_x3, as_x4)

  

if __name__=="__main__":
    main()