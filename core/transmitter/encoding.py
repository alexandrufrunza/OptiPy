import numpy as np

from ..utils.controller import Chain

class BitsGen(Chain):
    def __init__(self, num_bits, name="Generator"):
        if num_bits == 0:
            raise ValueError("Your binary array cannot have a 0 length")
        elif num_bits & (num_bits-1) != 0:
            raise ValueError("You have to insert a value representing a power of 2")
        self.num_bits = num_bits
        self.name = name

    def process(self):
        # Generate random integers (0 or 1) for the specified number of bits
        self.data = np.random.randint(2, size=self.num_bits, dtype=int)
        return self.data

# Example: generate 10 random bits
genBin = BitsGen(2**8)
print(genBin.process()) 
