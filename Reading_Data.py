def Reading(file_name):
    data = open(f"{file_name}", "r")
    nK = int(data.readline().split(":")[1])
    nI = int(data.readline().split(":")[1])
    data.readlines(2)
    Capacity = [int(x) for x in data.readline().split(",")]
    data.readlines(2)
    Profits = [int(x) for x in data.readline().split(",")]
    data.readlines(2)
    Weights = []
    for i in range(nK):
        Weights.append([int(x) for x in data.readline().split(",")])
        
    return nK, nI, Capacity, Profits, Weights