import numpy as np
from utils import Layer
class me:
    def __init__(self):
        self.x = [1,2,3,4,5]
        self.y = self.tanh([a for a in self.x])
        self.layer = Layer

    def tanh(self, x):
        return (np.exp(x)-np.exp(-x))/ (np.exp(x)+np.exp(-x))


