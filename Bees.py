import numpy as np

class Bee:
    # each bee is equal to a valid solution, that has the body(data = array answer), and its fitness
    
    def __init__(self, demands, blocks):
                
        self.data = [[0 for i in range(len(blocks))] for j in range(len(demands))]
        self.fitness = None
        self.improvement_try = 0
        self.feasiblity = None

    def _calculating_fitness(self, bee, blocks):
        
        for demand_solution in bee.data:
            for block_choosed in demand_solution:
                if(block_choosed==1):
                    print("1")