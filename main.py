import numpy as np
class me:
    def __init__(self):
        self.post_init()

    def sigmoid(self, x):
        return 1/ (1 + np.exp(-x))

    def post_init(self):
        self.var1 = self.sigmoid(1)
        self.var2 = self.sigmoid(2)
        self.var3 = self.sigmoid(3)
        self.var4 = self.sigmoid(4)
        self.var5 = self.sigmoid(5)