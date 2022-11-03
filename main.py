import numpy as np
class me:
    def __init__(self):
        self.x = [1,2,3,4,5]
        self.y = self.sigmoid([a for a in self.x])


    def sigmoid(self, x):
        return 1/ (1 + np.exp(-x))

