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
        demands.append(each_demand)
        
    data.readline()
    stations_amount = int(data.readline().split(":")[1])
    data.readline()
    stations = []
    for s in range(stations_amount):
        a = data.readline().split(',')
        stations.append([int(i.strip()) for i in a])
        
    data.readline()
    blocks_amount = int(data.readline().split(":")[1])
    data.readline()
    blocks = []
    for b in range(blocks_amount):
        a = data.readline().split(',')
        blocks.append([int(i.strip()) for i in a])
        
    return demands_amount, demands, stations_amount, stations, blocks_amount, blocks