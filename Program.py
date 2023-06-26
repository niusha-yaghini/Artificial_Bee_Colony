import Artificial_Bee_Colony as ABC
import numpy as np
import Reading_Data

if __name__ == '__main__':
    
    population_num = 6   # number of total bees => npop/2 = amount of first population
    k = 3   # number of iterations in roulette wheel
    iteration = 2   # number of total iteration of algorithm
    
    
    # getting the data
    file_name = "Question.txt"

    # nK = number of knapstacks
    # nI = number of items
    nK, nI, Capacity, Profits, Weights = Reading_Data.Reading(file_name)
    
    
    
    # ABC = ABC.ABC_algorithm(npop, nK, nI, Capacity, Weights, ndim, limit, lower_bound, upper_bound, ncycle, search_radius=1)
    ABC = ABC.ABC_algorithm(population_num, nK, nI, Capacity, Profits, Weights, k)
    
    
    # getting result by bees :)
    best_bees = []
    for i in range(iteration):
        population = ABC.employed_bees()
        ABC.onlooker_bees(population)
        best_bee_of_iteration = ABC.finding_best_bee(population)
        best_bees.append(best_bee_of_iteration)
        best_fitness_so_far = max(best_bees)
        print(f"number of iteration: {iteration}")
        print(f"best fitness of iteration: {best_bee_of_iteration}")        
        print(f"best fitness so far: {best_fitness_so_far}\n")        


    # scouts, time showing, diagram showing, saving results in a text



    # ---------------------------------------------------------------------

    # pop = ABC.Initialize()

    # Continue = True
    # t = 1
    # while Continue:
    #     pop = ABC.employee_search(pop)
    #     pop = ABC.onlooker_search(pop)
    #     pop = ABC.scoutBee(pop)

    #     for bee in pop:
    #         if bee.fitness > bestFitness:
    #             bestFitness = bee.fitness
    #             bestintpos=bee.intpos.copy()
    #             #bestPosition = [(i, j) for i in range(nK) for j in range(nI) if bee.intpos[i + (j - 1) * nK] > 0]

    #             #profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    #             # obj2 =sum(np.array(bee.intpos) * np.array(profits))
    #             bestobj = bee.obj
    #     t += 1

    #     # if t > ncycle or noimprove > maxNoImprove or time > maxTime:
    #     if t > ncycle:
    #         Continue = False

    #     print("Iteration: %s    Fitness:%.3f     obj:%.3f      position:%s" % (t, bestFitness, bestobj, bestintpos[:4]))