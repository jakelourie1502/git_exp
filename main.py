import numpy as np
from utils import Layer, MONTHS
class me:
    def __init__(self):
        self.x = [1,2,3,4,5]
        self.y = self.tanh([a for a in self.x])
        self.layer = Layer
        self.layer2 = MONTHS

    def tanh(self, x):
        return (np.exp(x*2)-np.exp(-x))/ (np.exp(x)+np.exp(-x))


