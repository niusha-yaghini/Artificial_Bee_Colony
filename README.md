# Artificial_Bee_Colony

Algorithm Explanation:

there is 2 classes: abc/bee
abc class is were the algorithm starts, with bees
bee class is actually represents each solution that has data and fitness

first algorithm starts with "employed bees":
1- we make random valid solution (in amount of the have of the population number)
2- for each solution we do the cross-over and mutation by choosing the bee with roulette wheel procedure, one time (if doing the cross-over or mutation make improvement, we replace the result with original)
3- we make a array that reperesent the amount of "cross-ove, mutation done" on each bee
4- if there was not any improvement the number of that bee increases 1 time