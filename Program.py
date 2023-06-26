import Artificial_Bee_Colony as ABC
import numpy as np
import Reading_Data


if __name__ == '__main__':
    npop = 6   # number of total bees => npop/2 = amount of first population
    # nK = 2     # number of knapsacks
    # nI = 4    # number of items
    # ndim = nK*nI
    limit = 2
    tries = 0
    ncycle = 150
    # lower_bound = [-6 for i in range(ndim)]
    # upper_bound = [6 for i in range(ndim)]
    bestFitness = -1e10
    bestobj = 0
    bestPosition = []
    
    
    # getting the data
    file_name = "Question.txt"
    nK, nI, Capacity, Profits, Weights = Reading_Data.Reading(file_name)
    # nK = number of knapstacks
    # nI = number of items
    
    # ABC = ABC.ABC_algorithm(npop, nK, nI, Capacity, Weights, ndim, limit, lower_bound, upper_bound, ncycle, search_radius=1)
    ABC = ABC.ABC_algorithm(npop, nK, nI, Capacity, Profits, Weights)

    pop = ABC.Initialize()

    Continue = True
    t = 1
    while Continue:
        pop = ABC.employee_search(pop)
        pop = ABC.onlooker_search(pop)
        pop = ABC.scoutBee(pop)

        for bee in pop:
            if bee.fitness > bestFitness:
                bestFitness = bee.fitness
                bestintpos=bee.intpos.copy()
                #bestPosition = [(i, j) for i in range(nK) for j in range(nI) if bee.intpos[i + (j - 1) * nK] > 0]

                #profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
                # obj2 =sum(np.array(bee.intpos) * np.array(profits))
                bestobj = bee.obj
        t += 1

        # if t > ncycle or noimprove > maxNoImprove or time > maxTime:
        if t > ncycle:
            Continue = False

        print("Iteration: %s    Fitness:%.3f     obj:%.3f      position:%s" % (t, bestFitness, bestobj, bestintpos[:4]))