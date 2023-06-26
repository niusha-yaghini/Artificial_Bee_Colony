import numpy as np

class Bee:
    # each bee is equal to a valid solution, that has the body(data = array answer), and its fitness
    
    def __init__(self, items):
        self.data = np.zeros(items)
        self.fitness = None

    def _calculating_fitness(self, blocks, items, weights):
        # fitness is amount of capacity that the bee can take (the capacity that the answer is occupying)
        
        fitness = 0
        for j in range(blocks):
            for i in range(items):
                if(self.data[i]==1):
                    fitness += weights[j][i]
        self.fitness = fitness