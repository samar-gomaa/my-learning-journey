import pandas as pd
import numpy as np
#load dataset
df=pd.read_csv("Advertising.csv")
#preprocessing
df=df.drop(columns=["Unnamed: 0"])
#features and target
x=df[["TV", "Radio", "Newspaper"]]
y=df["Sales"]
x=x.to_numpy()
y=y.to_numpy()
x=np.c_[np.ones(x.shape[0]),x]
#linear regression with normal equation
theta=np.linalg.inv(x.T @ x)@x.T@y
y_pred=x@theta
print("Model parameters:",theta)
