def gas_station(gas, cost):
    if sum(gas) < sum(cost):
        return -1
        
    total_tank = 0
    starting_station = 0
    
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        
        # If we can't reach the next station
        if total_tank < 0:
            # Try starting from the next station
            starting_station = i + 1
            # Reset tank
            total_tank = 0
            
    return True  if starting_station < len(gas) else False



print(gas_station(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))