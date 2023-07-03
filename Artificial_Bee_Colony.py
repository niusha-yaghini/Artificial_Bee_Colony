import numpy as np
import Bees
import random
import copy

class ABC_algorithm():
# artificial bee colony algorithm 

    def __init__(self, npop, nK, nI, Capacity, Profits, Weights, RW_iteration):
        self.total_population_num = npop
        self.employed_bees_num = int(npop/2)
        self.blocks = nK
        self.items = nI
        self.capacity = Capacity
        self.profits = Profits
        self.weights = Weights
        self.RW_iteration = RW_iteration # the amount of iterations in rolette wheel
          
    def employed_bees(self):
        # making initial random answers (equal to amount of employed bees number)
        # do the improvement-try once on each of them
        # return the made answers
        
        population = []
        for i in range(self.employed_bees_num):
            row = self._solution()
            population.append(row)
            
        # we try for improvement one time for each bee, if change happens we add one to improvement-try property of that bee
        for bee in population():
            change_flag = self.try_for_improvement(population, bee)
            if(change_flag): bee.improvement_try = 0
            else: bee.improvement_try += 0
            
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
                
    def _validality_check(self, bee):
        # checking validality of the answers that has been made (capacity)
        
        for j in range(self.blocks):
            current_capacity = self.capacity[j]
            my_capacity = 0
            for i in range(self.items):
                if (bee.data[i]==1):
                    my_capacity += self.weights[j][i]
            if(my_capacity>current_capacity):
                return False
        return True
                
    def onlooker_bees(self, population):
        # by rolette wheel precedure we do "k" (RW_iteration) times cross_over and mutation,
        # on solution that employed bees have made
        
        for i in range(self.RW_iteration):
            # selecting the bee by rroulette wheel
            bee = self._roulette_wheel(population)

            # we try for improvement one time for each bee, if change happens we add one to improvement-try property of that bee
            change_flag = self.try_for_improvement(population, bee)
            if(change_flag): bee.improvement_try = 0
            else: bee.improvement_try += 0
                
        
    def try_for_improvement(self, population, bee):
        # we do the cross over and mutation here
        # we also return that if the process made any changes or not
        
        # doing the cross over on selected bee and a neighbor (that will be handled in _cross_over)
        change_flag_co = self._cross_over(population, bee)
        
        # doing the mutation on selected bee
        change_flag_m = self._mutation(bee) 
        
        return (change_flag_co or change_flag_m)
    
    def _roulette_wheel(self, population):
        # more fitness = more probbility
        
        total_fitness = 0
        
        # for each bee we calculate the fitness
        for bee in population:
            Bees.Bee._calculating_fitness(bee, self.blocks, self.items, self.weights)
            total_fitness += bee.fitness
        
        # choose a random number for selecting our bee    
        pick = random.uniform(0, total_fitness)
        
        # selecting our bee by the "pick" number and roulette wheel procedure
        current = 0
        for bee in population:
            current += bee.fitness
            if current >= pick:
                return bee         
                
    def _cross_over(self, population, bee):
        # for each answer that employed bees have made, we select a radom neighbor
        # for each answer we also select a random position, and it replaced with its neighbors pos
        # if the changed answer be better than the previous one and it be valid, it will change
        # we also return that if the cross-over has done a change or not

        change_flag = False
        new_bee = copy.deepcopy(bee)
        
        # choosing a random position for change
        random_pos = random.randint(0, self.items-1)
        
        # choosing a neighbor that is not itself
        random_neighbor = random.choice([neighbor for neighbor in population if neighbor!=bee])
        
        # checking that if the two position of bees are different or not (if they were different we do the replacement)
        if(new_bee.data[random_pos] != random_neighbor.data[random_pos]):
            new_bee.data[random_pos] = random_neighbor.data[random_pos]
            
            # check if the new_bee is valid, and had improvements from the bee
            if(self._validality_check(new_bee) and self._improvement_check(bee, new_bee)):
                bee.data = new_bee.data
                change_flag = True
        
        return change_flag
                             
    def _mutation(self, bee):
        # for each answer that employed bees have made, we select a random position and we change it with 0 or 1 (randomly)
        # only if the changed answer be better than the previous one and it be valid, it will change
        # we also return that if the muatation has done a change or not

        change_flag = False
        new_bee = copy.deepcopy(bee)
        
        # choosing a random position
        random_pos = random.randint(0, self.items-1)
        
        # choosing a random new answer for the choosen position (0 or 1)
        replace_target = random.randint(0, 1)
        
        # check that if the current answer of choosen position is different with replace_target or not (if they were different we do the replacement)
        if(new_bee.data[random_pos] != replace_target):
            new_bee.data[random_pos] = replace_target
            
            # check if the new_bee is valid, and had improvements from the bee
            if(self._validality_check(new_bee) and self._improvement_check(bee, new_bee)):
                bee.data = new_bee.data
                change_flag = True
                
        return change_flag

    def _improvement_check(self, current_bee, new_bee):
        # checking that the new bee (changed bee by cross_over or mutation) has imporoved or not
        
        Bees.Bee._calculating_fitness(current_bee, self.blocks, self.items, self.weights)
        Bees.Bee._calculating_fitness(new_bee, self.blocks, self.items, self.weights)
        return True if new_bee.fitness>current_bee.fitness else False
    
    def finding_best_bee(self, population):
        # finding the best solution
        
        best_fitness = 0
        best_bee = None
        for bee in population:
            Bees.Bee._calculating_fitness(bee, self.blocks, self.items, self.weights)
            if(bee.fitness>best_fitness):
                best_fitness = bee.fitness
                best_bee = bee

        return best_bee, best_fitness