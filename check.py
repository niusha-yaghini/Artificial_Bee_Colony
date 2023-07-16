rows, cols = (2, 3)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)
arr[0][0] = 1
print(arr)


# for d in range(demands_amount):
#     demand_data = [0 for i in range(self.blocks_amount)]
#     destination_flag = False

#     # finding the first cell
#     choosing_options = []
#     for b in range(self.blocks_amount):
#         if self.demands[d].origin == self.blocks[b].origin:
#             choosing_options.append(b)
#     choosed = random.choice(choosing_options)
#     demand_data[choosed] = 1
    
#     if(self.demands[d].destination == self.blocks[choosed].destination):
#         destination_flag = True
    
#     while(destination_flag == False):
#         choosing_options = []
#         for b in range(self.blocks_amount):
#             if self.blocks[choosed].destination == self.blocks[b].origin:
#                 choosing_options.append(b)
#         choosed = random.choice(choosing_options)
#         demand_data[choosed] = 1
        
#         if(self.demands[d].destination == self.blocks[choosed].destination):
#             destination_flag = True
