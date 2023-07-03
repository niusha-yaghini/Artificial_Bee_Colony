import Artificial_Bee_Colony
import numpy as np
import Reading_Data
import time
import copy
import Diagram


def Bee_Colony_Algorithm():
    # ABC = ABC.ABC_algorithm(npop, nK, nI, Capacity, Weights, ndim, limit, lower_bound, upper_bound, ncycle, search_radius=1)
    ABC = Artificial_Bee_Colony.ABC_algorithm(population_num, nK, nI, Capacity, Profits, Weights, k, max_improvement_try)
    population = ABC.employed_bees()
    ABC.onlooker_bees(population)
    best_bee_of_iteration, best_fitness_of_iteration = ABC.finding_best_bee(population)
    
    return best_bee_of_iteration, best_fitness_of_iteration


if __name__ == '__main__':
    
    population_num = 5000  # number of total bees => npop/2 = amount of first population
                         # this must be an even number 
    k = 200   # number of iterations in roulette wheel, that select a bee and pass it to improvement-try
    max_improvement_try = 30
    iteration_of_ABC = 40   # number of total iteration of algorithm
    
    # file name of the datas
    data_file_name = ".\\mknap1-Question\\06.txt"
    
    # file name for save results
    result_file_name = ".\\mknap1-Answer(try4)\\06.txt"
    photo_name = "06"

    # nK = number of knapstacks
    # nI = number of items
    nK, nI, Capacity, Profits, Weights = Reading_Data.Reading(data_file_name)
    
    # getting result by bees :)
    st = time.time() # get the start time of all
    
    result = open(f'{result_file_name}', 'a')
    result.write(f"Artificial Bee Colony Algorithm \n \n")        
    result.close()

    # 1) writing the results in a text
    # 2) getting the time of algorithm in each iteration
    
    best_bees_each_iter = []
    best_fitnesses_each_iter = []
    best_fitnesses_so_far = []
    fitness_sum = 0
    
    for i in range(iteration_of_ABC):
        iteration_st = time.time()  # start time of iteration
        result = open(f'{result_file_name}', 'a')    
        
        print(f"iteration number {i}")
        best_bee_of_iteration, best_fitness_of_iteration = Bee_Colony_Algorithm()
        fitness_sum += best_fitness_of_iteration

        # print(f"best bee => data: {best_bee_of_iteration.data}, fitness: {best_fitness_of_iteration}")
        best_bees_each_iter.append(copy.deepcopy(best_bee_of_iteration))
        best_fitnesses_each_iter.append(copy.deepcopy(best_fitness_of_iteration))
        best_fitness_so_far = max(best_fitnesses_each_iter)
        best_fitnesses_so_far.append(best_fitness_so_far)

        result.write(f"iteration number {i}:\n")
        result.write(f"best bee => data: {best_bee_of_iteration.data}, fitness: {best_fitness_of_iteration}\n")  
        result.write(f"best fitness so far: {best_fitness_so_far}\n")

        iteration_et = time.time()  # end time of iteration
        iteration_elapsed_time = iteration_et - iteration_st
        # print(f"Execution time of iteration: {iteration_elapsed_time} seconds\n")
        result.write(f"Execution time of iteration: {iteration_elapsed_time} seconds\n \n")
        
        result.close()

    # clearfiying the bee
    best_bee_so_far = None
    for b in best_bees_each_iter:
        if(b.fitness == best_fitness_so_far):
            best_bee_so_far = b
            
    # writing the result
    result = open(f'{result_file_name}', 'a')
    result.write("------------------------\n")
    result.write("FINAL RESULT\n \n")
        
    fitness_avg = fitness_sum/iteration_of_ABC
    result.write(f"the best Bee of all => \ndata: {best_bee_so_far.data}, fitness: {best_fitness_so_far} \n")
    result.write(f"the average fitness of all: {fitness_avg} \n \n")

    # end time of all
    et = time.time()

    elapsed_time = et - st
    # print('Execution time of all:', elapsed_time, 'seconds')
    result.write(f'Execution time of all: {elapsed_time} seconds \n \n')

    result.write("------------------------\n")
    result.write("COMPARE ANSWER \n \n")
    result.write("real answer = \n")
    result.write(f"my answer = {best_fitness_so_far}\n")
    result.write("loss = \n")
    result.write("try3 loss = \n")
    result.write("betterment than try3 = \n \n")

    result.write("------------------------\n")
    result.write("PARAMETERS\n \n")
    result.write(f"population number = {population_num}\n")
    result.write(f"k = {k}\n")
    result.write(f"max improvement try = {max_improvement_try}\n")
    result.write(f"iteration of ABC Algorithm = {iteration_of_ABC}\n")

    print("---------------------------------")
    # print("RESULT")
    print(f"the best fitness of all: {best_fitness_so_far} \n")
    # print(f"the average fitness of all: {fitness_avg} \n")

    result.close()
    
    iteration_number_list = [i for i in range(1, iteration_of_ABC+1)]
    Diagram.diagram(iteration_number_list, best_fitnesses_each_iter, best_fitnesses_so_far, photo_name)
    
    print()