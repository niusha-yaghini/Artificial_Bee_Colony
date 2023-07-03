import Artificial_Bee_Colony
import numpy as np
import Reading_Data
import time


def Bee_Colony_Algorithm():
    # ABC = ABC.ABC_algorithm(npop, nK, nI, Capacity, Weights, ndim, limit, lower_bound, upper_bound, ncycle, search_radius=1)
    ABC = Artificial_Bee_Colony.ABC_algorithm(population_num, nK, nI, Capacity, Profits, Weights, k)
    population = ABC.employed_bees()
    ABC.onlooker_bees(population)
    best_bee_of_iteration, best_fitness_of_iteration = ABC.finding_best_bee(population)
    
    return best_bee_of_iteration, best_fitness_of_iteration


if __name__ == '__main__':
    
    population_num = 6   # number of total bees => npop/2 = amount of first population
                         # this must be an even number 
    k = 3   # number of iterations in roulette wheel
    iteration_of_ABC = 5   # number of total iteration of algorithm
    
    
    # file name of the datas
    data_file_name = "Question.txt"
    
    # file name for save results
    result_file_name = "results.txt"

    # nK = number of knapstacks
    # nI = number of items
    nK, nI, Capacity, Profits, Weights = Reading_Data.Reading(data_file_name)
    
        
    
    # getting result by bees :)
    st = time.time() # get the start time of all
    
    result = open(f'{result_file_name}', 'a')
    result.write(f"Artificial Bee Algorithm \n \n")        
    result.close()


    # 1) writing the results in a text
    # 2) getting the time of algorithm in each iteration
    
    best_bees = []
    best_fitnesses = []
    fitness_sum = 0
    for i in range(iteration_of_ABC):
        iteration_st = time.time()  # start time of iteration
        result = open(f'{result_file_name}', 'a')    
        
        print(f"iteration number {i}:")
        best_bee_of_iteration, best_fitness_of_iteration = Bee_Colony_Algorithm()
        fitness_sum += best_fitness_of_iteration
        print(f"best bee => data: {best_bee_of_iteration.data}, fitness: {best_fitness_of_iteration}")
        best_bees.append(best_bee_of_iteration)
        best_fitnesses.append(best_fitness_of_iteration)
        best_fitness_so_far = max(best_fitnesses)
        result.write(f"iteration number {i}:\n")
        result.write(f"best bee => data: {best_bee_of_iteration.data}, fitness: {best_fitness_of_iteration}\n")  
        result.write(f"best fitness so far: {best_fitness_so_far}\n")
        iteration_et = time.time()  # end time of iteration
        iteration_elapsed_time = iteration_et - iteration_st
        print(f"Execution time of iteration: {iteration_elapsed_time} seconds\n")
        result.write(f"Execution time of iteration: {iteration_elapsed_time} seconds\n \n")
        
        result.close()

    result = open(f'{result_file_name}', 'a')
    result.write("---------------------\n")
    result.write("RESULT\n \n")
        
    best_fitness_of_all = max(best_fitnesses)
    fitness_avg = fitness_sum/iteration_of_ABC
    result.write(f"the best fitness of all: {best_fitness_of_all} \n")
    result.write(f"the average fitness of all: {fitness_avg} \n")


    print("------------------------------")
    print("RESULT")
    print(f"the best fitness of all: {best_fitness_of_all} \n")
    print(f"the average fitness of all: {fitness_avg} \n")


    # end time of all
    et = time.time()

    elapsed_time = et - st
    print('Execution time of all:', elapsed_time, 'seconds')
    result.write(f'Execution time of all: {elapsed_time} seconds')

    result.close()
     

    # scouts, diagram showing
