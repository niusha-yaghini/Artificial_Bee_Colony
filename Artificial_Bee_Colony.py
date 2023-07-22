import numpy as np
import Bees
import random
import copy
from Structure import *


class ABC_algorithm():
    # artificial bee colony algorithm 
    
    def __init__(self, Demands_amount, Demands, Stations_amount, Stations, Blocks_amount, Blocks, Employed_bees_num, Onlooker_bees_num, Max_improvement_try, Pc, Pm, K_tournomet_percent):
        self.demands_amount = Demands_amount
        self.demands = Demands
        self.stations_amount = Stations_amount
        self.stations = Stations
        self.blocks_amount = Blocks_amount
        self.blocks = Blocks
        self.employed_bees_num = Employed_bees_num
        self.onlooker_bees_num = Onlooker_bees_num
        self.max_improvement_try = Max_improvement_try
        self.crossover_probbility = Pc
        self.mutation_probblity = Pm/self.demands_amount
        # self.k_tournoment = int(k_tournomet_percent*self.items)
          

    def employed_bees(self, population):
        # making initial random answers (equal to amount of employed bees number)
        # do the improvement-try once on each of them
        # return the made answers
        
        if(len(population) == 0):
            for i in range(self.employed_bees_num):
                bee = self._making_bee()
                population.append(bee)
            
        # we try for improvement one time for each bee, if change happens we add one to improvement-try property of that bee
        for bee in population:
            change_flag = self._try_for_improvement(population, bee)
            if(change_flag): 
                bee.improvement_try = 0
                Bees.Bee._calculating_fitness(bee, self.items, self.profits)
            else: 
                bee.improvement_try += 1
                    
    def _making_bee(self):
        # each bee is a (amount of demands * amount of blocks) matrix
        
        bee = Bees.Bee(self.demands, self.blocks)

        data = []
        for demand in self.demands:
            demand_answer = self._make_demand_answer(demand)
            data.append(demand_answer)
            
        bee.data = data
        return bee
                
    def _make_demand_answer(self, demand):
        data = [0 for i in range(self.blocks_amount)]
        destination_flag = False

        # finding the first cell
        choosing_options = []
        for acp_block_indx in demand.acceptable_blocks_index:
            if demand.origin == self.blocks[acp_block_indx].origin:
                choosing_options.append(acp_block_indx)
        choosed_index = random.choice(choosing_options)
        data[choosed_index] = 1
        
        if(demand.destination == self.blocks[choosed_index].destination):
            destination_flag = True
        
        while(destination_flag == False):
            choosing_options = []
            for acp_block_indx in demand.acceptable_blocks_index:
                if self.blocks[choosed_index].destination == self.blocks[acp_block_indx].origin:
                    choosing_options.append(acp_block_indx)
                    
            if(len(choosing_options)==0):
                print("we are in trouble!!!")  
     
            choosed = random.choice(choosing_options)
            data[choosed] = 1
            
            if(demand.destination == self.blocks[choosed].destination):
                destination_flag = True
        
        return data              

                
    def _validality_check(self, bee):
        
        feasiblity_flag = True

        block_limits_check = [0 for i in range(self.stations_amount-1)]
        vagon_limits_check = [0 for i in range(self.stations_amount-1)]

        for demand_solution in bee.data:
            for b in range(self.blocks_amount):
                if(feasiblity_flag):
                    if (demand_solution[b]==1):
                        o = self.blocks[b].origin
                        d = self.blocks[b].destination
                        block_limits_check[o] += 1
                        vagon_limits_check[d] += self.demands[demand_solution].volume
                        if(block_limits_check[o]>self.stations[o].block_capacity):
                            feasiblity_flag = False
                        if(vagon_limits_check[d]>self.stations[d].vagon_capacity):
                            feasiblity_flag = False
                    
        return feasiblity_flag
                                    
    def onlooker_bees(self, population):
        # by rolette wheel precedure we do "onlooker_bees_num" times cross_over and mutation,
        # on solution that employed bees have made
                
        for bee in population:
            if(bee.fitness == None):
                Bees.Bee._calculating_fitness(bee, self.items, self.profits)
        
        sum_of_fitnesses = sum([bee.fitness for bee in population])
        
        for i in range(self.onlooker_bees_num):
            
            # selecting the bee by roulette wheel
            bee = self._roulette_wheel(population, sum_of_fitnesses)
            
            # # sele a bee by tournoment procedure
            # bee = self._tournoment(population)
            
            # we try for improvement one time for each bee, if change happens we add one to improvement-try property of that bee
            change_flag = self._try_for_improvement(population, bee)
            if(change_flag): 
                bee.improvement_try = 0
                Bees.Bee._calculating_fitness(bee, self.items, self.profits)
            else: 
                bee.improvement_try += 1
                                                        
    def scout_bees(self, population):
        delete_bees = []
        new_bees = []
        for bee in population:
            if(bee.improvement_try>=self.max_improvement_try):
                delete_bees.append(bee)
                new_bees.append(self._making_bee())
        for i in range(len(delete_bees)):
            population.remove(delete_bees[i])
            population.append(new_bees[i])
                    
    def _try_for_improvement(self, population, bee):
        # we do the cross over and mutation here
        # we also return that if the process made any changes or not
        
        change_flag = False
        new_bee = copy.deepcopy(bee)
        
        # doing the cross over on selected bee and a neighbor (that will be handled in _cross_over)
        self._cross_over_one_point(population, new_bee)
        
        # doing the mutation on selected bee
        self._mutation(new_bee) 
        
        # feasible = true, infeasible = false
        validality_flag = self._validality_check(new_bee)
        
        # having improvement = true, do not have any improvement = false
        improvement_flag = self._improvement_check(bee, new_bee)
        
        if((validality_flag == False) or (validality_flag and improvement_flag)):
            bee.data = new_bee.data
            change_flag = True

        return change_flag        
    
    def _tournoment(self, population):
        tournoment_list = []
        for i in range(self.k_tournoment):
            tournoment_list.append(random.choice(population))
            
        maxF = 0
        max_B = None
        for bee in population:
            if(bee.fitness>maxF):
                maxF = bee.fitness
                max_B = bee
        return max_B
    
    def _roulette_wheel(self, population, sum_of_fitnesses):
        
        # choose a random number for selecting our bee    
        pick = random.uniform(0, sum_of_fitnesses)
        
        # selecting our bee by the "pick" number and roulette wheel procedure
        current = 0
        for bee in population:
            current += bee.fitness
            if current >= pick:
                return bee         
                
    def _cross_over_one_point(self, population, bee):
        # for each answer that employed bees have made, we select a radom neighbor
        # for each answer we also select a random position, and it replaced with its neighbors pos
        # if the changed answer be better than the previous one and it be valid, it will change
        # we also return that if the cross-over has done a change or not
        
        x = random.random()

        if(x<=self.crossover_probbility):
            term_pos = random.randint(1, self.demands_amount-1)
            neighbor_bee = random.choice(population)
            self.replace_terms(bee, neighbor_bee, term_pos)
        
    def replace_terms(self, bee, neighbor_bee, random_pos):
        # in here we change parts of our choromosome base on choosed term
        
        data = []
        for i in range(0, random_pos):
            data.append(bee.data[i])
        for j in range(random_pos, self.demands_amount):
            data.append(neighbor_bee.data[j])
        
        bee.data = data
                                                            
    def _mutation(self, bee):
        # for each answer that employed bees have made, we select a random position and we change it with 0 or 1 (randomly)
        # only if the changed answer be better than the previous one and it be valid, it will change
        # we also return that if the muatation has done a change or not
        
        for i in range(self.demands_amount):            
            x = random.random()
            if(x<=self.mutation_probblity):
                bee.data[i] = self._make_demand_answer(self.demands[i])
                
    def _improvement_check(self, current_bee, new_bee):
        # checking that the new bee (changed bee by cross_over or mutation) has imporoved or not
        
        Bees.Bee._calculating_fitness(current_bee, self.blocks)
        Bees.Bee._calculating_fitness(new_bee, self.items, self.profits)
        return True if new_bee.fitness>current_bee.fitness else False
    
    def finding_best_bee(self, population):
        # finding the best solution
        
        best_fitness = 0
        best_bee = None
        for bee in population:
            Bees.Bee._calculating_fitness(bee, self.items, self.profits)
            if(bee.fitness>best_fitness):
                best_fitness = bee.fitness
                best_bee = bee

        return best_bee, best_fitness