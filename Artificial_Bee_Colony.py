import numpy as np
import Bees
import random
import copy

class ABC_algorithm():
# artificial bee colony algorithm 

    def __init__(self, npop, nK, nI, Capacity, Profits, Weights, RW_iteration):
        self.total_population_num = npop
        self.employed_bees_num = npop/2
        self.blocks = nK
        self.items = nI
        self.capacity = Capacity
        self.profits = Profits
        self.weights = Weights
        self.RW_iteration = RW_iteration # the amount of iterations in rolette wheel
          
    def employed_bees(self):
        # making initial random answers (equal to amount of employed bees number)
        # this function returns the initial population
        
        population = []
        for i in range(self.employed_bees_num):
            row = self._solution()
            population.append(row)
        return population
        
    def _solution(self):
        # making each random solution -> employed bees
        
        capacity_flag = True
        row = Bees.Bee(self.items)
        new_row = copy.deepcopy(row)
        while(capacity_flag):
            x = random.randint(0, self.items-1)
            new_row.data[x] = 1
            capacity_flag = self._validality_check(new_row)
            if(capacity_flag):
                row.data[x] = 1
                
        return row
                
    def _validality_check(self, row):
        # checking validality of the answers that has been made (capacity)
        
        for j in range(self.blocks):
            c = self.capacity[j]
            for i in range(self.items):
                if (row.data[i]==1):
                    c += self.weights[j][i]
            if(c>self.capacity[j]):
                return False
        return True
                
    def onlooker_bees(self, population):
        # by rolette wheel precedure we do k times cross_over and mutation
        # on solution that employed bees have made
        
        for i in range(self.RW_iteration):
            bee = self._roulette_wheel(population)
            self._cross_over(population, bee)
            self._mutation(bee)
        
    def _roulette_wheel(self, population):
        # more fitness = more probbility
        
        total_fitness = 0
        for bee in population:
            Bees.Bee._calculating_fitness(bee, self.blocks, self.items, self.weights)
            total_fitness += bee.fitness
        pick = random.uniform(0, total_fitness)
        current = 0
        for bee in population:
            current += bee.fitness
            if current > pick:
                return bee         
                
    def _cross_over(self, population, bee):
        # for each answer that employed bees have made, we select a radom neighbor
        # for each answer we also select a random position, and it replaced with its neighbors pos
        # if the changed answer be better than the previous one and it be valid, it will change

        new_bee = copy.deepcopy(bee)
        random_pos = random.randint(0, self.items)
        random_neighbor = random.choice([neighbor for neighbor in population if neighbor!=bee])
        new_bee.data[random_pos] = random_neighbor.data[random_pos]
        if(self._validality_check(new_bee) and self._imporovement_check(bee, new_bee)):
            bee.data = new_bee.data
                             
    def _mutation(self, bee):
        # for each answer that employed bees have made, we select a random position and we change it with 0 or 1 (randomly)
        # only if the changed answer be better than the previous one and it be valid, it will change

        new_bee = copy.deepcopy(bee)
        random_pos = random.randint(0, self.items)
        random_replace = random.randint(0, 1)
        new_bee.data[random_pos] = random_replace
        if(self._validality_check(new_bee) and self._imporovement_check(bee, new_bee)):
            bee = new_bee

    def _imporovement_check(self, current_bee, new_bee):
        Bees.Bee._calculating_fitness(current_bee, self.blocks, self.items, self.weights)
        Bees.Bee._calculating_fitness(new_bee, self.blocks, self.items, self.weights)
        return True if new_bee.fitness>current_bee.fitness else False




#     def onlooker_search(self, employedBees):
#         for i in range(int(len(employedBees) / 2)):
#             currentBee = rouletteWheel(employedBees)
#             self.local_update(currentBee, employedBees)
#         return employedBees

#     def scoutBee(self, employedBees):
#         for i in range(len(employedBees)):
#             currentBee = employedBees[i]
#             if currentBee.tries > self.limit:
#                 currentBee = self.global_update()
#         return employedBees

#     def check_bound(self, pos):
#         newPos = pos.copy()
#         for ind in range(len(pos)):
#             newPos[ind] = min(self.upper_bound[ind], newPos[ind])
#             newPos[ind] = max(self.lower_bound[ind], newPos[ind])

#         return newPos


# def rouletteWheel(bees, greaterApproval=True):
#     import numpy as np
#     # in greaterApproval=True greater values has greater chance
#     if greaterApproval:
#         sumVals = sum(bee.fitness for bee in bees)
#         p = {bee: bee.fitness / sumVals for bee in bees}
#     else:
#         sumVals = sum(1 / (bee.fitness + 1e-5) for bee in bees)
#         p = {bee: (1 / (bee.fitness + 1e-5)) / sumVals for bee in bees}

#     sortedIndex = sorted(p, key=p.get, reverse=True)

#     r = np.random.rand()
#     chosenIndex = 0
#     chosen = sortedIndex[chosenIndex]
#     cumP = p[chosen]
#     while cumP < r:
#         chosenIndex += 1
#         chosen = sortedIndex[chosenIndex]
#         cumP += p[chosen]

#     return chosen


# # get bee with best fitness
#     """def BestIter(self,fitness):
#         BestBee = max(self,fitness)"""
