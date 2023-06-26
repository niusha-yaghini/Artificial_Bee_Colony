import numpy as np

class Bee:
    
    def __init__(self, items):
        self.data = np.zeros(items)
        self.fitness = None

        # self.pos = pos
        # self.intpos = []
        # self.obj= self.evaluate(pos)
        # ##self.obj , self.intpose= self.evaluate(pos)
        # self.prob = 0
        # self.fitness = self.calculate_fitness(self.obj)
        # self.tries = 0

    def _calculating_fitness(self, blocks, items, weights):
        fitness = 0
        for j in range(blocks):
            for i in range(items):
                if(self.data[i]==1):
                    fitness += weights[j][i]
        self.fitness = fitness

    # def Reading_Data(self, pos):
    #     capacity = [320, 320]
    #     penalty = 1500
    #     weights = [[120, 150, 150, 200], [130, 140, 160, 190]]
    #     profits = [20, 16, 17, 10]


    #     sigmoidpos = []
    #     for i in range(len(pos)):  # ndim
    #         sigmoidpos.append(1 / (1 + np.exp(-pos[i])))
    #     self.intpos = [1 if np.random.rand() < sigmoidpos[i] else 0 for i in range(len(sigmoidpos))]

    #     nk = len(capacity)
    #     nI = len(profits)
    #     #k = 1
    #     #item = 0
    #     obj = 0
    #     w = [0,0]
    #     choose = [0 for i in range(len(pos))]
    #     for i in range(len(self.intpos)//nk):
    #         w[0] += self.intpos[i] * weights[i]
    #         w[1] += self.intpos[i] * weights[i]
    #         if (w[0] > capacity[0]) or (w[1] > capacity[1]):
    #             w[0] -= self.intpos[i] * weights[i]
    #             w[1] -= self.intpos[i] * weights[i]
    #             choose[i] = 0
    #             self.intpos[i] = 0
    #         else:
    #             obj += profits[i] * self.intpos[i]
    #             choose[i] = 1
    #         # TODO : maximization (-)  Min (+)
    #     return -obj
    #     ##return -obj, choose

    # def calculate_fitness(self, obj):
    #     # TODO : maximization (-)  Min (+)
    #     fx = obj
    #     if fx >= 0:
    #         fitness = 1 / (1 + fx)
    #     else:
    #         fitness = 1 - fx
    #     return fitness
