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
        row = Bees.Bee
        # row = np.zeros(self.items)
        new_row = copy.deepcopy(row)
        while(capacity_flag):
            x = random.randint(0, self.items-1)
            new_row. [x] = 1
            capacity_flag = self._validality_check(new_row)
            if(capacity_flag):
                row[x] = 1
                
        return row
                
    def _validality_check(self, row):
        # checking validality of the answers that has been made (capacity)
        
        for j in range(self.blocks):
            c = self.capacity[j]
            for i in range(self.items):
                if (row[i]==1):
                    c += self.weights[j][i]
            if(c>self.capacity[j]):
                return False
        return True
                
    def onlooker_bees(self, population):
        # by rolette wheel precedure we do k times cross_over and mutation
        # on solution that employed bees have made
        p = self._roulette_wheel(population, self.RW_iteration)
        self._cross_over(population, p)
        self._mutation(p)
        
    def _roulette_wheel(population, iteration):
        for i in range(iteration):
            print(1)
            
    
    def _cross_over(self, population, p):
        # for each answer that employed bees have made, we select a radom neighbor
        # for each answer we also select a random position, and it replaced with its neighbors pos
        # if the changed answer be better than the previous one and it be valid, it will change

        new_p = copy.deepcopy(p)
        random_pos = random.randint(0, self.items)
        random_neighbor = random.choice([neighbor for neighbor in population if neighbor!=p])
        new_p[random_pos] = random_neighbor[random_pos]
        if(self._validality_check(new_p) and self._imporovement_check(p, new_p)):
            p = new_p
                             
    def _mutation(self, p):
        # for each answer that employed bees have made, we select a random position and we change it with 0 or 1 (randomly)
        # only if the changed answer be better than the previous one and it be valid, it will change

        new_p = copy.deepcopy(p)
        random_pos = random.randint(0, self.items)
        random_replace = random.randint(0, 1)
        new_p[random_pos] = random_replace
        if(self._validality_check(new_p) and self._imporovement_check(p, new_p)):
            p = new_p

    def _imporovement_check(self, old_solution, new_solution):
        old_fitness = 0
        new_fitness = 0
        for j in range(self.blocks):
            for i in range(self.items):
                if(old_solution[i]==1):
                    old_fitness += self.weights[j][i]
                if(new_solution[i]==1):
                    new_fitness += self.weights[j][i]
        return True if new_fitness>old_fitness else False


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
