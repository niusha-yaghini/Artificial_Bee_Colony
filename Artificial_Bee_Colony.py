import numpy as np
from Bee_Colony import Bee
import random
import copy

class ABC_algorithm():
# artificial bee colony algorithm 

    def __init__(self, npop, nK, nI, Capacity, Profits, Weights):
        self.total_population_num = npop
        self.employed_bees_num = npop/2
        self.blocks = nK
        self.items = nI
        self.capacity = Capacity
        self.profits = Profits
        self.weights = Weights
          
    def _employed_bees(self):
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
        row = np.zeros(self.items)
        while(capacity_flag):
            x = random.randint(0, self.items-1)
            self._validality_check(capacity_flag, row, x)
            if(capacity_flag):
                row[x] = 1
                
        return row
                
    def _validality_check(self, capacity_flag, row, x):
        # checking validality of the answers that has been made (capacity)
        
        for j in range(self.blocks):
            c = self.capacity[j]
            for i in range(self.items):
                if (row[i]==1 or i == x):
                    c += self.weights[j][i]
            if(c>self.capacity[j]):
                capacity_flag = False
                return
                
    def employed_improvement(self, population):
        # doing the cross_over and mutation for each answer that employed bees have made
        
        self.cross_over(population)
        self.mutation(population)
        
    def cross_over(self, population):
        # for each answer that employed bees have made, we select a radom neighbor
        # for each answer we also select a random position, and it replaced with its neighbors pos

        for p in population:
            new_p = copy.deepcopy(p)
            random_pos = random.randint(0, self.items)
            random_neighbor = random.choice([neighbor for neighbor in population if neighbor!=p])
            new_p[random_pos] = random_neighbor[random_pos]
            if()
             
    def mutation(self, population):
        # for each answer that employed bees have made, we select a random position and we change it with 0 or 1 (randomly)

        for p in population:
            random_pos = random.randint(0, self.items)
            random_replace = random.randint(0, 1)
            p[random_pos] = random_replace

    def imporovement_check(old_solution, new_solution):
        


    # def employee_search(self, employedBees):
    #     for i in range(len(employedBees)):
    #         currentBee = employedBees[i]
    #         self.local_update(currentBee, employedBees)
    #     return employedBees

    # def local_update(self, currentBee, employedBees):
    #     import numpy as np
    #     from Bee_Colony import Bee
    #     neighbor = np.random.choice(employedBees)
    #     randomPos = np.random.randint(0, self.ndim)
    #     newPosCurrent = currentBee.pos[randomPos] + np.random.uniform(
    #         -self.search_radius, self.search_radius) * (currentBee.pos[randomPos] - neighbor.pos[randomPos])

    #     newPos = currentBee.pos.copy()
    #     newPos[randomPos] = newPosCurrent
    #     newPos = self.check_bound(newPos)
    #     oldFitness = currentBee.fitness
    #     newBee = Bee(newPos)
    #     newFitness = newBee.fitness
    #     newObj = newBee.obj

    #     if oldFitness is None or newFitness > oldFitness:
    #         currentBee.pos = newPos.copy()
    #         currentBee.fitness = newFitness
    #         currentBee.obj = newObj
    #         currentBee.intpos=newBee.intpos.copy()
    #         currentBee.tries = 0
    #     else:
    #         currentBee.tries += 1

    def onlooker_search(self, employedBees):
        for i in range(int(len(employedBees) / 2)):
            currentBee = rouletteWheel(employedBees)
            self.local_update(currentBee, employedBees)
        return employedBees

    def scoutBee(self, employedBees):
        for i in range(len(employedBees)):
            currentBee = employedBees[i]
            if currentBee.tries > self.limit:
                currentBee = self.global_update()
        return employedBees

    def check_bound(self, pos):
        newPos = pos.copy()
        for ind in range(len(pos)):
            newPos[ind] = min(self.upper_bound[ind], newPos[ind])
            newPos[ind] = max(self.lower_bound[ind], newPos[ind])

        return newPos


def rouletteWheel(bees, greaterApproval=True):
    import numpy as np
    # in greaterApproval=True greater values has greater chance
    if greaterApproval:
        sumVals = sum(bee.fitness for bee in bees)
        p = {bee: bee.fitness / sumVals for bee in bees}
    else:
        sumVals = sum(1 / (bee.fitness + 1e-5) for bee in bees)
        p = {bee: (1 / (bee.fitness + 1e-5)) / sumVals for bee in bees}

    sortedIndex = sorted(p, key=p.get, reverse=True)

    r = np.random.rand()
    chosenIndex = 0
    chosen = sortedIndex[chosenIndex]
    cumP = p[chosen]
    while cumP < r:
        chosenIndex += 1
        chosen = sortedIndex[chosenIndex]
        cumP += p[chosen]

    return chosen


# get bee with best fitness
    """def BestIter(self,fitness):
        BestBee = max(self,fitness)"""
