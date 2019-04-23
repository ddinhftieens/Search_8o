import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    n = np.size(x)
    Xtb = np.mean(x)
    Ytb = np.mean(y)
    B1 = (np.sum(x*y)-n*Xtb*Ytb)/(np.sum(x*x)-n*Xtb*Xtb)
    B0 = Ytb - B1*Xtb
    return (B0,B1)

def plot_regression(x,y,b):
    plt.scatter(x,y,c="g",label='Point=0')
    y_ = b[0] + b[1]*x
    plt.plot(x,y_,c="r",label='Line=1')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("LinearRegression")
    plt.show()

def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    b = estimate_coef(x,y)
    print("Ket qua la:\nB0 = {} \nB1 = {}".format(b[0],b[1]))
    plot_regression(x,y,b)
if __name__ == "__main__":
    main()


