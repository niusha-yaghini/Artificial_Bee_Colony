# classes: Station(istgah), Block(khotot), Demand(taghaza)

class Demand():
    
    def __init__(self, Index, Origin, Destination, Volume, Acceptable_Blocks):
        self.index = Index
        self.origin = Origin
        self.destination = Destination
        self.volume = Volume
        self.acceptable_blocks = Acceptable_Blocks
        
        
class Station():
    # we have limits in here
    
    def __init__(self, Index, Block_Capacity, Demand_Capacity):
        self.index = Index
        self.block_capacity = Block_Capacity
        self.demand_capacity = Demand_Capacity
        
        
class Block():
    
    def __init__(self, Index, Origin, Destination, Cost_Per_Unit):
        self.index = Index
        self.origin = Origin
        self.destination = Destination
        self.cost = Cost_Per_Unit