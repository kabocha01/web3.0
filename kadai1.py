import numpy as np

def function():
    num1 = 0
    num2 = 0
    array = np.zeros((12,12))
    for num1 in range(12):
        for num2 in range(12):
            array[num1][num2] = (num1+1)*(num2+1)
        #print(array[num1])
    print(array)

function()
