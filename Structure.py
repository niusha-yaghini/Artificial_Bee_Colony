# classes: Station(istgah), Block(khotot), Demand(taghaza)

class Demand():
    
    def __init__(self, Index, Origin, Destination, Volume):
        self.d_index = Index
        self.d_origin = Origin
        self.d_destination = Destination
        self.d_volume = Volume
        
        
class Station():
    # we have limits in here
    
    def __init__(self, Index, Block_Capacity, Demand_Capacity):
        self.s_index = Index
        self.s_block_capacity = Block_Capacity
        self.s_demand_capacity = Demand_Capacity
        
        
class Block():
    
    def __init__(self, Index, Origin, Destination, Cost_Per_Unit):
        self.b_index = Index
        self.b_origin = Origin
        self.b_destination = Destination
        self.b_cost = Cost_Per_Unit
