import numpy as np
import os
import struct
from array import array as pyarray
from sklearn.model_selection import train_test_split
from load_data_subset import make_vector

def load_mnist(dataset="training", digits=np.arange(10), path="data_set", size = 60000):
    if dataset == "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif dataset == "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    
    else:
        raise ValueError("dataset must be 'testing' or 'training'")

    flbl = open(fname_lbl, 'rb')
    magic_nr, size = struct.unpack(">II", flbl.read(8))
    lbl = pyarray("b", flbl.read())
    flbl.close()

    fimg = open(fname_img, 'rb')
    magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
    img = pyarray("B", fimg.read())
    fimg.close()

    X = [0 for i in range(size)]

    step_value = rows * cols

    for i in range(size):
        X[i] = np.array(img[i * step_value : (i + 1) * step_value]).reshape(rows * cols, 1)

    X = np.divide(np.array(X), 255.0)

    if dataset == "training":
        Y = np.array([make_vector(j) for j in lbl])
    else:
        Y = [j for j in lbl]

    return X, Y

