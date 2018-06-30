import numpy as np

def gradient_descent(inp,out):
    length=len(inp)
    theta0=0
    theta1=1
    learning_rate=0.00001
    min_cost=200
    cost=200
    while cost>0.00001:
        predicted=theta1*inp+theta0
        cost=sum((predicted-out)**2)/length
        der1=sum((predicted-out)*inp)/length
        der0=sum(predicted-out)/length
        theta0=theta0-der0*learning_rate
        theta1=theta1-der1*learning_rate
    return (theta0 , theta1)
       
inp=np.array([1,2,3,4,5,6,7,8])
out=np.array([1,4,9,16,25,36,49,64])
theta0,theta1=gradient_descent(inp,out)
print(theta0,theta1)
print(theta0+theta1*10)
    


























    
