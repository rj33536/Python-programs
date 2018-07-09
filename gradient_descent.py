import numpy as np
from numpy import matmul,transpose
def gradientdescent_vectorized(inp,out,alpha,iterations):
    length=np.shape(inp)
    theta=np.zeros(length[1])
    for i in range(iterations):
        predicted=matmul(inp,transpose(theta))
        theta=theta-alpha*(matmul(transpose(predicted-out),inp)/length[1])
    return theta

def predict(X,theta):
    return sum(X*theta)
inp=np.array([[1,2],[1,3],[1,5],[1,6]])
out=np.array([500,550,600,650])
    
theta=gradientdescent_vectorized(inp,out,0.001,100000)
print(predict([1,8],theta))

























    
