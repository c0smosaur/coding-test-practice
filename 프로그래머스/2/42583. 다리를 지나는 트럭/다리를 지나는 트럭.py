from collections import deque

def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    on_bridge = deque() # (weight, remaining time)
    time = 0
    curr_weight = 0
    
    while waiting or on_bridge:
        time += 1
        
        if on_bridge and on_bridge[0][1] == 0:
            truck = on_bridge.popleft()
            curr_weight -= truck[0]
            
        if waiting and curr_weight + waiting[0] <= weight and len(on_bridge) < bridge_length:
            truck = waiting.popleft()
            on_bridge.append((truck, bridge_length))
            curr_weight += truck
        
        on_bridge = deque([(t[0], t[1]-1) for t in on_bridge])
    
        
    return time