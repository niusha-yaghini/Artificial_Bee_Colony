# Artificial_Bee_Colony
modified artificial bee colony algorithm on "bargiri vagon haye bari"

Algorithm Explanation:

there is 2 classes: abc/bee
abc class is were the algorithm starts, with bees
bee class is actually represents each solution that has data and fitness

"employed bees":
1- a list named population will pass to "employee_bees" function, this is for recognizing that if we are in first iteration of algorithm or not, if it was empty, it means we are in first itration, and we make some random solutions (bees) (in amount of "population number"), if it was not empty, it means it's not our first iteration so we skip making new bees part
2- for each "bee" we do the "cross-over" and "mutation", one time, then we calculate the validality of our "new_bee" and the "current_bee" in specific circumstances, we replace the "current_bee" to "new_bee"

    how to do "cross-over":
        in probblity of "cross_over_probblity" we do:
            choose a random position,
            choose a random neighbor,
            we make a "new_bee" somehow that the first part of bee (befor chosen position) be from "current_bee" and the rest of the bee (after chosen position) from "neighbor_bee"

    how to do "mutation":
        in each bee, each line is an answer to a demand, for each demand we want to change it with a certain probblity. (for example if we had 10 demands, and our "mutation_probblity" was 2 (2 in here means, 2 of all demands) it is likely that the algorithm change 2 answers, and untouch 8 demand answers). each new demand answer will be made randomly.

        in amount of "demands_amount" do:
            in probblity of "mutation_probblity" do:
                replacement of demand answer with new randomly made answer.

    circumstances for replacement:
        -------------------------------------------------
        |  validality_flag_current_bee:   | false | true |
        |  validality_flag_new_bee:       |   -   | true |
        |  improvement_flag:              |   -   | true |
        |---------------------------------|-------|------|
        |  replacement:                   | true  | true |
        -------------------------------------------------
    replacement will be false in any other condition:
        if replacement was true -> turn "improvement_try" property of that bee to zero
        if replacement was false -> add one to "improvement_try" property of that bee


"onlooker bees": (we do these in amount of "onlooker_bees_number")
1- we choose a "bee" by "roulette wheel" or "Tournoment" procedure (if it be "" roullette wheel we do this in amount of "RW_iteration" variable) 
2- we pass the choosen "bee" to "try_for_improvement"
3- in "try_for_improvement" we do "cross-over" and "mutation"
4- after that with following above rules we decide to replace the bee or not
5- we check that if doing cross-over and mutation had made any change or not, for any bee that change has be made, we add one to that bee's "improvement_try" property, if there was a change we set the "improvement_try" property equal to zero
7- after that we update the "best_fitness_so_far", and it will pass it to scout bees

"scout bees":
1- here we delete the all the bees that their "improvement_try" property is more than the "max_improvement_try" variable
2- we make new bees randomly in amount of deleted bees
3- we check if the limits of ending algorithm has been reached or not, if it has reached we come out of the algorithm, if not, it goes to employee bees section