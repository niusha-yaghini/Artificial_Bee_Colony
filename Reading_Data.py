from Structure import *

def Reading(file_name):
        
    data = open(f"{file_name}", "r")
    demands_amount = int(data.readline().split(":")[1])
    data.readline()
    demands = []
    for d in range(demands_amount):
        each_demand = []
        acceptable_blocks = []
        for i in data.readline().split(','):
            i = i.strip()
            if i.startswith('[') and i.endswith(']'):
                i = i[1:-1]  # Remove the brackets
                acceptable_blocks.append([int(j.strip()) for j in i.split(' ')])
            else:
                # Convert the substring to a number and add it to the list
                each_demand.append(int(i))
        each_demand.extend(acceptable_blocks)
        demands.append(Demand(each_demand[0], each_demand[1], each_demand[2], each_demand[3], each_demand[4]))
        
    data.readline()
    stations_amount = int(data.readline().split(":")[1])
    data.readline()
    stations = []
    for s in range(stations_amount):
        a = [int(i.strip()) for i in data.readline().split(',')]
        stations.append(Station(a[0], a[1], a[2]))
        
    data.readline()
    blocks_amount = int(data.readline().split(":")[1])
    data.readline()
    blocks = []
    for b in range(blocks_amount):
        a = [int(i.strip()) for i in data.readline().split(',')]
        blocks.append(Block(a[0], a[1], a[2], a[3]))
        
    return demands_amount, demands, stations_amount, stations, blocks_amount, blocks