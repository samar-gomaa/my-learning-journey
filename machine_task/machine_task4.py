import numpy as np
def polynomial_features(x,order):
    x=np.array(x)
    features=[]
    for i in range (order+1):
        features.append(x**i)
    return np.column_stack(features)
x=np.array([1,2,3,4])
y=polynomial_features(x,3)
print(y)