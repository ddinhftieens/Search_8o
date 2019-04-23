import csv
import numpy as np

def readFile(filename):
    with open(filename,"r") as csvfile:
        file = csv.reader(csvfile)
        lines = list(file)
        for i in range(len(lines)):
            lines[i] = [float(x) for x in lines[i][0].split()]
    return np.array(lines)

def normalize(X):
    mins = np.min(X, axis=0)
    maxs = np.max(X, axis=0)
    rng = maxs - mins
    norma_X = 1 - (maxs - X)/rng
    return norma_X
def main():
    X = readFile("dataLogistic.csv")
    normalize(X)

if __name__ == "__main__":
    main()