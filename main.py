import modify_dataset as mod
import numpy as np
import pandas as pd

def first():
    datafile = pd.read_csv(r'20140711.CSV')
    sievedData = datafile[datafile['NumberOfBoardings'] > 20]
    print("Filtered Data: ")
    print(sievedData)
    # distribution2D = []
    for i,row in sievedData.iterrows():
        elements = 7
        alpha = 10
        number = row['NumberOfBoardings']
        distribution, remaining = mod.calculateDistribution(number, alpha, elements)
        print(number, distribution, remaining)
        # distribution2D.append(distribution)

    # print(distribution2D)

if __name__ == "__main__":
    first()